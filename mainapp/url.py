from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register),
    path('api/showall/',views.showall),
    path('api/single/<int:pk>',views.single),
    path('api/teachers/', views.get_teachers),
    path('api/gallery/', views.get_galleryimages),
    path('create_superuser/',views.create_superuser)
]