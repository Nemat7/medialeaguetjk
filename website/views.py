from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.generic import ListView
from .models import Player
# Create your views here.

def voting_page(request):
    players = Player.objects.all()
    csrf_token = get_token(request)
    return render(request, 'voting_page.html', {'players': players, 'csrf_token': csrf_token})


def vote_player(request, player_id):
    if request.method == "POST":
        if not request.session.get('voted', False):
            player = get_object_or_404(Player, id=player_id)
            player.votes += 1
            player.save()
            request.session['voted'] = True
            return JsonResponse({"success": True, "message": "Vote counted!"})
        else:
            return JsonResponse({"success": False, "message": "You have already voted."})
    return JsonResponse({"success": False, "message": "Invalid request."})