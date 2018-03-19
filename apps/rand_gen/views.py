from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
  context = { "unique_word": get_random_string(length=14) }
  if 'counter' not in request.session:
        request.session['counter'] = 0
  request.session['counter'] += 1
  return render(request,'index.html', context)

def reset(request):
    request.session['counter'] = 0
    return redirect('/')
