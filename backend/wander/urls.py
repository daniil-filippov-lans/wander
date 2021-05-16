from django.urls import path, include
from django.conf import settings as _settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet, basename='City')
router.register(r'place', views.PlaceViewSet, basename='Place')
router.register(r'attraction', views.AttractionViewSet, basename='Attraction')
router.register(r'poster', views.PosterEventViewSet, basename='PosterEvent')
router.register(r'restaurant', views.RestaurantViewSet, basename='Restaurant')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
