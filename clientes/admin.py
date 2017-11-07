from django.contrib import admin
from clientes.models import Menu, MenuAdmin, Cliente, ClienteAdmin

admin.site.register(Menu, MenuAdmin)
admin.site.register(Cliente, ClienteAdmin)
