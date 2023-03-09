from django.urls import path
from .views import (MemberListAPI, 
                    MemberDetailAPI, 
                    ProjectListAPI, 
                    ProjectDetailAPI, 
                    MemberProjectAPI, 
                    ImageAPI,
                    ImageProjectRetrieveAPI)

urlpatterns = [
    path('members/list/', MemberListAPI.as_view(), name='member-list'),   
    path('members/<int:pk>/', MemberDetailAPI.as_view(), name='member-detail'),
    path('members/<int:member_id>/projects/', MemberProjectAPI.as_view(), name='member-projects'),
    path('projects/list/', ProjectListAPI.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPI.as_view(), name='project-detail'),
    path('images/list/', ImageAPI.as_view(), name='image-list'),
    path('images/<int:project_id>/', ImageProjectRetrieveAPI.as_view(), name='image-project'),
]
