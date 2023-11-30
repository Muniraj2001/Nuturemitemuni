# Generated by Django 4.2.7 on 2023-11-08 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('SH', 'Sexual health')], max_length=2),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
