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


class Article(models.Model):
    url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    article_url = models.CharField(unique=True, max_length=767)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleImgConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_img_configuration'


class ArticlePublishDateConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_publish_date_configuration'


class ArticleTextConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_text_configuration'


class ArticleTopicHeadlineConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    parent_tag_name = models.CharField(max_length=20)
    child_tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_topic_headline_configuration'


class ArticleUrlConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', models.DO_NOTHING)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20)
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_url_configuration'

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'

class DomainUrl(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING)
    url = models.CharField(max_length=600)
    is_active = 1          ##*******Include this is active here later........

    class Meta:
        managed = False
        db_table = 'domain_url'


class UnprocesssedScrapeData(models.Model):
    article = models.OneToOneField(Article, models.DO_NOTHING)
    unprocessed_news_topic = models.TextField()
    unprocessed_news_description = models.TextField()
    publication_date = models.CharField(max_length=767)
    image_href = models.CharField(max_length=767)
    scrape_time_stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'unprocesssed_scrape_data'


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'



