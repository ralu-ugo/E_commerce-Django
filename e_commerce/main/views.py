from django.shortcuts import render, redirect

def title(request):
    return render(request, "title.html")

def preview1(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("title.html")
    return render(request, "p1.html")


# Create your views here.
