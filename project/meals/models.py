from django.db import models

# Create your models here.

class Dish(models.Model):

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return "{0} ({1})".format(self.name, self.description)

class Meal(models.Model):

    class Meta:
        ordering = ["-datetime"]

    dish = models.ForeignKey(Dish)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return "{0} was made at {1}".format(self.dish.name, self.datetime)
