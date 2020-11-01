from django.db import models
from django.conf import settings


class Transaction(models.Model):
    OPTIONS = (
        ('e', 'E'),
        ('s', 'S')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=1, choices=OPTIONS)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.value}'
