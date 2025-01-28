from django.urls import path
from .views import voting_page, vote_player

urlpatterns = [
    path('', voting_page, name='voting_page'),
    path('vote/<int:player_id>/', vote_player, name='vote_player'),

]