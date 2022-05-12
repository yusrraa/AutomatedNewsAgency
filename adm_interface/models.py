from django.db import models

# Create your models here.

SCRAPE_CHOICES = (('class','Scrape by Class'),('id','Scrape by ID'))


class tb1_master_domain(models.Model):
    domain_name = models.CharField(max_length=90);

    def __str__(self):
        return self.domain_name


class tb2_Url_details_table(models.Model):
    domain = models.ForeignKey(tb1_master_domain, on_delete=models.CASCADE)
    article_url = models.CharField(max_length=100)
    url_string = models.CharField(max_length=200)







class Article(models.Model):
    url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    article_url = models.CharField(unique=True, max_length=767)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleImgConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20,choices=SCRAPE_CHOICES, default='class')
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_img_configuration'


class ArticlePublishDateConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20,choices=SCRAPE_CHOICES, default='class')
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_publish_date_configuration'


class ArticleTextConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20,choices=SCRAPE_CHOICES, default='class')
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_text_configuration'


class ArticleTopicHeadlineConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    parent_tag_name = models.CharField(max_length=20)
    child_tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20,choices=SCRAPE_CHOICES, default='class')
    attribute_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'article_topic_headline_configuration'


class ArticleUrlConfiguration(models.Model):
    domain_url = models.ForeignKey('DomainUrl', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=20)
    scrape_type = models.CharField(max_length=20,choices=SCRAPE_CHOICES, default='class')
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
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    url = models.CharField(max_length=600)
    is_active = 1                 ##*******Include this is active here later........

    class Meta:
        managed = False
        db_table = 'domain_url'



class ProcesssedScrapeData(models.Model):
    article_id = models.IntegerField()
    processed_news_topic = models.TextField()
    processed_news_description = models.TextField()
    image_href = models.CharField(max_length=767)
    scrape_date_stamp = models.CharField(max_length=20)
    scrape_time_stamp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'processsed_scrape_data'


class UnprocesssedScrapeData(models.Model):
    article = models.OneToOneField(Article, models.DO_NOTHING)
    unprocessed_news_topic = models.TextField()
    unprocessed_news_description = models.TextField()
    publication_date = models.CharField(max_length=767)
    image_href = models.CharField(max_length=767)
    scrape_date_stamp = models.CharField(max_length=20)
    scrape_time_stamp = models.CharField(max_length=20)

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'









class AdmInterfaceTb1MasterDomain(models.Model):
    id = models.BigAutoField(primary_key=True)
    domain_name = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'adm_interface_tb1_master_domain'


class AdmInterfaceTb2UrlDetailsTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_url = models.CharField(max_length=100)
    url_string = models.CharField(max_length=200)
    domain = models.ForeignKey(AdmInterfaceTb1MasterDomain, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adm_interface_tb2_url_details_table'







