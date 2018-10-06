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

weekdays = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    ]

class Truck(models.Model):
    truck_name = models.CharsField(max_length = 50)
    truck_description = models.CharsField(max_length = 150)
    truck_phone_number = models.CharsField(max_length = 12)
    match_phone_number = re.search(r'^(\d{3}--\d{3}--\d{4})',truck_phone_number)
        #Formats phone number to xxx-xxx-xxxx
    truck_email_address = models.CharsField(max_length = 50)
    match_truck_email_address = (r'\w+@\w+', truck_email_address)
        #Formats email address field name@example.com
    rating = DoubleField(default=0.0)
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
    truck = ForeignKey(Truck)
    rating = FloatField(min=1.0, max=5.0, default=0.0)

class Header(models.Model)
    header_name = models.CharsField(max_length = 50)

class Menu(models.Model):
    truck = ForeignKey(Truck)
    header = ForeignKey(Header)

class Item(models.Model):
    header = ForeignKey(Header)
    item_name = models.CharsField(max_length = 50)
    item_description = model.CharsField(max_lenth = 100)
    item_price = model.FloatField(null=True, blank=True, default=None)

class Tags(models.Model):
    tag_name = model.CharsField(max_length = 20)

#Links Truck and Tags models
class Truck_Tag(models.Model):
    tag = ForeignKey(Tags)
    truck = ForeignKey(Truck)

class Profile_Picture(models.Model):
    image = models.ImageField(upload_to='profile_image', default = 'profile_image/img_avatar2.png')
