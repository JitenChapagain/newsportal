from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    en_name = models.CharField(max_length=100)
    np_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.en_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.en_name

class Tag(models.Model):
    en_tag = models.CharField(max_length=100)
    np_tag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.en_tag)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.en_tag

class News(models.Model):
    en_title = models.CharField(max_length=200)
    np_title = models.CharField(max_length=200)
    en_description = models.TextField()
    np_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True)
    file = models.FileField(upload_to='news_files/', blank=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.en_title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.en_title
