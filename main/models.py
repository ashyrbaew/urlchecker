from django.db import models
from django.conf import settings


class Urls(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=400, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name="url_item")

    class Meta:
        verbose_name = "url_item"
        verbose_name_plural = "url_items"

    def __str__(self):
        return self.title