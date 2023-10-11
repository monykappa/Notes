
from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.note:
            return f"Deleted Note: {self.note.title} ({self.deleted_at})"
        else:
            return f"Deleted Note (no associated note) ({self.deleted_at})"


