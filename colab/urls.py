from django.urls import path
from colab.views import (
    SubjectList,
    SubjectDetail,
    ProjectList,
    ProjectDetail,
    TaskList,
    TaskDetail,
    ResourceList,
    ResourceDetail,
    DiscussionList,
    DiscussionDetail,
    CommentList,
    CommentDetail,
)

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('resources/', ResourceList.as_view(), name='resource-list'),
    path('resources/<int:pk>/', ResourceDetail.as_view(), name='resource-detail'),
    path('discussions/', DiscussionList.as_view(), name='discussion-list'),
    path('discussions/<int:pk>/', DiscussionDetail.as_view(), name='discussion-detail'),
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
