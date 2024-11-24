from django.shortcuts import render,HttpResponse

# Create your views here.
def home(reequest):
    return HttpResponse("hey this is my Django server ")