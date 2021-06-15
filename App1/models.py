
from django.db import models
from django.db.models import Avg

# Create your models here.
from django.db import models
# from django.db.models import Avg, Min, Max, Sum, Count


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    score = models.DecimalField(max_digits=10,decimal_places=3)





#    # def __str__(self):
#         return self.id
#
# # Create your models here.
#     def __unicode__(self):
#         return self.id