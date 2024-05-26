from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar-empresa', views.add_company, name='add_company'),
    path('editar-empresa/<int:company_id>', views.edit_company, name='edit_company'),
    path('api/adicionar-empresa', views.add_company_action, name='add_company_action'),
    path('api/adicionar-contato', views.add_contact_action, name='add_contact_action'),
    path('api/editar-empresa', views.edit_company_action, name='edit_company_action'),
    path('api/editar-contato', views.edit_contact_action, name='edit_contact_action'),
    path('api/deletar-empresa', views.delete_company_action, name='delete_company_action'),
    path('api/deletar-contato', views.delete_contact_action, name='delete_contact_action'),
]
