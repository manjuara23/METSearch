from django.db import models

#from django.utils.text import slugify



class Bus(models.Model):

    bus_name = models.CharField(max_length=50, unique=True)

    bus_id = models.CharField( max_length=50 , null = True , blank = True)

    route = models.CharField(max_length=50, unique=True)
    
    type = models.CharField(max_length=50, null=True)
    
    station = models.CharField(max_length=2000,null=True)
    
    def __str__(self):
        return self.bus_name

    

class Bus_Stopage(models.Model):
    # Stopage_id = models.IntegerField(primary_key=True)

    stopage_name = models.CharField( max_length=150 , null = True , blank = True)

    location = models.CharField( max_length=50 , null = True , blank = True)
    
    def __str__(self):
        return self.stopage_name
    
    


class Bus_Route(models.Model):
    
    bus_stopage = models.ForeignKey(Bus_Stopage, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    
    
        
    # Route_id = models.CharField(max_length=50, unique=True)
    
    
