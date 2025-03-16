from django.http import HttpResponse
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Course
from  .forms import AddCourseForm
from trainee.models import Trainee



# Create your views here.
def ListOfCourse(req):
    context = {
        'courses': Course.objects.all()
    }
    return render(req , 'course/ListView.html',context)

def AddCourse(req):
    form = AddCourseForm()
    if req.method == 'POST':
        form = AddCourseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('ListOfCourse')

    return render(req, 'course/addform.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import AddCourseForm

def UpdateCourse(req, id):
    course = get_object_or_404(Course, id=id)
    form = AddCourseForm(instance=course)

    if req.method == 'POST':
        form = AddCourseForm(req.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('ListOfCourse')

    return render(req, 'course/updatecourse.html', {'form': form})

def DeleteCourse(req , id):
    course = Course.objects.get(id=id)
    course.delete()
