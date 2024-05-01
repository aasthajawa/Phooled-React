from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from game.models import GameRoom, Image, User
from game.serializers import ImageSerializer
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    print(username)
    print(password)
    
    user = authenticate(request, username = username, password=password)
    print("user", user)
    if user is not None:
        login(request, user)
        user_data = {
        'username': user.username,
        'email': user.email,
        'user_id': user.user_id
        # Add other user data as needed
    }
        return Response({'detail': 'Login successful', 'user': user_data})
    else:
        return Response({'detail': 'Invalid credentials'}, status=401)
 
@api_view(['POST'])
def user_signup(request):
   
    username = request.data.get('username')
    password = request.data.get('password')
    user_email = request.data.get('email')
   
    if User.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, email=user_email, password=password)
    
    login(request, user)
    return Response({'detail': 'Signup successful'})

@api_view(['POST'])
def create_game_room(request):
    print("request", request)
    room_name = request.data.get('roomName')
    user_id = request.data.get('gameStarter')
    print("user_id", user_id)

    User = get_user_model()

    try:
       user_instance = User.objects.get(pk=user_id)
    except User.DoesNotExist:
    # Handle the case where the user with the specified ID does not exist
       user_instance = None

    # Check if the user instance exists
    if user_instance:
        print("user_instance", user_instance)
    # Create the GameRoom instance and assign the admin
     
        room = GameRoom.objects.create(room_name=room_name, game_starter=user_instance)
        room_url = '/game/phish-game/room/' + str(room.room_name)  # Assuming room_detail is your URL pattern for viewing a specific room
        room.room_url = room_url
        room.save()
        room.players.add(user_instance) 
        print("room.players", room.players.all())


    # Other logic to handle successful room creation
    else:
    # Handle the case where the user instance is not found
        print("User with ID {} does not exist.".format(user_id))
    room_data = {
        'room_name': room.room_name,
        'room_id': room.id, 
        'room_players': [player.username for player in room.players.all()],
        'room_url': room_url
        # Add other user data as needed
    }
    return Response({'detail': 'Game room created successfully', 'room': room_data})

@api_view(['POST'])
def start_game(request):
    room = GameRoom.objects.first()
    room.game_started = True
    room.save()
    return Response({'detail': 'Game started successfully'})
    
    #if request.user == room.admin:
        # Set game state to started
        
@api_view(['GET'])
def list_images(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
def user_dashboard(request):
    login_url = "/login/"
    redirect_field_name = "next"
    user = request.user
    print("idhar hu", user)
    curUserName = user.username
    curUserID = user.user_id  # Stores current User ID
    user_data = {
        'curUserName': curUserName,
        'curUserID': curUserID
    }
    return Response({'detail': 'Game room created successfully', 'user': user_data})
