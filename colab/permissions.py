from rest_framework import permissions


class IsSubjectStaffOrInstructor(permissions.BasePermission):
    """
    Custom permission to only allow staff users or instructors of the subject to delete or update a subject.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a staff member
        if request.user.is_staff:
            return True

        # Check if the user is an instructor of the subject
        if obj.instructors.filter(id=request.user.id).exists():
            return True

        return False


class IsProjectInstructorOrCreator(permissions.BasePermission):
    """
    Custom permission to only allow project subject instructors, and the creator of the project to update a project.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        project = obj

        # Check if user is an instructor of the project's subject
        # TODO: take a close look at this:
        subject = project.subject
        if subject and subject.instructors.filter(id=user.id).exists():
            return True

        # Check if user is the creator of the project
        if obj.created_by == request.user:
            return True

        return False


class IsTaskCreatorOrProjectMemberOrStaff(permissions.BasePermission):
    """
    Custom permission to only allow project members or creators or staff members to update a task.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a member of the project
        if obj.project and obj.project.members.filter(id=request.user.id).exists():
            return True

        # Check if the user is the creator of the project
        if obj.project and obj.project.created_by_id == request.user.id:
            return True

        # Check if user is staff
        if request.user.is_staff:
            return True

        return False


class IsResourceCreatorOrProjectMemberOrStaff(IsTaskCreatorOrProjectMemberOrStaff):
    """
    Custom permission to only allow project members or creators or staff members to update a resource.
    """


class IsDiscussionCreatorOrProjectMemberOrStaff(IsTaskCreatorOrProjectMemberOrStaff):
    """
    Custom permission to only allow project members or creators or staff members to update a discussion.
    """


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff users to create or update.
    Normal users can only view.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
