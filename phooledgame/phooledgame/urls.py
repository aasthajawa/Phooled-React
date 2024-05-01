"""
URL configuration for phooledgame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from game.views import account, phish_game
#from homepage import views as HomePageViews

""" urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game.urls')),
    path('api/login', views.user_login ),
    path('api/signup', views.user_signup),
    path('api/create-room', views.create_game_room),
    path('api/start-game', views.start_game),
    path('api/images/', views.list_images, name='list_images'),

     path('', HomePageViews.homepage, name="index")
  
    path('', include('django.contrib.auth.urls'))
    ,path('', include('account.urls'))
    ,path('system-admin/', admin.site.urls)
    ,path('game/', include('gamification.urls'))
    ,path('rest/', include('rest.urls')) 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """


urlpatterns = [
    path('system-admin/', admin.site.urls),
    path('api/signup', account.user_signup),
    path('api/login', account.user_login ),
    path('api/game/dashboard', account.user_dashboard),
    path('api/game/phish-game', phish_game.phish_game_view),
    path('api/phish-game/create', phish_game.phish_game_handler),
    #path('api/phish-game/room/<str:room_id>/', phish_game.phish_room_handler, name="phishgame_room_view"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
