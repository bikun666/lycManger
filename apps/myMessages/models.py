from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    message = models.CharField(default="", max_length=160)
    updateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message'
        verbose_name = "留言"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name