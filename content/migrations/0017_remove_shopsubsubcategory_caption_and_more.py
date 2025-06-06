# Generated by Django 5.2 on 2025-05-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_product_shop_subsubsubcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopsubsubcategory',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='shopsubsubcategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='shopsubsubsubcategory',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='shopsubsubsubcategory',
            name='image',
        ),
        migrations.AddField(
            model_name='shopsubcategory',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shopsubcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/subcategories/'),
        ),
    ]
