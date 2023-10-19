from django.db import models
from django.utils import timezone

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)  # Unique email address for each subscription
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Date and time when the subscription was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the subscription was last updated

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    include_user_email = models.BooleanField(default=False)

    def __str__(self):
        return self.name