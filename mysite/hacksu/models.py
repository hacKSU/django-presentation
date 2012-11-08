from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    join_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    members = models.ManyToManyField(Member)

    def __unicode__(self):
        return self.name
