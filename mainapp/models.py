from django.db import models

# Create your models here.
class Register(models.Model):
    fname = models.CharField("First Name", max_length=30)
    lname = models.CharField("Last Name", max_length=30)
    email = models.EmailField("Email", max_length=100,unique=True)
    phone = models.CharField("Phone Number", max_length=15, blank=True, null=True)
    preference = models.CharField("Yoga Preference", max_length=100, default="Not Specified")

    def __str__(self):
        return f"{self.fname}, {self.lname}, {self.email}, {self.phone}, {self.preference}"


class Teacher(models.Model):
    name = models.CharField("Teacher Name", max_length=100)
    photo = models.ImageField("Photo", upload_to='teachers_photos/')
    specialization = models.CharField("Yoga Specialization", max_length=100, default="General Yoga")

    def __str__(self):
        return self.name
    


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"Image {self.id}"


