# Generated by Django 5.1.1 on 2024-10-07 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_alter_answer_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(db_column='content', on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='server.question'),
        ),
    ]
