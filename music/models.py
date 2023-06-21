from django.db import models

# Create your models here.
class Music(models.Model):
    song_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    song = models.FileField(upload_to='songs/')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.song

    class Meta:
        verbose_name = "Музыка"

class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name