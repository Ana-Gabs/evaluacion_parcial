# Generated by Django 3.1.12 on 2025-04-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('ave', 'Ave')], max_length=10)),
                ('edad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pets/images/')),
                ('adoptado', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='pet',
            name='created_by',
        ),
    ]
