# Generated by Django 4.2.7 on 2023-11-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_specialoffer_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialoffer',
            old_name='main_image',
            new_name='mains_image',
        ),
        migrations.RenameField(
            model_name='specialoffer',
            old_name='thumb1',
            new_name='thumblist1',
        ),
        migrations.RenameField(
            model_name='specialoffer',
            old_name='thumb2',
            new_name='thumblist2',
        ),
        migrations.RenameField(
            model_name='specialoffer',
            old_name='thumb3',
            new_name='thumblist3',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Assam', 'Assam'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Bihar', 'Bihar'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Chattisgarh', 'Chattisgarh'), ('Haryana', 'Haryana'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Chandigarh', 'Chandigarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('Accepted', 'Accepted'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care')], max_length=2),
        ),
    ]
