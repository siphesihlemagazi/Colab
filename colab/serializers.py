from django.contrib.auth.models import User
from rest_framework import serializers
from colab.models import Subject, Project, Task, Resource, Discussion, Comment


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subject model.
    """

    instructors = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Subject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    """

    members = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """

    assigned_to = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username')
    completed_by = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username', allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resource model.
    """

    class Meta:
        model = Resource
        fields = '__all__'


class DiscussionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Discussion model.
    """

    comments = serializers.StringRelatedField(many=True)
    started_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Discussion
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    created_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
