from dataclasses import fields
from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ('lesson_id', 'nom', 'video', 'fpe', 'pdf' , 'position')
