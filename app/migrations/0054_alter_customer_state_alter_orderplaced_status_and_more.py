# Generated by Django 4.2.7 on 2023-12-14 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0053_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Gujrat', 'Gujrat'), ('Daman and Diu', 'Daman and Diu'), ('Chattisgarh', 'Chattisgarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Wey', 'On The Way'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('MH', 'Men Health'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MH', 'Men Health'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('MH', 'Men Health'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('MH', 'Men Health'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
