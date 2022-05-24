from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY = (
    ("Technology", "Technology"),
    ("Data Science", "Data Science"),
    ("Database", "Database"),
    ("Security", "Security"),
    ("Web Dev", "Web dev"),
    ("Machine learning", "Machine learning")
)
class Story(models.Model):
    title = models.CharField(max_length= 100)
    category = models.CharField(choices= CATEGORY,max_length=30, default= "Technology")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


   
    def __str__(self):
        return self.title