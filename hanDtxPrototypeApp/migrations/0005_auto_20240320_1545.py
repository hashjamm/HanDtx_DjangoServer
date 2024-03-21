# Generated by Django 3.2 on 2024-03-20 06:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hanDtxPrototypeApp', '0004_alter_questionnairenutrition_result_11_consume_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='input_text_type_1',
            field=models.TextField(null=True, verbose_name='입력된 기분 텍스트'),
        ),
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='input_text_type_3',
            field=models.TextField(null=True, verbose_name='입력된 식이 텍스트'),
        ),
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='score_type_1',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)], verbose_name='입력된 기분 점수'),
        ),
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='score_type_2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)], verbose_name='입력된 불안 점수'),
        ),
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='score_type_3',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)], verbose_name='입력된 식이 점수'),
        ),
        migrations.AlterField(
            model_name='emotiondiaryrecords',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emotion_diary_records_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='logininfo',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_info_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnaireexercise',
            name='result_13_exer_type',
            field=models.ManyToManyField(related_name='questionnaire_exercise_set', through='hanDtxPrototypeApp.QuestionnaireExerciseExerciseType', to='hanDtxPrototypeApp.ExerciseType'),
        ),
        migrations.AlterField(
            model_name='questionnaireexercise',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_exercise_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnaireexerciseexercisetype',
            name='exercise_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questionnaire_exercise_exercise_type_set', to='hanDtxPrototypeApp.exercisetype'),
        ),
        migrations.AlterField(
            model_name='questionnaireexerciseexercisetype',
            name='questionnaire_exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_exercise_exercise_type_set', to='hanDtxPrototypeApp.questionnaireexercise'),
        ),
        migrations.AlterField(
            model_name='questionnairegad7',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_gad7_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnaireissuechecking',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_issue_checking_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairenutrition',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_nutrition_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairephq9',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_phq9_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairepss10',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_pss10_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnaireselfdiagnosis',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_self_diagnosis_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairesmokingdrinking',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_smoking_drinking_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairestress',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_stress_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
        migrations.AlterField(
            model_name='questionnairewellbeingscale',
            name='user_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_well_being_scale_set', to='hanDtxPrototypeApp.userinfo', verbose_name='UserInfo pk'),
        ),
    ]
