# Generated by Django 4.2.7 on 2024-01-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0139_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Goa', 'Goa'), ('Haryana', 'Haryana'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh'), ('Bihar', 'Bihar'), ('Gujrat', 'Gujrat'), ('Delhi', 'Delhi'), ('Chandigarh', 'Chandigarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Assam', 'Assam')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('On The Wey', 'On The Way'), ('Packed', 'packed'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E')], max_length=3),
        ),
    ]
