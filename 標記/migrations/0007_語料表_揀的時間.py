# Generated by Django 2.1 on 2018-08-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('標記', '0006_auto_20180626_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='語料表',
            name='揀的時間',
            field=models.DateTimeField(null=True),
        ),
    ]
