from django.db import models

# Create your models here.

class Dish(models.Model):
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name + " (" + self.description + ")"
        
class Meal(models.Model):
    
    class Meta:
        ordering = ["-datetime"]
    
    dish = models.ForeignKey(Dish)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.dish.name + " was made at " + self.datetime