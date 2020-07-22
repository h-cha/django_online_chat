from django.db import models

# Create your models here.

class Word(models.Model):
    villager = models.CharField(max_length=50)
    wolf = models.CharField(max_length=50)
    
    def __str__(self):
        return '<Word:id=' + str(self.id) + ', ' + self.villager + ', ' + self.wolf + '>'
    
class Room(models.Model):
    room_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    word = models.CharField(max_length=50,null=True)
    user_count = models.IntegerField(default=0)