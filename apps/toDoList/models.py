from django.db import models

# Create your models here.
class ToDoList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(default="", max_length=1600)
    updateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'toDoList'
        verbose_name = "要做的事"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name