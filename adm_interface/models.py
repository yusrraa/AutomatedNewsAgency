from django.db import models

# Create your models here.

class tb1_master_domain(models.Model):
    domain_name = models.CharField(max_length=90);

    def __str__(self):
        return self.domain_name


class tb2_Url_details_table(models.Model):
    domain = models.ForeignKey(tb1_master_domain, on_delete=models.CASCADE)
    article_url = models.CharField(max_length=100)
    url_string = models.CharField(max_length=200)


