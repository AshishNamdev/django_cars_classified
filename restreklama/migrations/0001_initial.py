# Generated by Django 2.2.12 on 2020-06-01 13:18

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('django_classified', '0003_auto_20180717_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='ThumbnailsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='avatars')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_classified.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('category', models.ManyToManyField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ItemReact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restreklama.CarType')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_classified.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_classified.Item')),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restreklama.ItemType')),
            ],
        ),
    ]
