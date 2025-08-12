# from django.db import models
# from conf.settings import AUTH_USER_MODEL
# User = AUTH_USER_MODEL
# from home.models import Gullar
# # Create your models here.

# class Card(models.Model):
#     user = models.OneToOneField(on_delete=models.CASCADE, blank=True, null=True)
#     create_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.user.first_name
    
#     @property
#     def total_price(self):
#         return sum(item.total_price for item in self.items)
 

# class CaradItem(models.Model):
#     card = models.ForeignKey(on_delete=models.CASCADE)
#     gullar = models.ForeignKey(Gullar, on_delete=models.CASCADE, blank=True, null=True)
#     amount = models.PositiveIntegerField(default=1)


#     def __str__(self): 
#         return self.gullar.name

#     @property
#     def total_price(self):
#         return self.gullar.price * self.amount