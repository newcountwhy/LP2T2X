"""eco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from checkout.views import *


urlpatterns = [
    path('payment_method/', payment_method_view, name='payment_method'),
    path('shopping_cart/', shopping_cart_view, name='shopping_cart'),
    path('checkout/', start_page_view, name='start_page'),
    path('logout', start_page_view, name='logout'),
    path('get_product/', get_product_view, name='get_product'),
    path('go_to_payment/', goto_payment_view, name='go_to_payment'),
    path('greeting/', finish_payment_view, name='finish_payment'),
]
