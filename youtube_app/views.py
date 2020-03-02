from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'resourses/index.html')




def about(request):
    return render(request, 'resourses/about.html')