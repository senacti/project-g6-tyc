from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect

#from django.contrib.auth.models import User
from users.models import User

from .forms import RegisterForm

from productos.models import Producto

from .decorators import empleado_required



def index(request):

    productos = Producto.objects.all().order_by('-id')

    return render(request,'index.html', {
        'message': 'Listado de productos',
        'title': 'Productos',
        'productos': productos
    } )

def login_view(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Empleado').exists():
            print("El usuario pertenece al grupo 'Empleado'")
            return redirect('menu_empleados')
        elif request.user.groups.filter(name='Admin').exists():
            print("El usuario es Admin")
            return redirect('/admin')
        else:
            print("El usuario NO pertenece al grupo 'Empleado'")
            return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            if user.groups.filter(name='Empleado').exists():
                return redirect('menu_empleados')
            elif user.groups.filter(name='Admin').exists():
                
                return redirect('/admin')
            else:
                return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no válidos')

    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request,'users/register.html', {
        'form': form
    })

#Web cerrada


@empleado_required
def menu_principalEmpleados(request):
    return render(request, 'web_cerrada/menu_principalEmpleados.html',{

    })

@empleado_required
def productosE(request):
    return render(request, 'web_cerrada/productosE.html',{

    })

@empleado_required
def categoriasE(request):
    return render(request, 'web_cerrada/categoriasE.html',{

    })

@empleado_required
def promocionalE(request):
    return render(request, 'web_cerrada/promocionalE.html',{

    })