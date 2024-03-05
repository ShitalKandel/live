from django.urls import path
from liveStream import views


urlpatterns = [
    path('artist/', views.ArtistView.as_view(),name="artist"),
    path('file/',views.FileView.as_view(),name='file'),
    path('file/<int:audio_id>/',views.FileView.as_view(),name='file_detail')
]

