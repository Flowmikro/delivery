"""service URL Configuration

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
from django.contrib import admin
from django.urls import path

from cargo.views import CargoAPIList, CargoAPIDetail, CargoAPIUpdate
from truck.views import TruckAPIList, TruckAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cargo/', CargoAPIList.as_view()),  # Получение информации о грузах и создание груза
    path('api/cargo/<int:pk>/', CargoAPIDetail.as_view()),  # Список грузов и количество ближайших машин до груза
    path('api/cargo/update/<int:pk>/', CargoAPIUpdate.as_view()),  # Редактирование и удаление груза по ID

    path('api/truck/', TruckAPIList.as_view()),  # Список машин и их создание
    path('api/truck/<int:pk>/', TruckAPIUpdate.as_view()),  # Редактирование машины по ID
]
