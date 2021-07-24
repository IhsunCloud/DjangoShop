from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('mysite.urls')),
    path('blog/', include('blog.urls')),
    path('cart', include('cart.urls')),
    path('checkout/', include('payment.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('registration/', include('accounts.urls')), 
    path('shop/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
