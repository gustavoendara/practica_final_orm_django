from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Laboratorio
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'laboratorio/home.html'
    
class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'  
    context_object_name = 'laboratorios'

class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_detail.html'
    context_object_name = 'laboratorio'

class LaboratorioCreateView(SuccessMessageMixin, CreateView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')
    success_message = "Laboratorio creado con éxito"

class LaboratorioUpdateView(SuccessMessageMixin, UpdateView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')
    success_message = "Laboratorio actualizado con éxito"

class LaboratorioDeleteView(SuccessMessageMixin, DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    context_object_name = 'laboratorio'
    success_url = reverse_lazy('laboratorio_list')
    success_message = "Laboratorio eliminado con éxito"
