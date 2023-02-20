from xml.parsers.expat import model
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from .form import LessonForm

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

class LessonCreateView(CreateView):
    form_class= LessonForm
    context_object_name= 'matieres'
    model= Matiere
    template_name='programmes/lessoncreate.html'

    def get_success_url(self):
        self.object = self.get_object
        niveau = self.object.niveaux
        return reverse_lazy('programmes:lessonlist', kwargs={'niveau':niveau, 'slug':self.object.slug})



    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        ls = form.save(commit=False)
        ls.creer_par = self.request.user
        ls.niveaux = self.object.niveaux
        ls.matiere = self.object
        ls.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonUpdateView(UpdateView):
    fields = ('nom', 'position', 'pdf', 'fpe')
    context_object_name =  'lesson'
    model = Lesson
    template_name = 'programmes/lessonupdate.html'

class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'programmes/lessondelete.html'

    def get_success_url(self):
        niveau = self.object.niveaux
        return reverse_lazy("programmes:lessonlist", kwargs={'niveau':niveau, 'slug':self.object.matiere.slug})