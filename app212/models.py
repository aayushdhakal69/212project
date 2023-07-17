from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timeStap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message form " + self.name + "--" + self.email


class Blogupper(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=50, default="default_slug")
    mainimage = models.ImageField(upload_to="myapp/images", default="upload-image")
    location = models.CharField(max_length=30)
    datee = models.TextField()

    paragraphone = models.TextField()

    imgone = models.ImageField(upload_to="myapp/images", default="upload-image-one")
    imgtwo = models.ImageField(upload_to="myapp/images", default="upload-image-two")
    imgthree = models.ImageField(upload_to="myapp/images", default="upload-image-three")
    imgfour = models.ImageField(upload_to="myapp/images", default="upload-image-four")

    paragraphtwo = models.TextField()

    imgfive = models.ImageField(upload_to="myapp/images", default="upload-image-five")
    imgsix = models.ImageField(upload_to="myapp/images", default="upload-image-six")
    imgseven = models.ImageField(upload_to="myapp/images", default="upload-image-seven")
    imgeight = models.ImageField(upload_to="myapp/images", default="upload-image-eight")

    def __str__(self):
        return "Blog of " + self.location
