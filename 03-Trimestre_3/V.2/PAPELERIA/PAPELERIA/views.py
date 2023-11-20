from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def Menu_Principal(request):
    return render(request,'Menu_Principal.html',{

    })

def Inventario(request):
    return render(request,'Inventario.html',{

    })

def Caja(request):
    return render(request,'Caja.html',{
        
    })

def Personal(request):
    return render(request,'Personal.html',{
        
    })

def Proveedores(request):
    return render(request,'Proveedores.html',{
        
    })

def ModulosIndex(request):
    return render(request,'ModulosIndex.html',{
        
    })




def Login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        user = authenticate(username=usuario, password=contrasena)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('Menu_Principal')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'Login.html',{

    })
def logout(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('Login')


def Ayuda(request):
    return render(request,'Ayuda.html',{

    })

def Modificar_Proveedores(request):
    return render(request,'Modificar_Proveedores.html',{
        
    })

def Devolucion_Proveedores(request):
    return render(request,'Devolucion_Proveedores.html',{
        
    })

def Administrar_Personal(request):
    return render(request,'Administrar_Personal.html',{
        
    })

def Consultar_Personal(request):
    return render(request,'Consultar_Personal.html',{
        
    })