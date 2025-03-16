from django import forms
from .models import Course

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

