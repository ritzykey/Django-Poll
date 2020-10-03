from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.TextField()
    example = models.TextField(null=True)
    example4 = []
    options = models.JSONField(null=True, default={})

    def __str__(self):
        return self.question
    
    def example2(self,example2):
        for i in range(len(example2)):
            self.example4.append(0)
        return dict(zip(example2.split(','),self.example4))
    

    def total(self):
        return sum(self.options.values())




