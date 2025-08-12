# from django.db import models
# from home.models import Gullar
# from auth_user_.models import CustomUser
# # Create your models here.


# class Order(models.Model):
#     STATUS_CHOICES = [
#         {'pending', 'Pending'},
#         {'paid', 'paid'},
#         {'shipped','shipped'},
#         {'canceled', 'canceled'}
#     ]
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.status
#     @property
#     def total_price(self):
#         return sum(item.total_price for item in self.items)


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
#     gullar = models.ForeignKey(Gullar, on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return self.gullar.name
    
#     @property
#     def total_price(self):
#         return self.gullar.price * self.amount




