from django.shortcuts import render

# Create your views here.
def indexProf(request):
    return render(request, 'Prof/Prof.html')