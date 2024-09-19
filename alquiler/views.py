from .models import alquiler, videojuego , genero, plataforma
from .forms import alquilerForm , videojuegosForm
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404


def registrar_alquiler(request):
    alquileres = alquiler.objects.all()
    if request.method == 'POST':
        form = alquilerForm(request.POST)
        if form.is_valid():
            alqui = form.save(commit=False)
            videojuego = alqui.videojuego  
            
            if videojuego.stock > 0:
                videojuego.stock -= 1  
                videojuego.save()  
                
                alqui.save() 
                return redirect('registrar_alquiler')  
            else:
                form.add_error('videojuego', 'No hay stock disponible para este videojuego.')
    else:
        form = alquilerForm()

    return render(request, 'registrar_alquiler.html', {'form': form,'alquileres':alquileres})


def listar_videojuegos(request):
    videojuegos = videojuego.objects.all()

    return render(request, 'listar_videojuegos.html', {'videojuegos': videojuegos})

def finalizar_alquiler(request, id):
    alqui = get_object_or_404(alquiler, id=id)
    video = alqui.videojuego  
    
    video.stock += 1
    video.save()

    alqui.delete() 
    
    return redirect('registrar_alquiler') 

def list_genero(request):
    generos = genero.objects.all()
    return render(request, 'list_genero.html', {'generos': generos})

def list_plataforma(request):
    plataformas = plataforma.objects.all()
    return render(request, 'list_plataforma.html', {'plataformas': plataformas})

def añadir_videojuego(request):
    if request.method == 'POST':
        form = videojuegosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_videojuegos')
    else:
        form = videojuegosForm()
    return render(request, 'añadir_videojuego.html', {'form': form})

def videojuegos_genero(request, id):
    genero_instance = get_object_or_404(genero, id=id)
    videojuegos = videojuego.objects.filter(genero=genero_instance)  
    genero_nombre = genero_instance.nombre
    return render(request, 'videojuegos_genero.html', {'videojuegos': videojuegos, 'genero': genero_nombre})




def videojuegos_plataforma(request,id):
    Plataforma = get_object_or_404(plataforma, id=id)
    videojuegos = videojuego.objects.filter(plataforma=Plataforma)
    Plataforma=Plataforma.nombre
    return render(request, 'videojuegos_plataforma.html', {'videojuegos': videojuegos, 'Plataforma': Plataforma})