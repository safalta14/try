from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

app_name="weather"

urlpatterns= [
path("",views.weather,name="weather"),
path("calling/",views.calling,name="calling"),
path('cities/',views.list_cities,name='list_cities')
# path("",views.weathering,name="weathering"),

] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)