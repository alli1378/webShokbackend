"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path,include,re_path
from account.views import Login,Register,activate
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('',include('django.contrib.auth.urls')),
    path('cart/',include('cart.urls')),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',activate, name='activate'),
    path('account/',include('account.urls')),
    path('comment/',include('comment.urls')),
    path('cart/',include('cart.urls'),name='cart'),
    path('product/',include('Product.urls')),
    # rest_url
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token-auth/', obtain_auth_token),
    # jwt
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # rest auth
    # path('api/rest-auth/', include('dj_rest_auth.urls')),
    # path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # jwt djoser
    path('api/auth/', include('djoser.urls')),
    # path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),

    # api
    path('api/',include('Product_api.urls')),
    path('api/articles/',include('blog_api.urls')),
    path('api/dashbord/',include('account_api.urls')),

]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
