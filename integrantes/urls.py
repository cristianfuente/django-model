from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name="home"),
    path('integrantes/',views.integrantes,name="integrantes"),
    path('integrantes/registro/',views.registro,name="registro"),
    path('integrantes/success/',views.success,name="success"),
    path('integrantes/prueba/',views.prueba,name="prueba"),

]
urlpatterns += staticfiles_urlpatterns()
