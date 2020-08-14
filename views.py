#i have created this file- shresth
from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
   
   return render(request, "index.html")
   # return HttpResponse("hello harry bhai ")

   



   


def about(request):
   return HttpResponse("<h1>hearry</h1> <a href="">google</a>")

def removepunc(request):
   
   djtext=request.GET.get('text', 'default')
   rs=request.GET.get('rs','off')
   cs=request.GET.get('cs','off')
   sr=request.GET.get('sr','off')
   if rs=='on':
      punclist='''.!%^&*()><.,/*-+@#$"%`~``~'''
      analyzed=""
      for char in djtext:
         if char not in punclist:
            analyzed=analyzed+char
            
      params={'purpose':'removed punctuation','analyzedtext':analyzed}
      return render(request, "analyze.html", params)

   elif (cs=='on'):
      analyzed=''
      for char in djtext:
         analyzed+=char.upper()
      params={'purpose':'Capitalize the text','analyzedtext':analyzed}
      return render(request, "analyze.html", params)
      
   elif (cs=='on' and rs=='on'):
      analyzed=''
      for char in djtext:
         if char not in punclist:
            analyzed+=char.upper()
      params={'purpose':'Capitalized the text','analyzedtext':analyzed}
      return render(request, "analyze.html", params)
      
   elif sr=='on':
      analyzed=''
      for index,i in enumerate(djtext):
         if not(djtext[index]==" " and djtext[index+1]==" "):
            analyzed+=djtext[index]
      params={'purpose':'Space Removed','analyzedtext':analyzed}
      return render(request, "analyze.html", params)      
            
      
      
      
      
   else:
      return HttpResponse("<h1 style=text-align: center;>Please select any one task !</h1>")

def capital(request): 
   return HttpResponse("Capital")
