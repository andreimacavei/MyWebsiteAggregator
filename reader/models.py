from django.db import models

# Create your models here.

class FeedUrl(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    url = models.URLField(max_length = 200, unique = True)
    lastVisited = models.DateTimeField(auto_now = True)

    users = models.ManyToManyField('self')

    def __unicode__(self):
        if not self.name:
            return self.url
        else:
            return self.name

class UserData(models.Model):
    username = models.CharField(max_length = 50, blank = False)
    password = models.CharField(max_length = 30, blank = False)
    feeds = models.ManyToManyField(FeedUrl)

    def feedslist(self):
        return list(self.feeds.all())

    def __unicode__(self):
        return self.username