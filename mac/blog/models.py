from django.db import models

class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    writer=models.CharField(max_length=50,default="")
    sec_writer=models.CharField(max_length=50,default="")

    title=models.CharField(max_length=50)
    head0=models.CharField(max_length=500,default="")
    chead0=models.CharField(max_length=5000,default="")
    head1=models.CharField(max_length=500,default="")
    chead1=models.CharField(max_length=5000,default="")
    head2 =models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=5000, default="")
    thumbnail=models.ImageField(upload_to="blog/images",default="")
    pub_date = models.DateField()


    def __str__(self):
        return self.title



# class blogwrite(models.Model):
#
#     writer_name=models.CharField(max_length=50,default="")
#     email=models.CharField(max_length=50,default="")
#     title = models.CharField(max_length=50)
#     head0 = models.CharField(max_length=500, default="")
#     chead0 = models.CharField(max_length=5000, default="")
#     head1 = models.CharField(max_length=500, default="")
#     chead1 = models.CharField(max_length=5000, default="")
#     head2 = models.CharField(max_length=500, default="")
#     chead2 = models.CharField(max_length=5000, default="")
#
#     def __str__(self):
#         return self.title
