from random import choice
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from core.models import Game

CHOICE = ['Rock', 'Paper', 'Scissors']


def rps_list(request):
    games = Game.objects.all()
    user = request.user
    data = {
        'user': user,
        'games': games
    }
    return render(request, 'rps_list.html', data)

def play_user(request, pk):
    if request.method == 'POST':
        defender = request.POST.get('defender', None)
        atk_choice = request.POST.get('atk_choice', None)
        Game.objects.create(
            atk_user = User.objects.get(pk=pk),
            dfn_user = User.objects.get(pk=defender),
            atk_choice = atk_choice,
            dfs_choice = '',
            result = '진행중'
        )
        return redirect(reverse('rps_list'))
    elif request.method == 'GET':
        users = User.objects.all().exclude(username=request.user)
        user = User.objects.get(pk=pk)
        data = {
            'user': user,
            'users': users,
        }
        return render(request, 'rps_play.html', data)

def rps_compete(request, pk):
    if request.method == 'POST':
        dfn_choice = request.POST.get('dfn_choice', None)
        game = Game.objects.get(pk=pk)

        if game.atk_choice == 'Rock':
            if dfn_choice == 'Paper':
                result = str(game.dfn_user) + " Win"
            elif dfn_choice == 'Scissors':
                result = str(game.atk_user) + " Win"
            elif dfn_choice == 'Rock':
                result = "Tie"

        elif game.atk_choice == 'Scissors':
            if dfn_choice == 'Rock':
                result = str(game.dfn_user) + " Win"
            elif dfn_choice == 'Paper':
                result = str(game.atk_user) + " Win"
            elif dfn_choice == 'Scissors':
                result = "Tie"

        elif game.atk_choice == 'Paper':
            if dfn_choice == 'Scissors':
                result = str(game.dfn_user) + " Win"
            elif dfn_choice == 'Rock':
                result = str(game.atk_user) + " Win"
            elif dfn_choice == 'Paper':
                result = "Tie"
        Game.objects.filter(pk=pk).update(dfs_choice=dfn_choice, result=result)
        return redirect(reverse('rps_list'))

    elif request.method == 'GET':
        users = User.objects.all().exclude(username=request.user)
        data = {
            'users': users,
        }
        return render(request, 'rps_compete.html', data)


def rps_detail(request, pk):
    game = Game.objects.get(pk=pk)
    data={
        'game': game
    }
    return render(request, 'rps_detail.html', data)

def play_cpu(request, pk):
    if request.method == 'POST':
        atk_choice = request.POST.get('atk_choice', None)
        atk_user = User.objects.get(pk=pk)
        dfn_choice = choice(CHOICE)

        if atk_choice == 'Rock':
            if dfn_choice == 'Paper':
                result = str(atk_user) + " Lose"
            elif dfn_choice == 'Scissors':
                result = str(atk_user) + " Win"
            elif dfn_choice == 'Rock':
                result = "Tie"

        elif atk_choice == 'Scissors':
            if dfn_choice == 'Rock':
                result = str(atk_user) + " Lose"
            elif dfn_choice == 'Paper':
                result = str(atk_user) + " Win"
            elif dfn_choice == 'Scissors':
                result = "Tie"

        elif atk_choice == 'Paper':
            if dfn_choice == 'Scissors':
                result = str(atk_user) + " Lose"
            elif dfn_choice == 'Rock':
                result = str(atk_user) + " Win"
            elif dfn_choice == 'Paper':
                result = "Tie"
        Game.objects.create(
            atk_user = User.objects.get(pk=pk),
            atk_choice = atk_choice,
            dfs_choice = dfn_choice,
            result = result,
        )
        return redirect(reverse('rps_list'))
    elif request.method == 'GET':
        user = User.objects.get(pk=pk)
        data = {
            'user': user,
        }
        return render(request, 'play_cpu.html', data)