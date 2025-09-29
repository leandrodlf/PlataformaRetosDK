from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retos/', views.lista_retos, name='lista_retos'),
    path('reto/<int:reto_id>/', views.detalle_reto, name='detalle_reto'),
    path('ranking/', views.ranking, name='ranking'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),
]