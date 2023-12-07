# Create your models here.
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max


class UserInfo(models.Model):
    id = models.BigAutoField(help_text="UserInfo pk", primary_key=True)
    user_id = models.CharField(max_length=32, unique=True, verbose_name="user 아이디")
    user_pw = models.CharField(max_length=128, verbose_name="user 비밀번호")
    name = models.CharField(max_length=10, verbose_name="이름")
    address = models.TextField(verbose_name="주소")
    created = models.DateTimeField(default=timezone.now, verbose_name="생성 날짜")


class LoginInfo(models.Model):
    id = models.BigAutoField(help_text="LoginInfo pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    login_time = models.DateTimeField(auto_now_add=True, verbose_name="로그인 시간")


class EmotionDiaryRecords(models.Model):
    id = models.BigAutoField(help_text="EmotionDiaryRecords pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    score_type_1 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 기분 점수")
    input_text_type_1 = models.TextField(verbose_name="입력된 기분 텍스트")
    score_type_2 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 불안 점수")
    input_text_type_2 = models.TextField(verbose_name="입력된 불안 텍스트")
    score_type_3 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(9)],
                                       verbose_name="입력된 식이 점수")
    input_text_type_3 = models.TextField(verbose_name="입력된 식이 텍스트")

    def save(self, *args, **kwargs):
        existing_records = (
            EmotionDiaryRecords.objects.filter(user_info_id=self.user_info_id, date=self.date)
        ).order_by("-id")  # 해당 유저 및 해당 일자에 대하여 + 최신 데이터 일수록 위로 오도록 정렬

        if existing_records.exists():  # 해당 유저 및 해당 일자에 대한 데이터 있는 경우
            latest_record = existing_records.first()  # 가장 최근 기록을 가져옴

            # 변경된 필드에 새로운 데이터 덮어 쓰기
            latest_record.score_type_1 = self.score_type_1
            latest_record.input_text_type_1 = self.input_text_type_1
            latest_record.score_type_2 = self.score_type_2
            latest_record.input_text_type_2 = self.input_text_type_2
            latest_record.score_type_3 = self.score_type_3
            latest_record.input_text_type_3 = self.input_text_type_3

            latest_record.save()

        else:

            super().save(*args, **kwargs)


class QuestionnaireIssueChecking(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireIssueChecking pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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

    def save(self, *args, **kwargs):
        latest_record_id_dict = EmotionDiaryRecords.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireSelfDiagnosis(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireSelfDiagnosis pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireSelfDiagnosis.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireWellBeingScale(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireWellBeingScale pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireWellBeingScale.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnairePHQ9(models.Model):
    id = models.BigAutoField(help_text="QuestionnairePHQ9 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnairePHQ9.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireGAD7(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireGAD7 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="7번 문항 점수")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireGAD7.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnairePSS10(models.Model):
    id = models.BigAutoField(help_text="QuestionnairePSS10 pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnairePSS10.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class ExerciseType(models.Model):
    id = models.BigAutoField(help_text="ExerciseType pk", primary_key=True)
    type = models.CharField(max_length=50, unique=True)


class QuestionnaireExercise(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireExercise pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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
    result_13_exer_type = models.ManyToManyField(ExerciseType)
    result_13_input_text = models.TextField(verbose_name="기타 운동 종목 입력 문자열")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireExercise.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireSmoking(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireSmoking pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(3)],
                                   verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(7)],
                                   verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(3)],
                                   verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)],
                                   verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)],
                                   verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(3)],
                                   verbose_name="7번 문항 점수")
    result_8 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)],
                                   verbose_name="8번 문항 점수")
    result_9 = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)],
                                   verbose_name="9번 문항 점수")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireSmoking.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireDrinking(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireDrinking pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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
    result_10 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="10번 문항 점수")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireSmoking.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireStress(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireStress pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
    date = models.DateField(auto_now_add=True, verbose_name="입력 날짜")
    result_1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name="1번 문항 점수")
    result_2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], verbose_name="2번 문항 점수")
    result_3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="3번 문항 점수")
    result_4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="4번 문항 점수")
    result_5 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="5번 문항 점수")
    result_6 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="6번 문항 점수")
    result_7 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="7번 문항 점수")

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireStress.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)


class QuestionnaireNutrition(models.Model):
    id = models.BigAutoField(help_text="QuestionnaireNutrition pk", primary_key=True)
    user_info_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, verbose_name="UserInfo pk")
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

    def save(self, *args, **kwargs):
        latest_record_id_dict = QuestionnaireNutrition.objects.filter(
            user_info_id=self.user_info_id, date=self.date).aggregate(
            Max("id"))  # 해당 유저 및 해당 일자에 대하여 가장 큰 id(가장 최근 기록의 id)

        if latest_record_id_dict["id__max"] != self.id:
            return

        super().save(*args, **kwargs)
