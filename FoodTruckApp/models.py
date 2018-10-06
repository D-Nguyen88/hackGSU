from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.PositiveIntegerField( default = 0)
    image = models.ImageField(upload_to='profile_image', default = 'profile_image/img_avatar2.png')

    def __str__(self):
        return '{}'.format(self.user.username)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)