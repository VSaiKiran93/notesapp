from django.db import models


## models are used to setup/desgin a database in tables ##

# Create your models here.
class Note(models.Model):
    
    #blank=True (used in models.py), means on the form level, accept empty forms - the associated field is not required in a form.
    # null=True (used in models.py), means on the database level that Python None values can be stored in the model and be saved (and then end up as SQL NULL values in the database).
    body = models.TextField(null=True, blank=True) #null is set to true, means it can be saved in the database without actual database attributes, # blank is set to true means we cannot submit the forms with no values#
    update = models.DateTimeField(auto_now=True) #auto_now means everytime we use save method to save a note, it takes the timestamp of the method or note
    created = models.DateTimeField(auto_now_add=True) #updates the existing note
    
    
    ## String Representation for admin panel ##
    def __str__(self):
        return self.body[0:50] # character limit of first 50 
    
