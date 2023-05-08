from django.urls import path
from colab.views import (
    SubjectList,
    SubjectDetails,
    ProjectList,
    ProjectDetails,
    TaskList,
    TaskDetails,
    ResourceList,
    ResourceDetails,
    DiscussionList,
    DiscussionDetails,
    CommentList,
    CommentDetails,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetails.as_view(), name='subject-details'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetails.as_view(), name='project-details'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetails.as_view(), name='task-details'),
    path('resources/', ResourceList.as_view(), name='resource-list'),
    path('resources/<int:pk>/', ResourceDetails.as_view(), name='resource-details'),
    path('discussions/', DiscussionList.as_view(), name='discussion-list'),
    path('discussions/<int:pk>/', DiscussionDetails.as_view(), name='discussion-details'),
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetails.as_view(), name='comment-details'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
