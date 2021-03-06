# Generated by Django 2.2.7 on 2019-12-13 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=120)),
                ('mongo_query', models.CharField(max_length=250, null=True)),
                ('topic_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='data_application.Topic')),
            ],
        ),
    ]
