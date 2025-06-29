from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Prestamo
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    libros = Libro.objects.all()
    return render(request, 'inicio.html', {'libros': libros})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

@login_required
def prestar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if libro.disponible:
        Prestamo.objects.create(
            usuario=request.user,
            libro=libro,
            fecha_prestamo=timezone.now()
        )
        libro.disponible = False
        libro.save()
    return redirect('lista_libros')

@login_required
def historial_usuario(request):
    prestamos = Prestamo.objects.filter(usuario=request.user).order_by('-fecha_prestamo')
    return render(request, 'historial.html', {'prestamos': prestamos})
