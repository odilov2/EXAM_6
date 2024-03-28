from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product/product')
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    lifetime = models.DateField()
    quality = models.CharField(max_length=30)
    checks = models.CharField(max_length=20)
    weight = models.FloatField()

    def __str__(self):
        return self.title


class FeaturedProducts(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product/product')
