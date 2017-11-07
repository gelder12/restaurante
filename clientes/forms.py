from django import forms
from .models import Cliente, Menu

class ClienteForm(forms.ModelForm):
#todos los campos de Cliente
   class Meta:
      model = Cliente
      fields = ('nombre', 'fecha_orden', 'edad', 'direccion', 'nit', 'clientes')
def __init__ (self, *args, **kwargs):
     super(ClienteForm, self).__init__(*args, **kwargs)
     self.fields["clientes"].widget = forms.widgets.CheckboxSelectMultiple()
     self.fields["clientes"].help_text = "Ingrese los Menus que se ordeno"
     self.fields["clientes"].queryset = Menu.objects.all()

class MenuForm(forms.ModelForm):
#todos los campos de Cliente
   class Meta:
      model = Menu
      fields = ('nombre', 'tipoproducto', 'descripcion', 'precio')
