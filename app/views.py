from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse('I HAVE DONE')
def hi(request):
    return render(request,'hi.html')