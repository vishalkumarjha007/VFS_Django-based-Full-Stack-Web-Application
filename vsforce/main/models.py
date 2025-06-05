from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    training = models.TextField()
    image = models.ImageField(upload_to='staff/', blank=True, null=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


