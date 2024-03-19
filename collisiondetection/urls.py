# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from django.urls import path, include
from collisiondetection import views
from rest_framework.routers import DefaultRouter
# from collisiondetection.views import 

router = routers.DefaultRouter()

urlpatterns = [
    path("detect-time/",views.ObstacleDetectionEventViewSet.as_view()),
    path('detect-time/<int:id>/', views.ObstacleDetectionEventViewSet.as_view()),
    path('', include(router.urls)),
]

urlpatterns += router.urls