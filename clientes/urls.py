from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cliente_list, name ='cliente_list'),
    url(r'^clienten/$', views.cliente_nuevo, name='cliente_nuevo'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detalle, name='cliente_detalle'),
    url(r'^cliente/(?P<pk>[0-9]+)/editar/$', views.cliente_editar, name='cliente_editar'),
    url(r'^cliente/(?P<pk>\d+)/remover/$', views.cliente_remove, name='cliente_remove'),
    url(r'^menun/$', views.menu_nuevo, name='menu_nuevo'),
    url(r'^menu/$', views.menu_list, name='menu_list'),
    url(r'^menu/(?P<pk>\d+)/remover/$', views.menu_remove, name='menu_remove'),
    url(r'^menu/(?P<pk>[0-9]+)/editar/$', views.menu_editar, name='menu_editar'),
    url(r'^menu/(?P<pk>[0-9]+)/$', views.menu_detalle, name='menu_detalle'),
    ]
