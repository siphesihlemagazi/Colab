from colab import permissions
from colab import serializers
from colab.models import Subject, Project, Task, Resource, Discussion, Comment
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied, ValidationError


class SubjectList(generics.ListCreateAPIView):
    """
    API endpoint that allows subjects to be viewed or created.
    """
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsStaffOrReadOnly]


class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a subject to be viewed, updated, or deleted.
    """
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsSubjectStaffOrInstructor]


class ProjectList(generics.ListCreateAPIView):
    """
    API endpoint that allows projects to be viewed or created.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a project to be viewed, updated, or deleted.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsProjectStuffOrInstructorOrCreator]


class TaskList(generics.ListCreateAPIView):
    """
    API endpoint that allows tasks to be viewed or created.
    """
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsTaskCreatorOrProjectMemberOrStaff]

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


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a task to be viewed, updated, or deleted.
    """
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsTaskCreatorOrProjectMemberOrStaff]


class ResourceList(generics.ListCreateAPIView):
    """
    API endpoint that allows resources to be viewed or created.
    """
    queryset = Resource.objects.all()
    serializer_class = serializers.ResourceSerializer

    def create(self, request, *args, **kwargs):
        # Check if user has permission to create a new resource for a project

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
                raise PermissionDenied('You do not have permission to create a resource without specifying a project ID')

        return super().create(request, *args, **kwargs)


class ResourceDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a resource to be viewed, updated, or deleted.
    """
    queryset = Resource.objects.all()
    serializer_class = serializers.ResourceSerializer
    permission_classes = [permissions.IsResourceCreatorOrProjectMemberOrStaff]


class DiscussionList(generics.ListCreateAPIView):
    """
    API endpoint that allows discussions to be viewed or created.
    """
    queryset = Discussion.objects.all()
    serializer_class = serializers.DiscussionSerializer

    def create(self, request, *args, **kwargs):
        # Check if user has permission to create a new discussion for a project

        project_id = request.data.get('project')
        if project_id is not None:
            try:
                project = Project.objects.get(id=project_id)
                if request.user not in project.members.all() and not request.user.is_staff:
                    raise PermissionDenied('You do not have permission to create a discussion for this project')
            except Project.DoesNotExist:
                raise ValidationError('Invalid project ID')
        elif not request.user.is_staff:
            projects = Project.objects.filter(members=request.user)
            if not projects.exists():
                raise PermissionDenied('You do not have permission to create a discussion without specifying a project ID')

        return super().create(request, *args, **kwargs)


class DiscussionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a discussion to be viewed, updated, or deleted.
    """
    queryset = Discussion.objects.all()
    serializer_class = serializers.DiscussionSerializer
    pagination_class = [permissions.IsDiscussionCreatorOrProjectMemberOrStaff]


class CommentList(generics.ListCreateAPIView):
    """
    API endpoint that allows comments to be viewed or created.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a comment to be viewed, updated, or deleted.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
