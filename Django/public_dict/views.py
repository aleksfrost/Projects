from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from . buissines import read_words, write_words

# Create your views here.


def home(request):
    return render(request, "home.html")

def show(request):
    words_to_show = read_words
    context = {'to_show': words_to_show}
    return render(request, 'words_list.html', context)

def add(request):
    if request.method == 'POST':
        write_words(request.POST['word1'], request.POST['word2'])
        return HttpResponseRedirect('/')
    return render(request, 'add_word.html')