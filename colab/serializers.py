from accounts.models import User
from rest_framework import serializers
from colab.models import Subject, Project, Task, Resource, Discussion, Comment


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subject model.
    """

    instructors = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Subject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    """

    members = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Project
        fields = '__all__'

    def update(self, instance, validated_data):
        members_data = validated_data.pop('members', None)
        instance = super().update(instance, validated_data)
        if members_data is not None:
            instance.members.add(*members_data)
        # remove user from project members
        remove_member_ids = self.context['request'].data.get('remove_members', [])
        instance.members.remove(*remove_member_ids)

        return instance


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """

    assigned_to = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='id')
    completed_by = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='id', allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        # Checks if user being assigned task is member of the project.
        project = instance.project
        assigned_to_user_id = self.context['request'].data.get('assigned_to')
        if assigned_to_user_id:
            if project.members.filter(id=assigned_to_user_id).exists():
                return super().update(instance, validated_data)
            raise serializers.ValidationError({"assigned_to": ["User is not a member of the project."]})
        return super().update(instance, validated_data)


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
    started_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Discussion
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    created_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Comment
        fields = '__all__'
