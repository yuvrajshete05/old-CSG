
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # For automatic profile creation
from django.dispatch import receiver # For automatic profile creation

# Model for Career opportunities/listings
class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Model for Skills
class Skill(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return self.name

# Model for Courses
class Course(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()

    def __str__(self):
        return self.name

# Model for Contact messages (from a contact form)
# Note: You had two similar Contact models, I'm keeping one and ensuring it's robust.
# app1/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

# Model for user login details (Though generally not needed if using Django's Auth User)
# If you are using Django's built-in authentication, you typically don't need a separate Login model.
# This model is provided as per your original input, but consider if it's truly necessary.
class Login(models.Model):
    username = models.CharField(max_length=50, unique=True) # Username should likely be unique
    password = models.CharField(max_length=128) # Store hashed passwords, not plain text!

    def __str__(self):
        return self.username

# app1/models.py (ResumeInput - assuming this is in app1 as per your comment)
class ResumeInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)

    summary = models.TextField(help_text="A brief professional summary or objective.")

    # Education fields
    education_level = models.CharField(max_length=100, blank=True, null=True)
    university_name = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    education_details = models.TextField(blank=True, null=True, help_text="List other educational achievements, courses, or certifications.")

    # Experience fields
    job_title = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current job.")
    experience_details = models.TextField(blank=True, null=  True, help_text="Describe your responsibilities and achievements in this role (use bullet points if possible).")
    previous_experience = models.TextField(blank=True, null=True, help_text="Add details for previous jobs if any.")

    # Skills fields (store as comma-separated string, or consider a ManyToManyField for complex apps)
    skills = models.TextField(help_text="Comma-separated list of your skills (e.g., Python, JavaScript, Django, Data Analysis).")

    # Projects (optional)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_description = models.TextField(blank=True, null=True, help_text="Describe a key project and your role.")
    project_url = models.URLField(blank=True, null=True)

    # Generated content
    generated_resume = models.TextField(blank=True, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume for {self.full_name}"


# ************************************************************
# NEW: Profile Model for User Avatars
# ************************************************************
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_avatars/') # Ensure default_avatar.png exists in your media root

    def __str__(self):
        return f'{self.user.username} Profile'

# ************************************************************
# NEW: Signals to auto-create and save Profile for each User
# ************************************************************
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a Profile instance automatically
    when a new User instance is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the Profile instance automatically
    when a User instance is saved.
    """
    instance.profile.save()