import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MagicLinkToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def is_valid(self):
        # token expires after 15 minutes
        expiry = self.created_at + timezone.timedelta(minutes=15)
        return not self.used and timezone.now() < expiry
