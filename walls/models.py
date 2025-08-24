from django.db import models

class Tags(models.Model):
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
    

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Список тегов'


class Wallpaper(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField('Изображение для превью', upload_to='image/%D')
    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return f'{self.title}'
    

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Список обоев'


