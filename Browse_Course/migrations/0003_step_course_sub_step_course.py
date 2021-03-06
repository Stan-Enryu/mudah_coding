# Generated by Django 3.2.3 on 2021-06-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Browse_Course', '0002_alter_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Browse_Course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Step_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('explanation', models.TextField()),
                ('instruction', models.TextField()),
                ('code', models.TextField()),
                ('output', models.CharField(max_length=255)),
                ('step_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Browse_Course.step_course')),
            ],
        ),
    ]
