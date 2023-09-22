from django.db import models

# Create your models here.
class Rooms(models.Model):

    room_no = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=60)

    def __str__ (self):
        return f"{self.room_no}"


class Guest(models.Model):

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=True)
    gov_id = models.IntegerField(primary_key=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
