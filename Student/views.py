from django.shortcuts import render

# Create your views here.
def indexStudent(request):
    return render(request, 'Student/Student.html')