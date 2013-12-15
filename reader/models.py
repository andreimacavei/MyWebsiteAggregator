from django.db import models

# Create your models here.

class FeedUrl(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    url = models.URLField(max_length = 200, unique = True);
    lastVisited = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        if not self.name:
            return self.url
        else:
            return self.name