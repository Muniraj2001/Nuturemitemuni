# Generated by Django 4.2.7 on 2023-11-08 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_rename_image_productimage_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.IntegerField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Gujrat', 'Gujrat'), ('Assam', 'Assam'), ('Delhi', 'Delhi'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Bihar', 'Bihar'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Goa', 'Goa')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MH', 'Men Health'), ('OG', 'Organic'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants')], max_length=2),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
