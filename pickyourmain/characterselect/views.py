from django.shortcuts import render
from.models import Char
import string 

def select(request):
	return render(request, 'characterselect/select.html')


def character(request,char):
	character = Char.objects.get(stripname = char)
	return render(request, 'characterselect/character.html',
		{'char': character})
	
# Create your views here.
