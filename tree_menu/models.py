from django.db import models


# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Menu(Branch):
    class Meta:
        proxy = True
