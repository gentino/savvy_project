from django.db import models
from django.conf import settings
from groups.models import Group


# Create your models here.
class Notification(models.Model):
    WIDTHRAWAL = "widthrawal"
    DEPOSIT = "deposit"
    REQUEST = "request"
    OTHERS = "others"

    notification_type = (
        (WIDTHRAWAL, "widthrawal"),
        (DEPOSIT, "deposit"),
        (REQUEST, "request"),
        (OTHERS, "others")
    )
    
 

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=15,choices=notification_type)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description    
