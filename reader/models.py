from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    url = models.URLField(max_length = 200, unique = True)
    lastUpdated = models.DateTimeField(auto_now = True)

    users = models.ManyToManyField('self')

    def __unicode__(self):
        if not self.name:
            return self.url
        else:
            return self.name

class User(models.Model):
    username = models.CharField(max_length = 50, blank = False)
    password = models.CharField(max_length = 30, blank = False)
    subscriptions = models.ManyToManyField(Subscription)

    def subscriptionlist(self):
        return list(self.subscriptions.all)

    def __unicode__(self):
        return self.username