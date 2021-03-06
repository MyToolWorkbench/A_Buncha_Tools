"""A_Buncha_Tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from myToolWorkbench import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('myToolWorkbench/home/',views.DashboardView.as_view(), name='dashboard'),
    path('myToolWorkbench/inventory/', views.InventoryView.as_view(), name='inventory'),
    path('myToolWorkbench/sale/', TemplateView.as_view(template_name='sale.html'), name='sale'),
    path('myToolWorkbench/people/', views.BusinessView.as_view(), name='people'),
    path('admin/', admin.site.urls),
    path('myToolWorkbench/', include('django.contrib.auth.urls')),
    path('myToolWorkbench/register/', views.register, name='register'),
    path('myToolWorkbench/add-business/', views.create_business, name='add-business'),
    path('myToolWorkbench/<int:pk>/',views.BusinessDetailView.as_view(), name='business-details'),
    path('myToolWorkbench/add-customer/', views.create_customer, name='add-customer'),
    path('myToolWorkbench/add-inventory/', views.add_inventory, name='add-inventory'),
    # path('myToolWorkbench/register/', TemplateView.as_view(template_name="registration/register.html"), name='register'),
]
