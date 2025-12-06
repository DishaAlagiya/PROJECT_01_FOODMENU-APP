from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import itemManager
class item(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['user_name', 'item_price']),
        ]

    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('food:index')
    
    #for soft delete
    def delete(self, using=None, keep_parents=False):
        self.is_deleted=True
        self.deleted_at=timezone.now()
        self.save()
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=20, db_index=True)
    item_desc = models.CharField(max_length=150,db_index=True)
    item_price = models.DecimalField(max_digits=7, decimal_places=2)
    item_image=models.URLField(max_length=500, default="https://previews.123rf.com/images/igoun/igoun1905/igoun190500141/123440040-spoon-fork-icon-restaurant-canteen-cutlery-or-foodcourt-illustrationt-as-a-simple-vector-sign.jpg")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    #custom Manager
    objects = itemManager()
    all_objects = models.Manager()

class Category(models.Model):
    name = models.CharField(max_length=20)
    add_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.name