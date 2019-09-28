# Generated by Django 2.2.5 on 2019-09-28 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190928_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Pais'),
            preserve_default=False,
        ),
    ]
