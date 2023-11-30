# Generated by Django 4.2.7 on 2023-11-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Assam', 'Assam'), ('Daman and Diu', 'Daman and Diu'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Gujrat', 'Gujrat'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Haryana', 'Haryana'), ('Goa', 'Goa')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'packed'), ('On The Wey', 'On The Way'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('IH', 'Immune Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health')], max_length=2),
        ),
    ]
