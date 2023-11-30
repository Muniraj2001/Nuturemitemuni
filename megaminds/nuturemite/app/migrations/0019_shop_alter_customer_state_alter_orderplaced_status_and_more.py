# Generated by Django 4.2.7 on 2023-11-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_delete_shop_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_sale', models.BooleanField(default=False)),
                ('reviews', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(choices=[('E', 'Electronics'), ('C', 'Clothing'), ('B', 'Books')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Bihar', 'Bihar'), ('Daman and Diu', 'Daman and Diu'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Haryana', 'Haryana'), ('Assam', 'Assam'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Chandigarh', 'Chandigarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Gujrat', 'Gujrat'), ('Chattisgarh', 'Chattisgarh'), ('Jammu & Kashmir', 'Jammu & Kashmir')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Wey', 'On The Way'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('WH', 'Women health'), ('AN', 'Antioxidants')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('WH', 'Women health'), ('AN', 'Antioxidants')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('IH', 'Immune Health'), ('OG', 'Organic'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('WH', 'Women health'), ('AN', 'Antioxidants')], max_length=2),
        ),
    ]