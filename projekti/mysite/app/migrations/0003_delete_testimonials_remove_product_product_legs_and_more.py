# Generated by Django 4.0.5 on 2022-06-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_color_contact_material_product_testimonials_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testimonials',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_legs',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_pillow',
        ),
        migrations.AddField(
            model_name='product',
            name='product_garanci',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_wateresistent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]