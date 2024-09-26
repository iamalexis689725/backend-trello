from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from trello.api import HomeViewSet, ListaViewSet, TareaViewSet
from trello.api.tablero_views import TableroViewSet
from . import views

router = DefaultRouter()
router.register(r'home', HomeViewSet, basename='home')
router.register(r'tableros', TableroViewSet, basename='tablero')
router.register(r'listas', ListaViewSet, basename='lista')
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = router.urls + [
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^profile$', views.profile, name='profile'),
]
