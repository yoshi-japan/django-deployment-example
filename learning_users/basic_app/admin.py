from django.contrib import admin
# I forgot to import User but it doesn't have to do with the problem.
from basic_app.models import UserProfileInfo, User
# Register your models here.
admin.site.register(UserProfileInfo)


# Note that whenever you add it the admin.py file or create a new model,
# where youre going to want to do is
# down here at the bottom, say python manage.py migrate ...and migrations and migrate again.
