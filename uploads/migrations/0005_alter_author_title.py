# Generated by Django 4.0 on 2021-12-31 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_alter_author_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3, null=True),
        ),
    ]