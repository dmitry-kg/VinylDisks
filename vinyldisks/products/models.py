from django.db import models
import uuid
from datetime import datetime

class ProductsDescriptionVinyl(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, null=False, blank=False, editable=False)
    artist_name = models.CharField(max_length=255, null=False, blank=False)
    album_name = models.CharField(max_length=255, null=False, blank=False)
    photo = models.ImageField(upload_to='photos/vinyls/%Y/%m/%d')
    price = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist_name + '-' + self.album_name
    class Meta:
        verbose_name = 'Виниловая пластинка'
        verbose_name_plural = 'Виниловые пластинки'

class ProductsDescriptionHiFi(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, null=False, blank=False, editable=False)
    photo = models.ImageField(upload_to='photo/hifi/%Y/%m/%d')
    name = models.CharField(max_length=255, null=False, blank=False)
    size =  models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Аудио Компонент'
        verbose_name_plural = 'Аудио Компоненты'