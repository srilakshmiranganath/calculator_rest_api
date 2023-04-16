from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculator import views

from .views import calculate

'''router = DefaultRouter()
router.register(r"calculator", CalculatorView)

urlpatterns = [
    path("", include(router.urls))
]'''

urlpatterns = [
    path('', views.calculate, name='calculate'),
]