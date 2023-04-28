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

from colab.permissions import IsSubjectStaffOrInstructor, IsProjectStuffOrInstructorOrCreator, IsTaskCreatorOrProjectMemberOrStaff
from rest_framework.exceptions import PermissionDenied, ValidationError


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
    permission_classes = [IsSubjectStaffOrInstructor]


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
    permission_classes = [IsProjectStuffOrInstructorOrCreator]


class TaskList(generics.ListCreateAPIView):
    """
    API endpoint that allows tasks to be viewed or created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskCreatorOrProjectMemberOrStaff]

    def create(self, request, *args, **kwargs):
        # Check if user has permission to create a new task for a project

        project_id = request.data.get('project')
        if project_id is not None:
            try:
                project = Project.objects.get(id=project_id)
                if request.user not in project.members.all() and not request.user.is_staff:
                    raise PermissionDenied('You do not have permission to create a task for this project')
            except Project.DoesNotExist:
                raise ValidationError('Invalid project ID')
        elif not request.user.is_staff:
            projects = Project.objects.filter(members=request.user)
            if not projects.exists():
                raise PermissionDenied('You do not have permission to create a task without specifying a project ID')

        return super().create(request, *args, **kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a task to be viewed, updated, or deleted.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskCreatorOrProjectMemberOrStaff]


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
