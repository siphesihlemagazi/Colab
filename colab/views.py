from rest_framework import generics
from colab.models import Subject, Project, Task, Resource, Discussion, Comment
from colab.serializers import (
    SubjectSerializer,
    ProjectSerializer,
    TaskSerializer,
    ResourceSerializer,
    DiscussionSerializer,
    CommentSerializer,
)


class SubjectList(generics.ListCreateAPIView):
    """
    API endpoint that allows subjects to be viewed or created.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a subject to be viewed, updated, or deleted.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ProjectList(generics.ListCreateAPIView):
    """
    API endpoint that allows projects to be viewed or created.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a project to be viewed, updated, or deleted.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskList(generics.ListCreateAPIView):
    """
    API endpoint that allows tasks to be viewed or created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a task to be viewed, updated, or deleted.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ResourceList(generics.ListCreateAPIView):
    """
    API endpoint that allows resources to be viewed or created.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a resource to be viewed, updated, or deleted.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class DiscussionList(generics.ListCreateAPIView):
    """
    API endpoint that allows discussions to be viewed or created.
    """
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a discussion to be viewed, updated, or deleted.
    """
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class CommentList(generics.ListCreateAPIView):
    """
    API endpoint that allows comments to be viewed or created.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a comment to be viewed, updated, or deleted.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
