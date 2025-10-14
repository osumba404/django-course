#from django.http import HttpResponse

# def hompage(request):
#     return HttpResponse("Welcome to the homepage!")

# def about(request):
#     return HttpResponse("This is the about page.")


from django.shortcuts import render

def hompage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
