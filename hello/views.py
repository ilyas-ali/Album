from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Album,Song
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = "hello/index.html"
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = "hello/detail.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = "hello/album_form.html"

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = "hello/album_form.html"
    
class AlbumDelete(DeleteView):
    model= Album
    success_url= reverse_lazy('hello:index')


class UserFormView(View):
    form_class=UserForm
    template_name= "hello/registration_form.html"

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form' : form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('hello:index')
        
        return render(request,self.template_name,{'form' : form})

def welcome(request):
    return render(request,'hello/welcome.html')