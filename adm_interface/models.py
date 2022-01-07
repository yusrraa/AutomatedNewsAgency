from django.db import models

# Create your models here.

class tb1_master_domain(models.Model):
    domain_name = models.CharField(max_length=90);

    def __str__(self):
        return self.domain_name

