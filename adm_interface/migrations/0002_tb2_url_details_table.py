# Generated by Django 3.2.7 on 2022-01-10 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb2_Url_details_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_data_id', models.CharField(max_length=100)),
                ('url_string', models.CharField(max_length=200)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm_interface.tb1_master_domain')),
            ],
        ),
    ]