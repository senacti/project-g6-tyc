from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from core.forms import CustomUserCreationForm

#WEB CERRADA 

    #ADMIN

def Menu_PrincipalAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Menu_Principal/Menu_PrincipalAdmin.html',{

    })

        #PERSONAL

def PersonalAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Personal/PersonalAdmin.html',{
        
    })

def Administrar_Personal(request):
    return render(request,'Web_Cerrada/Administrador/Personal/Administrar_Personal.html',{
        
    })

        #INVENTARIO

def InventarioAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Inventario/InventarioAdmin.html',{
        
    })

        #CAJA

def CajaAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Caja/CajaAdmin.html',{
        
    })

        #PROVEEDORES

def ProveedoresAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Proveedores/ProveedoresAdmin.html',{
        
    })

        #SOCIAL

def ModulosIndexAdmin(request):
    return render(request,'Web_Cerrada/Administrador/Social/ModulosIndexAdmin.html',{
        
    })

    #EMPLEADO

def Menu_Principal(request):
    return render(request,'Web_Cerrada/Empleado/Menu_Principal/Menu_Principal.html',{

    })

        #PERSONAL

def PersonalEmpleado(request):
    return render(request,'Web_Cerrada/Empleado/Personal/PersonalEmpleado.html',{
        
    })

def Consultar_Personal(request):
    return render(request,'Web_Cerrada/Empleado/Personal/Consultar_Personal.html',{
        
    })

        #INVENTARIO

def Inventario(request):
    return render(request,'Web_Cerrada/Empleado/Inventario/Inventario.html',{

    })

def Modificar_Inventario(request):
    return render(request,'Web_Cerrada/Empleado/Inventario/Modificar_Inventario.html',{

    })

        #CAJA

def Caja(request):
    return render(request,'Web_Cerrada/Empleado/Caja/Caja.html',{
        
    })

def Factura(request):
    return render(request,'Web_Cerrada/Empleado/Caja/Factura.html',{
        
    })

        #PROVEEDORES

def Proveedores(request):
    return render(request,'Web_Cerrada/Empleado/Proveedores/Proveedores.html',{
        
    })

def Modificar_Proveedores(request):
    return render(request,'Web_Cerrada/Empleado/Proveedores/Modificar_Proveedores.html',{
        
    })

def Devolucion_Proveedores(request):
    return render(request,'Web_Cerrada/Empleado/Proveedores/Devolucion_Proveedores.html',{
        
    })


        #SOCIAL

def ModulosIndex(request):
    return render(request,'Web_Cerrada/Empleado/Social/ModulosIndex.html',{
        
    })

def Ayuda(request):
    return render(request,'Web_Cerrada/Empleado/Social/Ayuda.html',{

    })


#################################################################################################




#WEB ABIERTA

def MarketplaceIndex(request):
    return render(request,'Web_Abierta/App/MarketplaceIndex.html',{
        
    })


# --------------------------------------------------- #


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario =CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('Menu_Principal')
        data['form'] = formulario


    return render(request, 'Web_Cerrada/Administrador/Personal/registro.html', data)

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
    return render(request, 'Web_Cerrada/Sesiones/Login.html',{

    })

def logout(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('Login')



#Login Clientes

def LoginClientes(request):
    return render(request,'Web_Abierta/Sesiones/LoginClientes.html',{
        
    })