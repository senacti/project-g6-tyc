from django.db import models
from users.models import User
import json

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    line3 = models.CharField(max_length=200, blank=True)

    DEPARTMENT_CHOICES = (
        ('', 'Seleccionar departamento'),  
        ('amazonas', 'Amazonas'),
        ('antioquia', 'Antioquia'),
        ('arauca', 'Arauca'),
        ('atlantico', 'Atlantico'),
        ('bolivar', 'Bolivar'),
        ('bogota D.C', 'Bogota D.C'),
        ('boyaca', 'Boyaca'),
        ('caldas', 'Caldas'),
        ('caqueta', 'Caqueta'),
        ('casanare', 'Casanare'),
        ('cauca', 'Cauca'),
        ('cesar', 'Cesar'),
        ('choco', 'Choco'),
        ('cordoba', 'Cordoba'),
        ('cundinamarca', 'Cundinamarca'),
        ('guainia', 'Guainia'),
        ('guaviare', 'Guaviare'),
        ('huila', 'Huila'),
        ('la guajira', 'La Guajira'),
        ('magdalena', 'Magdalena'),
        ('meta', 'Meta'),
        ('narino', 'Narino'),
        ('norte de santander', 'Norte de Santander'),
        ('putumayo', 'Putumayo'),
        ('quindio', 'Quindio'),
        ('risaralda', 'Risaralda'),
        ('san_andres', 'San Andres y Providencia'),
        ('santander', 'Santander'),
        ('sucre', 'Sucre'),
        ('tolima', 'Tolima'),
        ('valle del cauca', 'Valle del Cauca'),
        ('vaupes', 'Vaupes'),
        ('vichada', 'Vichada')
    )

    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)

        
    street_type = models.CharField(max_length=50, choices=(
        ('avenida', 'Avenida'),
        ('avenida_calle', 'Avenida Calle'),
        ('avenida_carrera', 'Avenida Carrera'),
        ('calle', 'Calle'),
        ('carrera', 'Carrera'),
        ('circular', 'Circular'),
        ('circunvalar', 'Circunvalar'),
        ('diagonal', 'Diagonal'),
        ('manzana', 'Manzana'),
        ('transversal', 'Transversal'),
        ('via', 'Vía'),
    ))
    reference = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=10, null=False, blank=False)
    is_home_or_work = models.CharField(max_length=20, choices=(
        ('home', 'Casa'),
        ('work', 'Trabajo'),
    ))
    contact_phone = models.CharField(max_length=20)

    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        address = "{} - {} - {}"
        return address.format(self.postal_code, self.line1, self.line2, self.line3)
    
    def has_orders(self):
        return self.order_set.count() >= 1

    def update_default(self, default=False):
        self.default = default
        self.save()
    
    @staticmethod
    def get_municipios(departamento):
        with open('direccion/data/colombia.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                if entry['departamento'].lower() == departamento.lower():
                    return entry['ciudades']
        return []
            

    @property
    def address(self):
        return f'{self.line1} {self.line2}, {self.line3}'
    
    @property
    def address_countrydetail(self):
        return f'Departamento: {self.get_department_display()}'
    
    @property
    def address_mundetail(self):
        municipios = self.get_municipios(self.department)
        municipio = municipios[0] if municipios else 'Sin municipio'
        return f'Municipio: {municipio}'
