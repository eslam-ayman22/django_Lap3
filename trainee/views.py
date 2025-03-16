from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Trainee ,Course
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


# list and add using class based view

class ListTraineeView(LoginRequiredMixin,ListView):
    model = Trainee
    template_name = "trainee/ListView.html"
    context_object_name = "trainees"

    def get_queryset(self):
        return Trainee.objects.filter(isactive=True)



class AddTraineeView(LoginRequiredMixin,CreateView):
    model = Trainee
    template_name = "trainee/addtrainee.html"
    fields = ["name", "email", "img", "course"]
    success_url = reverse_lazy("trainee_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context


#update traine using generic view

class UpdateTrainee(LoginRequiredMixin,UpdateView):
    model = Trainee
    fields = ['name', 'email', 'img']
    template_name = 'trainee/UpdateView.html'
    pk_url_kwarg = 'trainee_id'
    success_url = reverse_lazy('trainee_list')


def DeleteTrainee(req , trainee_id):
    Trainee.objects.filter(trainee_id=trainee_id).update(isactive=False)
    return redirect('trainee_list')

