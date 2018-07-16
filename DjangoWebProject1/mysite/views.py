from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

user_list = [
    {"user":"flansk","pwd":"22002"},
    ]


def index(request):
    #return HttpResponse("Hello World!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = {"user":username,"pwd":password}
        user_list.append(user)
    return render(request, "index.html",{"users":user_list})