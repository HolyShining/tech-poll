# Generated by Django 2.1.5 on 2019-02-02 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=60)),
                ('f_section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actions.SectionsModel')),
            ],
            options={
                'db_table': 'stages',
            },
        ),
    ]
