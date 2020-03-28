from django.db import models

class blogs(models.Model):
   title=models.CharField(max_length=200)
   pub_date=models.DateTimeField()
   pic=models.ImageField(upload_to='images/')
   body=models.TextField()

def __str__(self):   
   return self.title
   
def summary(self):
   return self.body[:200]    
   
 #it lets u return only 200 words of the totsl ewords yo wrote













          #on you Wow! u screw up ans get urc 




#create A blog models
   #title
   #pub_date
   #body 
   #image

#add the blog app to the settings

#create a migration

#migrate

#Add to the admin



