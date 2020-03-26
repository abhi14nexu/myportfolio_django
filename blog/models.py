from django.db import models

class blogs(models.Model):
   title=models.CharField(max_length=200)
   pub_date=models.DateField()
   pic=models.ImageField(upload_to='images/')
   body=models.TextField()
   
















#create A blog models
   #title
   #pub_date
   #body 
   #image

#add the blog app to the settings

#create a migration

#migrate

#Add to the admin



