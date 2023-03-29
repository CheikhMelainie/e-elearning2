from multiprocessing import context
from turtle import fd
from xml.parsers.expat import model
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView
from .form import LessonForm, ComForm, RepForm

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


class LessonListViewDetail(DetailView, FormView):
    model= Lesson
    context_object_name='lesson'
    template_name= 'programmes/LessonListdetail.html'
    form_class =  ComForm
    second_form_class = RepForm

    def get_context_data(self, **kwargs):
        context = super(LessonListViewDetail, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context
    
    def form_valid(self, form):
            self.object = self.get_object()
            fd = form.save(commit=False)
            fd.auteur = self.request.user
           # fd.nom_lesson = self.object.comments.nom
            fd.nom_lesson_id = self.object.id
            fd.save()
            return HttpResponseRedirect(self.get_success_url())

    def form_valid2(self, form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.nom_comm_id = self.request.POST.get('comment_id')
        fd.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveaux
        matiere = self.object
        return reverse_lazy('programmes:lessonlistdetail', kwargs={
            'niveau':niveau,
            'matiere':matiere,
            'slug':self.object.slug
        })


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class

            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'
        form = self.get_form(form_class)

        if form_name=='form' and form.is_valid():
            print('nouveau commentaire')
            return self.form_valid(form)

        if form_name=='form2' and form.is_valid():
            print('nouvelle reponse')
            return self.form_valid2(form)
        






class LessonCreateView(CreateView):
    form_class= LessonForm
    context_object_name= 'matieres'
    model= Matiere
    template_name='programmes/lessoncreate.html'

    def get_success_url(self):
        self.object = self.get_object()
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