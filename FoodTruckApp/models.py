from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
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

weekdays = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
        (4, ("Thursday")),
        (5, ("Friday")),
        (6, ("Saturday")),
        (7, ("Sunday")),
    ]

class Truck(models.Model):
    truck_name = models.CharField(max_length = 50)
    truck_description = models.CharField(max_length = 150)
    truck_phone_number_regex = RegexValidator(regex=r'^\d{3}--\d{3}--\d{4})', message= "Phone number must be entered in the format: '+999-999-9999'.")
    truck_phone_number = models.CharField(validators=[truck_phone_number_regex], max_length = 15 )
    # match_phone_number = re.search(r'^(\d{3}--\d{3}--\d{4})',truck_phone_number)
        #Formats phone number to xxx-xxx-xxxx
    truck_email_address = models.CharField(max_length = 50)
    match_truck_email_address = (r'\w+@\w+', truck_email_address)
        #Formats email address field name@example.com
    rating = models.FloatField(default=0.0)
        #Rating for new Truck is set to 0.0

    
class OperationHours(models.Model):
    truck = models.ForeignKey(Truck)
    weekday = models.IntegerField(choices=weekdays, unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

class Announcements(models.Model):
    truck = models.ForeignKey(Truck)
    announcement_text = models.CharField(max_length = 500)

class TruckList(models.Model):
    user = models.ForeignKey(UserProfile)
    truck = models.ForeignKey(Truck)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=0.0)

class Header(models.Model):
    header_name = models.CharField(max_length = 50)

class Menu(models.Model):
    truck = models.ForeignKey(Truck)
    header = models.ForeignKey(Header)

class Item(models.Model):
    header = models.ForeignKey(Header)
    item_name = models.CharField(max_length = 50)
    item_description = models.CharField(max_length = 100)
    item_price = models.FloatField(null=True, blank=True, default=None)

class Tags(models.Model):
    tag_name = models.CharField(max_length = 20)

#Links Truck and Tags models
class Truck_Tag(models.Model):
    tag = models.ForeignKey(Tags)
    truck = models.ForeignKey(Truck)

class Profile_Picture(models.Model):
    image = models.ImageField(upload_to='profile_image', default = 'profile_image/img_avatar2.png')
