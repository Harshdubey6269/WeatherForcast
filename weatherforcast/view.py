from django.shortcuts import render
def ShowInterface(request):
    return render(request,'index.html')