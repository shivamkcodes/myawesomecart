from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    prev_price=models.IntegerField(default=0)
    desc =models.TextField(max_length=3000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField
    contact_name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    query=models.CharField(max_length=50,default="")
    phone=models.IntegerField(default="")


    def __str__(self):
        return self.contact_name




class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    amount=models.IntegerField(default=0)
    items_json=models.CharField(max_length=500)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90)
    zip_code=models.CharField(max_length=90)
    phone=models.CharField(max_length=90,default="")



class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7] + "..."

