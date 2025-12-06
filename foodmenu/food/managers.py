from django.db import models
class itemManager(models.Manager):
    def cheap(self):
        return self.filter(item_price__lt=5)
    
    def expensive(self):
        return self.filter(item_price__gt=5)
    def search(self, keyword):
        return self.filter(item_name__icontains=keyword)
    #soft delete
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)
    #Restoring the delete(in shell): 
    #1. Access the item through items.objects.deleted
    #2. Get the item from the delted query set usinf 'item_name__icontains' filter
    #3. save the item in a variable (this also contains a quesry et so acces through .first())
    #4. Set the flags false (var.is_deleted=False, var.deleted_at= None)