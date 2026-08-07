from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Group(models.Model):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    FREQUENCY_CHOICES = (
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
    )

    PRIVATE = "private"
    PUBLIC = "public"

    VISIBILITY_CHOICES = (
        (PRIVATE, "Private"),
        (PUBLIC, "Public"),
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    group_image = models.ImageField(upload_to="group_images/",blank=True,null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="created_groups")
    contribution_amount = models.DecimalField(max_digits=12,decimal_places=2)
    contribution_frequency = models.CharField(max_length=20,choices=FREQUENCY_CHOICES)
    visibility = models.CharField(max_length=20,choices=VISIBILITY_CHOICES,default=PRIVATE)
    max_members = models.PositiveIntegerField(default=20)
    is_private = models.BooleanField(default=True)
    penalty_rules = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,through="GroupMember",related_name="joined_groups")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.name
    
class GroupMember(models.Model):
    CREATOR = "creator"
    MEMBER = "member"

    ROLE_CHOICES = (
        (CREATOR, "Creator"),
        (MEMBER, "Member"),
    )

    PENDING = "pending"
    ACTIVE = "active"
    LEFT = "left"
    REMOVED = "removed"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (ACTIVE, "Active"),
        (LEFT, "Left"),
        (REMOVED, "Removed"),
    )

    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="group_members")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="memberships")
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default=MEMBER)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("group", "user")

    def __str__(self):
        return f"{self.user} - {self.group}"
    


class GroupInvitation(models.Model):
    
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (DECLINED, "Declined"),
        (EXPIRED, "Expired"),
    )

    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="invitations")
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="sent_group_invites")
    invited_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="received_group_invites")
    invitation_code = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.invited_user} invited to {self.group}"
    
    


class JoinRequest(models.Model):
    
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    )

    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="join_requests")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="join_requests")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    requested_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("group", "user")

    def __str__(self):
        return f"{self.user} -> {self.group}"
    
    

class GroupAnnouncement(models.Model):
    
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="announcements")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title