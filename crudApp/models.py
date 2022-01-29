from django.db import models

CATEGORY_CHOICES = (
    ('Choose one :', ''),
    ('Education', 'Education'),
    ('Sports', 'Sports'),
    ('Politics', 'Politics')
)


class Category(models.Model):
    name = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default="Choose one :")

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
