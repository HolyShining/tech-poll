# Generated by Django 2.1.5 on 2019-02-07 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersmodel',
            name='f_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actions.GradesModel'),
        ),
    ]
