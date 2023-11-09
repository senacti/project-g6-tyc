from django.shortcuts import render

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
    return render(request,'Login.html',{

    })

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