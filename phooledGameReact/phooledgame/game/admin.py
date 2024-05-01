from django.contrib import admin

# Register your models here.
from .models import GameRoom, Image, User, PhishGameSession, GameState, PhishGameSessionPlayer, PhishGameSessionCards, PhishingAttribute, PhishingSample

admin.site.register(GameRoom)
admin.site.register(Image)
admin.site.register(User)
admin.site.register(PhishGameSession)
admin.site.register(GameState)
admin.site.register(PhishGameSessionPlayer)
admin.site.register(PhishGameSessionCards)
admin.site.register(PhishingSample)
admin.site.register(PhishingAttribute)