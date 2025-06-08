
from django.urls import path
from.import views 
from django.conf import settings
from django.conf.urls.static import static

#localhost:8000/chai

app_name='chai'
urlpatterns =[
    path('',views.all_chai,name='all_chai'),
    path('place-order/',views.linking,name='order'),
    # path('login/',views.login_views,name='login-views'),
    #   path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
