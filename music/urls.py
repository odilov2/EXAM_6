from django.urls import path, include
from .views import LandingPageAPIView, SongAPIViewSet, AlbomAPIViewSet, ArtistAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('songs', viewset=SongAPIViewSet)
router.register('alboms', viewset=AlbomAPIViewSet)
router.register('artists', viewset=ArtistAPIViewSet)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
