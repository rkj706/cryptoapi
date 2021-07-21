from django.shortcuts import render

from django.http import HttpResponse
from .models import CoinGraph, CoinList

# Create your views here.

def testing(request):
    # for coin in CoinGraph.objects:
    #     print(coin.hourly_data)
    coins = CoinList.objects.all()
    return HttpResponse(coins)