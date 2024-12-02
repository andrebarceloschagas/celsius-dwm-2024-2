from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from django.urls import reverse_lazy
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.generics import DestroyAPIView

from .models import Temperatura
from .forms import TemperaturaForm
from .serializers import TemperaturaSerializer

# Create your views here.
def index(request):
    return render(request, 'templates/index.html')

def temperatura(request):
    if request.method == 'POST':
        form = TemperaturaForm(request.POST)
        if form.is_valid():
            form.save()
            form = TemperaturaForm()
    else:
        form = TemperaturaForm()
    return render(request, 'templates/temperatura.html', {'form': form})

def temperatura_delete(request, id):
    try:
        temperatura = Temperatura.objects.get(id=id)
        temperatura.delete()
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'templates/temperatura.html')

def temperatura_edit(request, id):
    temperatura = Temperatura.objects.get(id=id)
    if request.method == 'GET':
        form = TemperaturaForm(instance=temperatura)
    else:
        form = TemperaturaForm(request.POST, instance=temperatura)
        if form.is_valid():
            form.save()
    return render(request, 'templates/temperatura.html', {'form': form})

class TemperaturaList(ListView):
    model = Temperatura
    template_name = 'templates/temperatura_list.html'

class TemperaturaCreate(CreateView):
    model = Temperatura
    form_class = TemperaturaForm
    template_name = 'templates/temperatura_form.html'
    success_url = reverse_lazy('temperatura_list')

class TemperaturaUpdate(UpdateView):
    model = Temperatura
    form_class = TemperaturaForm
    template_name = 'templates/temperatura_form.html'
    success_url = reverse_lazy('temperatura_list')

class TemperaturaDelete(DeleteView):
    model = Temperatura
    template_name = 'templates/temperatura_delete.html'
    success_url = reverse_lazy('temperatura_list')

class TemperaturaListAPI(ListAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TemperaturaDeleteAPI(DestroyAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

def download(request):
    try:
        file = open('temperatura.csv', 'r')
        return FileResponse(file)
    except FileNotFoundError:
        raise Http404
    
def download_api(request):
    try:
        file = open('temperatura.csv', 'r')
        return FileResponse(file)
    except FileNotFoundError:
        raise Http404
    

