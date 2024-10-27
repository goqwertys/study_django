# Generated by Django 5.1.1 on 2024-09-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                (
                    'preview_image',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to='blog_previews',
                        verbose_name='Preview image'
                    )
                ),
                ('created_at', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False, verbose_name='Publication flag')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Number of views')),
            ],
            options={
                'verbose_name': 'Blog post',
                'verbose_name_plural': 'Blog posts',
            },
        ),
    ]
