from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# if you want to add more information than the info that User have, we need to use OneToOneField(User)
class UserProfileInfo(models.Model):
    # this is basically Model class, the default User doesn't have.
    # the default User class has already had things like their username email, first name, last name
    # but if you want to add more attributes to your actual User,we use OneToOneField that inherits form User class.
    # we don't want to inherit User class, it will screw up your database.
    user = models.OneToOneField(User,on_delete=models.CASCADE)

 # the additional attributes below.
    # blank=True means they don't have to fill it out.
    portfolio_site = models.URLField(blank=True)

    # this way the user doesn't need to actually provide their profile picture first that they don't want to.
    # the 'profile_pics' is going to need to be a subdirectory in the media folder we created last time.

    # if youre getting the error that says something like a jpeg disabled
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self): # method
        return self.user.username # the user name is default attribute of the User class.
