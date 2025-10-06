from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Count, Sum
from django.http import JsonResponse
from .models import Reto, Categoria, IntentoReto, PerfilUsuario, Alternativa
from .forms import RetoForm

def home(request):
    categorias = Categoria.objects.all()
    retos_destacados = Reto.objects.filter(activo=True).order_by('-fecha_creacion')[:6]
    
    ranking = PerfilUsuario.objects.order_by('-puntos_totales')[:10]
    
    context = {
        'categorias': categorias,
        'retos_destacados': retos_destacados,
        'ranking': ranking,
    }
    return render(request, 'retos/home.html', context)

def lista_retos(request):
    categoria_id = request.GET.get('categoria')
    dificultad = request.GET.get('dificultad')
    
    retos = Reto.objects.filter(activo=True)
    
    if categoria_id:
        retos = retos.filter(categoria_id=categoria_id)
    
    if dificultad:
        retos = retos.filter(dificultad=dificultad)
    
    categorias = Categoria.objects.all()
    
    context = {
        'retos': retos,
        'categorias': categorias,
    }
    return render(request, 'retos/lista_retos.html', context)

@login_required
def detalle_reto(request, reto_id):
    reto = get_object_or_404(Reto, id=reto_id, activo=True)
    
    intento_previo = IntentoReto.objects.filter(usuario=request.user, reto=reto).first()
    
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        es_correcto = False
        if reto.tipo in ['M', 'L', 'P']:  
            alternativa_seleccionada = Alternativa.objects.filter(id=respuesta, reto=reto).first()
            if alternativa_seleccionada and alternativa_seleccionada.es_correcta:
                es_correcto = True
        else: 
            if respuesta.lower() == reto.respuesta_correcta.lower():
                es_correcto = True
        
        if not intento_previo:
            IntentoReto.objects.create(
                usuario=request.user,
                reto=reto,
                respuesta=respuesta,
                es_correcto=es_correcto
            )
            
            if es_correcto:
                perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
                perfil.puntos_totales += reto.puntos
                perfil.retos_resueltos += 1
                perfil.save()
        
        return JsonResponse({'correcto': es_correcto})
    
    context = {
        'reto': reto,
        'intento_previo': intento_previo,
    }
    return render(request, 'retos/detalle_reto.html', context)

def ranking(request):
    usuarios = PerfilUsuario.objects.order_by('-puntos_totales')
    context = {'usuarios': usuarios}
    return render(request, 'retos/ranking.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            PerfilUsuario.objects.create(usuario=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'retos/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'retos/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    

    return render(request, 'retos/login.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .esb_simple import ESBSimple

esb = ESBSimple()

@csrf_exempt
def api_retos_esb(request):
    if request.method == 'GET':
        retos = Reto.objects.filter(activo=True)
        datos_retos = list(retos.values('id', 'titulo', 'dificultad', 'puntos'))
        
        esb.log_operation("API_RETOS", "OBTENER_RETOS", f"{len(datos_retos)} retos obtenidos")
        
        return JsonResponse({'retos': datos_retos})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
