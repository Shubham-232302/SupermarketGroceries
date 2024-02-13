"""
URL configuration for GroceriesAtMarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
# from home.views import home, success
from home.views import addCategory, home, deleteCategory, addSubCategory, addItem, delSubCategory, delItem, displayData, updateCategory, UpdateSubCategory, updateItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addCategory', addCategory, name = 'addCategory'),
    path('deleteCategory', deleteCategory, name = 'delCategory'),
    path('addSubCategory', addSubCategory, name = 'subCategory'),
    path('addItem', addItem, name = 'addItem'),
    path('delSubCategory', delSubCategory, name = 'delSubCategory'),
    path('delItem', delItem, name = 'delItem'),
    path('displayData', displayData, name = 'displayData'),
    path('updateCategory', updateCategory, name = 'updateCategory'),
    path('updateSubCategory', UpdateSubCategory, name = 'UpdateSubCategory'),
    path('updateItem', updateItem, name = 'updateItem'),
]
