from django.urls import path
from .views import LaboratorioListView, LaboratorioDetailView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), #pagina de inicio
    path('lista/', LaboratorioListView.as_view(), name='laboratorio_list'),  # Listado de laboratorios
    path('detail/<int:pk>/', LaboratorioDetailView.as_view(), name='laboratorio_detail'),  # Detalles de un laboratorio
    path('create/', LaboratorioCreateView.as_view(), name='laboratorio_create'),  # Crear laboratorio
    path('update/<int:pk>/', LaboratorioUpdateView.as_view(), name='laboratorio_update'),  # Actualizar laboratorio
    path('delete/<int:pk>/', LaboratorioDeleteView.as_view(), name='laboratorio_delete'),  # Eliminar laboratorio
]
