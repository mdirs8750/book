# Generated by Django 3.2.9 on 2022-02-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbook', '0004_rename_firsname_clnt_info_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimg',
            name='pimage',
            field=models.ImageField(upload_to='upload/productimg'),
        ),
    ]