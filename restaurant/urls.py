from . import views
from django.urls import path,include

from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'table',views.BookingViewSet)
urlpatterns = [
    path('',views.index,name="index"),
    path('menu/',views.MenuItemsView.as_view()),
    path('menu/<int:pk>/',views.SingleMenuItemsView.as_view()),
    path('booking/',include(router.urls)),
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),

]