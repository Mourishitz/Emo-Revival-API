from django.db import models
from ..core.models import Core
from .choices import GENRE_CHOICES
from multiselectfield import MultiSelectField


class Event(Core):
    name = models.CharField(max_length=150, unique=True)
    genre = MultiSelectField(choices=GENRE_CHOICES, default=None, blank=True, null=True)
    tickets = models.IntegerField()
    sold_out = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    date_time = models.DateTimeField(auto_now_add=False)
    # guests = models.ForeignKey(User, on_delete=models.PROTECT, related_name="event", null=True)
    # def __str__(self):
    #     return "%s (%s)" %(self.name, self.date_time)
