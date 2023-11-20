from dal import autocomplete
from .models import categoria

class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = categoria.objects.all()

        if self.q:
            qs = qs.filter(nombre_categoria__icontains=self.q)

        return qs