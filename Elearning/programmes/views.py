from xml.parsers.expat import model
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView


class NiveauListView(ListView):
    model= Niveaux
    context_object_name='niveaux'
    template_name= 'programmes/niveaulist.html'
    
class MatiereListView(DetailView):
    model= Niveaux
    context_object_name='niveau'
    template_name= 'programmes/matierelist.html'

class LessonListView(DetailView):
    model= Matiere
    context_object_name='matieres'
    template_name= 'programmes/lessonlist.html'


class LessonListViewDetail(DetailView):
    model= Lesson
    context_object_name='lesson'
    template_name= 'programmes/LessonListdetail.html'