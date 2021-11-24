from django.urls import path
from . import views

urlpatterns = [
    path('' , views.indexx , name='index'),
    path('boutique' , views.boutique , name='boutique'),
    path('amour' , views.amour , name='amour'),
    path('anniversaire' , views.anniversaire , name='anniversaire'),
    path('naissance' , views.naissance , name='naissance'),
    path('remerciement' , views.remerciement , name='remerciement'),
    path('product/<int:id_test>' , views.product , name='product'),
    path('cart' , views.cart , name="cart"),
    path('about-us', views.about , name='about-us'),
    path('contact-us', views.Contact_Us , name='contact_us'),
]
