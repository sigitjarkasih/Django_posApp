from django.db import models
from django.utils import timezone

class PosCategory(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1) 
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pos_Category" 

    def __str__(self):
        return self.name

class PosProducts(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.CharField(
        null=True, blank=True, max_length=32, default=None)
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=1) 
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = "pos_Products" 

    def __str__(self):
        return self.code + " - " + self.name
    
class posSale(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount =  models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    tendered_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_change = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = "pos_Sale" 

    def __str__(self):
        return self.code
    
class posSalesItems(models.Model):
    sale_id = models.CharField(max_length=32, null=True, blank=True)
    product_id = models.CharField(max_length=32, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)

    class Meta:
        db_table = "pos_Sales_Items" 
    
    

