# Generated by Django 2.2.6 on 2024-05-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accountant_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=500)),
                ('Other_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('image', models.ImageField(default='T.png', upload_to='profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='category_ph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=500)),
                ('Othername', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(default='T.png', upload_to='profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Pham_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=500)),
                ('Other_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('image', models.ImageField(default='T.png', upload_to='profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=500)),
                ('Othername', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('price', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(default='T.png', upload_to='profile_pic')),
                ('status', models.CharField(default='False', max_length=400)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Category')),
            ],
        ),
    ]
