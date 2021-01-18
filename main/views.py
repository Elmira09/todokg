from django.shortcuts import render, HttpResponse, HttpResponse


def homepage(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")
    
    
def check(request):
    return HttpResponse("Текшерүү")

def test3(request):
    return HttpResponse("This is page test3")