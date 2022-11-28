from django.shortcuts import render

# Create your views here.


def app1_first(request):
    return render(request, 'app1_first.html')


def app1_second(request):
    return render(request, 'app1_second.html')
