from django.db import models

class PasswordRecord(models.Model):
    website_name = models.charField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    notes = models.TextField(blank = True)

    def __str__(self):
        return self.website__name
