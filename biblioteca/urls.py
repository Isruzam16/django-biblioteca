from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/prestar/', views.prestar_libro, name='prestar_libro'),

#Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('historial/', views.historial_usuario, name='historial_usuario'),

]

