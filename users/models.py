from django.db import models

class Users():
    objects = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField
    password = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.first_name
