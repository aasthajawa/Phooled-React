import logging
from game.models import PhishGameSession
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import FormView, TemplateView

#import arrow
import shortuuid
#from game.models import User
from game import game_engine, utils
#from gamification.choices import QuestionCategory
#from gamification.composers import QuestionComposer
from game.const import GameStates
#from game.forms import (
   # MultipleChoiceForm,
    #MultipleSelectionForm,
#)  
#from game.helpers import Question
from game.models import GameState
""" from gamification.models import (
    GamificationQuestionTemplate as QuestionTemplate,  # Gets the model for gamification templates imported
)
from gamification.models import PhishGameSession, UserAchievement, phish_game
from gamification.models.session import QuizSession, SessionQuestion
from phish.models import PhishingSample
from utils.datehelper import DateHandler """



@api_view(['GET'])
@login_required
def phish_game_view(request):

    print("I am finally here", request)
    active_games_info = []

    active_games = GameState.objects.exclude(state=GameStates.FINISH)
    if active_games:
        for game in active_games:
            active_games_info.append(
                {
                    "id": game.session.id,
                    #"host": (
                        #   utils.get_user_name(game.session.owner)
                        #   if game.session.owner != 0
                        #   else "No Host"
                    #),
                }
            )

    context = {
        "active_games": active_games_info,
    }
    return Response({'detail': 'Game room created successfully', 'context': context})

@api_view(['GET'])
@login_required
def phish_game_handler(request):

    print("I am finally2 here", request)
    this_uuid = None

    while this_uuid == None:
        this_uuid = shortuuid.uuid()[:10]
        if PhishGameSession.objects.filter(id=this_uuid).first():
            this_uuid = None

    game_engine.GameEngine().create_new_session(session_id=this_uuid)

    print("I am finally3 here")
    session = PhishGameSession.objects.filter(id=this_uuid).first()
    if not PhishGameSession.objects.filter(id=this_uuid).first():
        context = {"message": "The room does not exist!"}
        return Response({'detail': 'Game room created successfully', 'context': context})

    context = {
        "room_id": this_uuid,
        "user": request.user.username,
        "userId": request.user.user_id,
        "gameOwner": session.owner,
        "is_server": str(int(utils.is_current_instance_server())),
    }
    return Response({'detail': 'Game room created successfully', 'context': context})



   