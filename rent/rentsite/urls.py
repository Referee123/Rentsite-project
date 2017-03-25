from django.conf.urls import url
from rentsite import views as rentsite_views

urlpatterns = [
    url(r'^rentsite/$', rentsite_views.rentsites)
]