from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 1. โปรไฟล์ผู้ใช้
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    personality_type = models.CharField(max_length=50, blank=True, null=True)  # เช่น "นักผจญภัยใจดี"
    saved_pets = models.ManyToManyField('Pet', blank=True)  # สัตว์ที่บันทึกไว้
    
    def __str__(self):
        return self.user.username

# 2. แบบทดสอบบุคลิกภาพ
class PersonalityTestResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personality_type = models.CharField(max_length=50)
    score = models.JSONField()  # เก็บผลลัพธ์แบบ JSON
    
    def __str__(self):
        return f"{self.user.username} - {self.personality_type}"

# 3. ข้อมูลสัตว์จรจัด
class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    breed = models.CharField(max_length=100, blank=True, null=True)
    energy_level = models.CharField(max_length=50, blank=True, null=True)
    friendliness = models.CharField(max_length=50, blank=True, null=True)
    trainability = models.CharField(max_length=50, blank=True, null=True)
    health_status = models.TextField(blank=True, null=True)
    compatibility_with_kids = models.BooleanField(default=True)
    compatibility_with_pets = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to="pet_images/", blank=True, null=True)  
    
    def __str__(self):
        return self.name

# 4. การรับเลี้ยงสัตว์
class Adoption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    application_status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending"
    )
    application_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.pet.name} ({self.application_status})"

# 5. การนัดหมายพบสัตว์
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", "Scheduled"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
        default="Scheduled"
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.pet.name} ({self.appointment_date})"

# 6. บล็อกและบทความ
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    
    def __str__(self):
        return self.title
