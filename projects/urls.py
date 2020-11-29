from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('project/',views.project, name='projectForm'),
    path('search/', views.search_results, name='search'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.get_profile, name='userProfile'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.ProjectList.as_view()),
    path('project/<int:id>', views.get_project, name='single'),
]