from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("registro",views.registro,name="registro"),
    path('catalogo/', views.catalogo, name='catalogo'),
    path("crud", views.crud, name="crud"),
    path("carrito", views.carrito, name="carrito"),
    path('agregar_al_carrito/<int:tour_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('restar_del_carrito/<int:item_id>/', views.restar_del_carrito, name='restar_del_carrito'),

    path("user_add", views.user_add, name="user_add"),
    path("user_del/<str:pk>", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("user_update", views.user_update, name="user_update"),
    path("crud_genero", views.crud_genero, name="crud_genero"),
    path("genero_add", views.genero_add, name="genero_add"),
    path("genero_del/<str:pk>", views.genero_del, name="genero_del"),
    path("genero_edit/<str:pk>", views.genero_edit, name="genero_edit"),
    path("crud_tour", views.crud_tour, name="crud_tour"),
    path("iniciousuario", views.iniciousuario, name="iniciousuario"),
    path("tour_add", views.tour_add, name="tour_add"),
    path("tour_del/<str:pk>", views.tour_del, name="tour_del"),
    path("tour_edit/<str:pk>", views.tour_edit, name="tour_edit"),
    path("login", views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
