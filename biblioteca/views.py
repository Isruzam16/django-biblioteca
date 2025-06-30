from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Prestamo
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.serializers import serialize
from django.http import HttpResponse
from django import forms

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
    prestamos_activos = Prestamo.objects.filter(usuario = request.user, devuelto=False)
    if prestamos_activos.exists():
        return render(request, 'error_prestamo.html', {'mensaje': 'Ya tienes este libro prestado.'})
    if libro.stock > 0:
        Prestamo.objects.create(
            usuario=request.user,
            libro=libro,
            fecha_prestamo=timezone.now()
        )
        libro.stock -= 1
        if libro.stock == 0:
            libro.disponible = False
        libro.save()
    return redirect('lista_libros')

@login_required
def historial_usuario(request):
    prestamos = Prestamo.objects.filter(usuario=request.user).order_by('-fecha_prestamo')
    return render(request, 'historial.html', {'prestamos': prestamos})

@login_required
def devolver_libro(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id, usuario=request.user)

    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.fecha_devolucion = timezone.now()
        prestamo.libro.stock += 1
        prestamo.libro.disponible = True
        prestamo.libro.save()
        prestamo.save()

    return redirect('historial_usuario')

@user_passes_test (lambda u: u.is_superuser) # Solo permite superusuarios
def exportar_json(request):
    data = serialize('json', Libro.objects.all()) + serialize('json', Prestamo.objects.all())
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="backup_biblioteca.json"'
    return response

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'stock']

@user_passes_test(lambda u: u.is_staff)
def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'nuevo_libro.html', {'form': form})
