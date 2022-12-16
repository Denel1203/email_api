from django.urls import include, path
from rest_framework import routers

from . import views

router=routers.DefaultRouter()
router.register('Usuario',views.Envio_ViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]