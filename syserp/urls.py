from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from core.views import index


urlpatterns = [
    path('', index, name='index'),

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('api/', include('api.urls')),
    path('core/', include('core.urls')),
    path('crm/', include('crm.urls')),
    #path('frm/', include('frm.urls')),
    #path('hrm/', include('hrm.urls')),
    #path('mrp/', include('mrp.urls')),
    #path('scm/', include('scm.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
