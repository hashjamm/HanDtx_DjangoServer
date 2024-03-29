# Generated by Django 3.2 on 2024-01-19 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hanDtxPrototypeApp', '0002_alter_questionnaireissuechecking_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emotiondiaryrecords',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnaireexercise',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairegad7',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairenutrition',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairephq9',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairepss10',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnaireselfdiagnosis',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairesmokingdrinking',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairestress',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnairewellbeingscale',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='userinfo',
            unique_together={('user_id',)},
        ),
    ]
