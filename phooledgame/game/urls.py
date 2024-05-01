from django.urls import path
from .views.account import user_login, user_signup, start_game, user_dashboard
from .views.account import create_game_room, list_images
from django.conf import settings
from django.conf.urls.static import static
from .views.phish_game import phish_game_view, phish_game_handler, phish_room_handler
urlpatterns = [
   
    path('api/login/', user_login, name='user-login'),
    path('api/signup/', user_signup, name='user-signup'),
    path('create-room/', create_game_room, name='create-game-room'),
    path('start-game/', start_game, name='start-game' ),
    path('api/images/', list_images, name='list_images'),
    path('api/game/dashboard', user_dashboard),
    path('api/game/phish-game', phish_game_view),
    path('api/phish-game/create', phish_game_handler),
    #path('phish-game/room/<str:room_id>/', phish_room_handler, name="phishgame_room_view")
]
    # Add more URLs as needed

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)