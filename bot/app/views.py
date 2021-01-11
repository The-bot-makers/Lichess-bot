from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import Process
from botfiles import lichessbot

bot=""

# Create your views here.
def launch(request):
    bot=Process(target=lichessbot.launchbot, args=[])
    return HttpResponse("launched")
def term(request):
    bot.terminate()
    return HttpResponse("terminated")
    
