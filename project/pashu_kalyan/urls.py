
from django.urls import path
from pashu_kalyan import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/',views.uploadview.as_view(),name='upload'),
    path('',views.userData.as_view(),name='soja'),
    #for registration in cards
    path('registration-number/',views.Registration.as_view(),name='registration'), 
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
