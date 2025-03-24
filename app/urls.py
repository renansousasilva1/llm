from django.contrib import admin
from django.urls import path
from llm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('processar_noticia', views.processar_noticia, name='processar_noticia'),
]
