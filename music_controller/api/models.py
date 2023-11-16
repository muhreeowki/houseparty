from django.db import models
import random
import string


def generate_code():
    """Function to generate a uniqe room code"""

    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=6))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.
class Room(models.Model):
    """Room model to represent a music room. That users will join"""

    code = models.CharField(max_length=8, default=generate_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=True, default=False)
    votes_to_skip = models.IntegerField(null=True, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
