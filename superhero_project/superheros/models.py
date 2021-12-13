from django.db import models
from django.db.models import fields

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)
    
#class Form(Superhero):
#    class Meta:
#        model = Superhero
#        fields = ('Name', 'Alter Ego', 'Primary Ability', 'Secondary Ability', 'Catchphrase')
#        labels = {
#            'Name': '',
#            'Alter Ego': '',
#            'Primary Ability': '',
#            'Secondary Ability': '',
#            'Catchphrase': '',
#        }
    
    def __str__(self):
        return self.name
    
    