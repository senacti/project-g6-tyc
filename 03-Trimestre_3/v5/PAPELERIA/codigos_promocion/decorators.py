from django.shortcuts import redirect

def empleado_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Empleado').exists():
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return wrapped_view