from django.db import models

# Model for Comment

class Comment(models.Model):
    added_by = models.CharField(max_length=150, help_text="User")
    comment = models.TextField(help_text="Comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.comment

# Model for Reply

class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    added_by = models.CharField(max_length=150, help_text="User")
    reply = models.TextField(help_text="Reply")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.reply
