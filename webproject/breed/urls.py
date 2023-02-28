from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='breed-home'),
    path('ads/', views.PostListView.as_view(), name='breed-ads'),
    path('ads/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('ads/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('ads/new/', views.PostCreateView.as_view(), name='post-create'),
    path('contact/', views.contact, name='breed-contact'),
    path('messaging/', views.messaging, name='breed-messaging'),
]
