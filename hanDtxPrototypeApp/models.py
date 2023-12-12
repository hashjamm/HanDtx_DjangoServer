# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, transaction
from django.utils import timezone


class UserInfo(models.Model):
    id = models.BigAutoField(help_text="UserInfo pk", primary_key=True)
    user_id = models.CharField(max_length=32, unique=True, verbose_name="user 아이디")
    user_pw = models.CharField(max_length=128, verbose_name="user 비밀번호")
    name = models.CharField(max_length=10, verbose_name="이름")
    address = models.TextField(verbose_name="주소")
    created = models.DateTimeField(default=timezone.now, verbose_name="생성 날짜")


class LoginInfo(models.Model):
    id = models.BigAutoField(help_text="LoginInfo pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    login_time = models.DateTimeField(auto_now_add=True, verbose_name="로그인 시간")


class EmotionDiaryRecords(models.Model):
    id = models.BigAutoField(help_text="EmotionDiaryRecords pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    score_type_1 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 기분 점수")
    input_text_type_1 = models.TextField(verbose_name="입력된 기분 텍스트", blank=True, null=True)
    score_type_2 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 불안 점수")
    input_text_type_2 = models.TextField(verbose_name="입력된 불안 텍스트", blank=True, null=True)
    score_type_3 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 식이 점수")
    input_text_type_3 = models.TextField(verbose_name="입력된 식이 텍스트", blank=True, null=True)

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireIssueChecking(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireIssueChecking pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    checkbox_1 = models.BooleanField(blank=True, default=False, verbose_name="1번 체크 박스 선택 상태")
    checkbox_2 = models.BooleanField(blank=True, default=False, verbose_name="2번 체크 박스 선택 상태")
    checkbox_3 = models.BooleanField(blank=True, default=False, verbose_name="3번 체크 박스 선택 상태")
    checkbox_4 = models.BooleanField(blank=True, default=False, verbose_name="4번 체크 박스 선택 상태")
    checkbox_5 = models.BooleanField(blank=True, default=False, verbose_name="5번 체크 박스 선택 상태")
    checkbox_6 = models.BooleanField(blank=True, default=False, verbose_name="6번 체크 박스 선택 상태")
    checkbox_7 = models.BooleanField(blank=True, default=False, verbose_name="7번 체크 박스 선택 상태")
    checkbox_8 = models.BooleanField(blank=True, default=False, verbose_name="8번 체크 박스 선택 상태")
    checkbox_9 = models.BooleanField(blank=True, default=False, verbose_name="9번 체크 박스 선택 상태")
    checkbox_10 = models.BooleanField(blank=True, default=False, verbose_name="10번 체크 박스 선택 상태")
    checkbox_11 = models.BooleanField(blank=True, default=False, verbose_name="11번 체크 박스 선택 상태")
    checkbox_12 = models.BooleanField(blank=True, default=False, verbose_name="12번 체크 박스 선택 상태")
    checkbox_13 = models.BooleanField(blank=True, default=False, verbose_name="13번 체크 박스 선택 상태")
    checkbox_14 = models.BooleanField(blank=True, default=False, verbose_name="14번 체크 박스 선택 상태")
    checkbox_15 = models.BooleanField(blank=True, default=False, verbose_name="15번 체크 박스 선택 상태")
    checkbox_16 = models.BooleanField(blank=True, default=False, verbose_name="16번 체크 박스 선택 상태")
    checkbox_17 = models.BooleanField(blank=True, default=False, verbose_name="17번 체크 박스 선택 상태")
    checkbox_18 = models.BooleanField(blank=True, default=False, verbose_name="18번 체크 박스 선택 상태")
    checkbox_19 = models.BooleanField(blank=True, default=False, verbose_name="19번 체크 박스 선택 상태")
    checkbox_20 = models.BooleanField(blank=True, default=False, verbose_name="20번 체크 박스 선택 상태")
    checkbox_21 = models.BooleanField(blank=True, default=False, verbose_name="21번 체크 박스 선택 상태")
    checkbox_22 = models.BooleanField(blank=True, default=False, verbose_name="22번 체크 박스 선택 상태")
    input_text = models.TextField(blank=True, null=True, verbose_name="22번 체크 박스 입력 텍스트")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireSelfDiagnosis(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireSelfDiagnosis pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="9번 문항 점수")
    result_10 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="10번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireWellBeingScale(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireWellBeingScale pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnairePHQ9(models.Model):
    id = models.BigAutoField(help_text="QuestionnairePHQ9 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="9번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireGAD7(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireGAD7 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="7번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnairePSS10(models.Model):
    id = models.BigAutoField(help_text="QuestionnairePSS10 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="9번 문항 점수")
    result_10 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="10번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class ExerciseType(models.Model):
    id = models.BigAutoField(help_text="ExerciseType pk", primary_key=True)
    type = models.CharField(max_length=50, unique=True)


class QuestionnaireExercise(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireExercise pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="9번 문항 점수")
    result_10 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="10번 문항 점수")
    result_11 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="11번 문항 점수")
    result_12 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="12번 문항 점수")
    result_13_exer_type = models.ManyToManyField(ExerciseType, through="QuestionnaireExerciseExerciseType",
                                                 related_name="exercise_type", null=True)
    result_13_input_text = models.TextField(verbose_name="기타 운동 종목 입력 문자열", null=True)

    class Meta:
        unique_together = ['user_info_id', 'date']

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

            through_model = self.result_13_exer_type.through
            through_model.objects.filter(questionnaire_exercise=self).delete()

            exercise_type_objects = [
                through_model(questionnaire_exercise=self, exercise_type=exercise_type)
                for exercise_type in self.result_13_exer_type.all()
            ]

            through_model.objects.bulk_create(exercise_type_objects)


class QuestionnaireExerciseExerciseType(models.Model):
    questionnaire_exercise = models.ForeignKey(QuestionnaireExercise, on_delete=models.CASCADE,
                                               related_name="questionnaire_exercise_relations")
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING, related_name="exercise_type_relations")


class QuestionnaireSmokingDrinking(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireSmokingDrinking pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    smoking_result_1 = models.IntegerField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)],
                                           verbose_name="1번 흡연 문항 점수")
    smoking_result_2 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(3)],
                                           verbose_name="2번 흡연 문항 점수")
    smoking_result_3 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(7)],
                                           verbose_name="3번 흡연 문항 점수")
    smoking_result_4 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(3)],
                                           verbose_name="4번 흡연 문항 점수")
    smoking_result_5 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)],
                                           verbose_name="5번 흡연 문항 점수")
    smoking_result_6 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)],
                                           verbose_name="6번 흡연 문항 점수")
    smoking_result_7 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(3)],
                                           verbose_name="7번 흡연 문항 점수")
    smoking_result_8 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)],
                                           verbose_name="8번 흡연 문항 점수")
    smoking_result_9 = models.IntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(1)],
                                           verbose_name="9번 흡연 문항 점수")
    drinking_result_1 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="1번 음주 문항 점수")
    drinking_result_2 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="2번 음주 문항 점수")
    drinking_result_3 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="3번 음주 문항 점수")
    drinking_result_4 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="4번 음주 문항 점수")
    drinking_result_5 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="5번 음주 문항 점수")
    drinking_result_6 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="6번 음주 문항 점수")
    drinking_result_7 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="7번 음주 문항 점수")
    drinking_result_8 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="8번 음주 문항 점수")
    drinking_result_9 = models.IntegerField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(4)],
                                            verbose_name="9번 음주 문항 점수")
    drinking_result_10 = models.IntegerField(blank=True, null=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(2)],
                                             verbose_name="10번 음주 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireStress(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireStress pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")

    class Meta:
        unique_together = ['user_info_id', 'date']


class QuestionnaireNutrition(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireNutrition pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="9번 문항 점수")
    result_10 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="10번 문항 점수")
    result_11_snack_type = models.TextField(verbose_name="11번 문항 입력 간식 종류")
    result_11_consume_num = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="11번 문항 입력 간식 섭취 횟수")

    class Meta:
        unique_together = ['user_info_id', 'date']
