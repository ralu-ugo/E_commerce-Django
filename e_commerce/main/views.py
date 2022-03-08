from django.shortcuts import render, redirect

def title(request):
    context = {
        "section" : "home"
    }
    return render(request, "title.html", context = context)



def preview1(request):
    context = {
        "section" : "preview"
    }

    return render(request, "p1.html", context = context)



# Create your views here.
