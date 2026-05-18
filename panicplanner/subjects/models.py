from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
      User = models.ForeignKey(User,on_delete=models.CASCADE)
      name= models.CharField(max_length=200)
      description= models.TextField( blank= True)
      exam_date=models.DateField()
      created_at=models.DateTimeField(auto_now_add=True)


def __srt__(self):
      return self.name



class Exam(models.Model):
      subject= models.ForeignKey(Subject,on_delete=models.CASCADE)

      title= models.CharField(max_length=200)

      exam_date=models.DateField()
      total_marks=models.IntegerField()

      def __str__(self):
            return self.title


