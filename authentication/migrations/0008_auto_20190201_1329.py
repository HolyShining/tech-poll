# Generated by Django 2.1.5 on 2019-02-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_userdata_frole'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permissionsmodel',
            old_name='CodeName',
            new_name='code_name',
        ),
        migrations.RenameField(
            model_name='rolesmodel',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='rolesmodel',
            old_name='Permissions',
            new_name='permissions',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='encryptedPass',
            new_name='encrypted_pass',
        ),
        migrations.AlterModelTable(
            name='permissionsmodel',
            table='permissions',
        ),
        migrations.AlterModelTable(
            name='rolesmodel',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='userdata',
            table='user_data',
        ),
    ]