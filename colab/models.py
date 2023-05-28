from django.db import models
from accounts.models import User


class Subject(models.Model):
    """
    Model representing a subject.
    """

    name = models.CharField(max_length=255, unique=True)
    instructors = models.ManyToManyField(User, related_name='subjects')

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Model representing a project that belongs to a subject and can have multiple members.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.title


class Task(models.Model):
    """
    Model representing a task that belongs to a project and is assigned to specific users.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('removed', 'Removed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='tasks_assigned')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed_by = models.ManyToManyField(User, related_name='tasks_completed', blank=True)
    due_date = models.DateTimeField()

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.title


class Resource(models.Model):
    """
    Model representing a resource that belongs to a project and can be a file.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resources/')

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.title


class Discussion(models.Model):
    """
    Model representing a discussion that belongs to a project and can have multiple comments.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    started_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model representing a comment that belongs to a discussion and is made by a specific user.
    """

    text = models.TextField()
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'colab'

    def __str__(self):
        return self.text
