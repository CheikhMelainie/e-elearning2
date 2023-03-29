from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import os

def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    photo_profile = models.ImageField(upload_to=renommer_image, blank=True)

    etudiant = 'etudiant'
    enseignant  = 'enseignant'
    parant = 'parant'

    type_user = [
        (etudiant, 'etudiant'), (enseignant, 'enseignant'), (parant, 'parant')
    ]

    type_profile = models.CharField(max_length=100, choices=type_user, default=etudiant)

    def __str__(self) :
        return self.user.username
    
    #cHERCHERUR20202