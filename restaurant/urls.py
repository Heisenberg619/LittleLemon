from . import views
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'table',views.BookingViewSet)
urlpatterns = [
    path('',views.index,name="index"),
    path('menu-items/',views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/',views.SingleMenuItemsView.as_view()),
    path('booking/',include(router.urls)),
    path('',include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),


]