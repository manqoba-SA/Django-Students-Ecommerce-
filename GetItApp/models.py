from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='categories', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('GetitApp:products_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    QUANTITY_SIZES = (
        ('per item', 'per item'),
        ('per packet', 'per packet'),
        ('per plastic', 'per plastic'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,)
    image = models.ImageField(upload_to='products/%Y/%M/%D', blank=True)
    slide_image = models.ImageField(upload_to='products/%Y/%M/%D', blank=True)
    slide_image1 = models.ImageField(upload_to='products/%Y/%M/%D', blank=True)
    slide_image2 = models.ImageField(upload_to='products/%Y/%M/%D', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=100, choices=QUANTITY_SIZES)
    brand = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    information = models.TextField(blank=True)
    important_information = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    service = models.BooleanField(default=False)
    is_technology = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('GetItApp:single', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class Month_Special(models.Model):
    name = models.CharField(max_length=200)
    it_is_advertise = models.BooleanField(default=False)
    it_is_youtube_video = models.BooleanField(default=False)
    first_slide_image = models.ImageField(upload_to='specials', blank=True)
    second_slide_image = models.ImageField(upload_to='specials', blank=True)
    third_slide_image = models.ImageField(upload_to='specials', blank=True)
    procedure_for_ordering = models.TextField(blank=True)
    note_on_ordering = models.TextField(blank=True)
    youtube_link = models.URLField(blank=True)
