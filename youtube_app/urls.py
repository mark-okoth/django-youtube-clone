from django.urls import path
from . import views
from . views import postListView, postDetailView

urlpatterns = [
    path('', postListView.as_view(), name = 'home' ),
    path('post/<int:pk>/', postDetailView.as_view(), name="details"),
    path('about/', views.about, name = 'about' ),
    
    
]