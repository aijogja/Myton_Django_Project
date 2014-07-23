from django.db import models

# Create your models here.





class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Part(models.Model):
    #Timestamps
    first_entered_timestamp = models.DateTimeField(auto_now_add=True)
    last_edited_timestamp = models.DateTimeField(auto_now=True)

    #Part Number, Supersessions & Descriptions
    part_number = models.CharField(max_length=30)
    supersessions = models.TextField()
    description = models.CharField(max_length=30)
    long_description = models.TextField()
    full_description = models.TextField()
    full_description_file = models.TextField()

    chassis_range = models.CharField(max_length=30)
    derivitive = models.CharField(max_length=30)

    weight = models.FloatField()

    #Prices
    rrp_price = models.FloatField()
    buy_price = models.FloatField()
    surcharge = models.FloatField()

    #Supplier Information
    supplier_1 = models.TextField()
    supplier_1_part_number = models.TextField()
    supplier_1_leadtime = models.TextField()
    supplier_1_buy_price = models.TextField()

    supplier_2 = models.TextField()
    supplier_2_part_number = models.TextField()
    supplier_2_leadtime = models.TextField()
    supplier_2_buy_price = models.TextField()

    supplier_3 = models.TextField()
    supplier_3_part_number = models.TextField()
    supplier_3_leadtime = models.TextField()
    supplier_3_buy_price = models.TextField()

    supplier_4 = models.TextField()
    supplier_4_part_number = models.TextField()
    supplier_4_leadtime = models.TextField()
    supplier_4_buy_price = models.TextField()

    supplier_5 = models.TextField()
    supplier_5_part_number = models.TextField()
    supplier_5_leadtime = models.TextField()
    supplier_5_buy_price = models.TextField()


    def __unicode__(self):

        #return self.part_number
        return u'%s : %s : %s : %s : %s : %s'% (self.part_number, self.description, self.rrp_price, self.buy_price, self.supersessions, self.surcharge)
    #self.description, self.rrp_price, self.buy_price, self.supersessions, self.surcharge

   # def __unicode__(self):
       # part_number1 = self.part_number
       # part_desciption1 = self.description
        #return part_number1, part_desciption1
        #return self.part_number, self.description, self.rrp_price, self.buy_price, self.surcharge
