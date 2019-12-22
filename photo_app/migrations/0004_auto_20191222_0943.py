# Generated by Django 2.2 on 2019-12-22 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('photo_app', '0003_commentmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photomodel',
            name='User',
        ),
        migrations.AddField(
            model_name='photomodel',
            name='upload_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_post', to='user_app.UserModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_app.UserModel'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='photo_app.PhotoModel'),
        ),
    ]