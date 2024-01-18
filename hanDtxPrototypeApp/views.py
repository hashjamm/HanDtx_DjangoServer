import requests
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
import json

from .models import UserInfo, ExerciseType
from .models import LoginInfo
from .models import EmotionDiaryRecords
from .models import QuestionnaireSmokingDrinking
from .models import QuestionnaireStress
from .models import QuestionnaireNutrition
from .models import QuestionnaireExercise
from .models import QuestionnaireGAD7
from .models import QuestionnaireIssueChecking
from .models import QuestionnairePHQ9
from .models import QuestionnairePSS10
from .models import QuestionnaireSelfDiagnosis
from .models import QuestionnaireWellBeingScale

from .serializers import UserInfoSerializer
from .serializers import LoginInfoSerializer
from .serializers import EmotionDiaryRecordsSerializer
from .serializers import QuestionnaireSmokingDrinkingSerializer
from .serializers import QuestionnaireStressSerializer
from .serializers import QuestionnaireNutritionSerializer
from .serializers import QuestionnaireExerciseSerializer
from .serializers import QuestionnaireGAD7Serializer
from .serializers import QuestionnaireIssueCheckingSerializer
from .serializers import QuestionnairePHQ9Serializer
from .serializers import QuestionnairePSS10Serializer
from .serializers import QuestionnaireSelfDiagnosisSerializer
from .serializers import QuestionnaireWellBeingScaleSerializer


# Create your views here.

@csrf_exempt
@require_POST
def home(request):
    if request.method == 'POST':
        post_data = request.POST
        response_data = {'status': 'success!!', 'message': 'POST request processed successfully'}

        return HttpResponse(response_data['status'], status=200)

    else:

        return HttpResponse('Method Not Allowed', status=405)


@csrf_exempt
@require_POST
def login(request):
    try:
        search_id = request.POST.get('user_id')
        search_pw = request.POST.get('user_pw')

        obj = UserInfo.objects.get(user_id=search_id)

        if search_pw == obj.user_pw:
            response_data = {"message": "로그인 성공"}

            # 로그인 성공 시 LoginInfo 모델에 로그인 기록 저장
            login_info = LoginInfo(user_info_id=obj)  # user_info_id에 UserInfo 인스턴스가 들어가야 함.
            login_info.save()

            return JsonResponse(response_data, status=200)
        else:
            response_data = {"message": "패스워드가 일치하지 않습니다."}
            return JsonResponse(response_data, status=201)

    except UserInfo.DoesNotExist:

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 감정 다이어리 정보 전체를 반환
@csrf_exempt
@require_POST
def get_emotion_diary_records(request):
    try:
        search_id = request.POST.get('user_id')
        search_date = request.POST.get('date')

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        emotion_diary_records_obj = EmotionDiaryRecords.objects.filter(user_info_id=user_info_obj,
                                                                       date=search_date).get()

        response_data = {"score1": emotion_diary_records_obj.score_type_1,
                         "inputText1": emotion_diary_records_obj.input_text_type_1,
                         "score2": emotion_diary_records_obj.score_type_2,
                         "inputText2": emotion_diary_records_obj.input_text_type_2,
                         "score3": emotion_diary_records_obj.score_type_3,
                         "inputText3": emotion_diary_records_obj.input_text_type_3}

        return JsonResponse(response_data, status=200)

    except EmotionDiaryRecords.DoesNotExist:

        return JsonResponse({"message": "EmotionDiaryRecords not found"}, status=402)

    except EmotionDiaryRecords.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple EmotionDiaryRecords found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_emotion_diary_records(request):
    try:
        update_id = request.POST.get('user_id')
        update_date = request.POST.get("date")
        update_score_type_1 = request.POST.get("score1")
        update_input_text_type_1 = request.POST.get("inputText1")
        update_score_type_2 = request.POST.get("score2")
        update_input_text_type_2 = request.POST.get("inputText2")
        update_score_type_3 = request.POST.get("score3")
        update_input_text_type_3 = request.POST.get("inputText3")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = EmotionDiaryRecords(user_info_id=user_info_obj,
                                             date=update_date,
                                             score_type_1=update_score_type_1,
                                             input_text_type_1=update_input_text_type_1,
                                             score_type_2=update_score_type_2,
                                             input_text_type_2=update_input_text_type_2,
                                             score_type_3=update_score_type_3,
                                             input_text_type_3=update_input_text_type_3)

        update_records.save()

        response_data = {"message": "updated emotion diary records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_issue_checking_survey(request):
    try:
        print(request.POST.get("user_id"))
        print(request.POST.get("date"))
        print(bool(request.POST.get("checkbox1")))
        print(bool(request.POST.get("checkbox2")))

        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_checkbox_1 = bool(request.POST.get("checkbox1"))
        update_checkbox_2 = bool(request.POST.get("checkbox2"))
        update_checkbox_3 = bool(request.POST.get("checkbox3"))
        update_checkbox_4 = bool(request.POST.get("checkbox4"))
        update_checkbox_5 = bool(request.POST.get("checkbox5"))
        update_checkbox_6 = bool(request.POST.get("checkbox6"))
        update_checkbox_7 = bool(request.POST.get("checkbox7"))
        update_checkbox_8 = bool(request.POST.get("checkbox8"))
        update_checkbox_9 = bool(request.POST.get("checkbox9"))
        update_checkbox_10 = bool(request.POST.get("checkbox10"))
        update_checkbox_11 = bool(request.POST.get("checkbox11"))
        update_checkbox_12 = bool(request.POST.get("checkbox12"))
        update_checkbox_13 = bool(request.POST.get("checkbox13"))
        update_checkbox_14 = bool(request.POST.get("checkbox14"))
        update_checkbox_15 = bool(request.POST.get("checkbox15"))
        update_checkbox_16 = bool(request.POST.get("checkbox16"))
        update_checkbox_17 = bool(request.POST.get("checkbox17"))
        update_checkbox_18 = bool(request.POST.get("checkbox18"))
        update_checkbox_19 = bool(request.POST.get("checkbox19"))
        update_checkbox_20 = bool(request.POST.get("checkbox20"))
        update_checkbox_21 = bool(request.POST.get("checkbox21"))
        update_checkbox_22 = bool(request.POST.get("checkbox22"))
        update_input_text = bool(request.POST.get("inputText"))

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireIssueChecking(user_info_id=user_info_obj,
                                                    date=update_date,
                                                    checkbox_1=update_checkbox_1,
                                                    checkbox_2=update_checkbox_2,
                                                    checkbox_3=update_checkbox_3,
                                                    checkbox_4=update_checkbox_4,
                                                    checkbox_5=update_checkbox_5,
                                                    checkbox_6=update_checkbox_6,
                                                    checkbox_7=update_checkbox_7,
                                                    checkbox_8=update_checkbox_8,
                                                    checkbox_9=update_checkbox_9,
                                                    checkbox_10=update_checkbox_10,
                                                    checkbox_11=update_checkbox_11,
                                                    checkbox_12=update_checkbox_12,
                                                    checkbox_13=update_checkbox_13,
                                                    checkbox_14=update_checkbox_14,
                                                    checkbox_15=update_checkbox_15,
                                                    checkbox_16=update_checkbox_16,
                                                    checkbox_17=update_checkbox_17,
                                                    checkbox_18=update_checkbox_18,
                                                    checkbox_19=update_checkbox_19,
                                                    checkbox_20=update_checkbox_20,
                                                    checkbox_21=update_checkbox_21,
                                                    checkbox_22=update_checkbox_22,
                                                    input_text=update_input_text)

        update_records.save()

        response_data = {"message": "updated questionnaire(issue checking) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(issue checking) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 이슈 확인 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_issue_checking_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireIssueChecking.objects.filter(user_info_id=user_info_obj,
                                                                      date=search_date).get()

        response_data = {"checkbox1": questionnaire_obj.checkbox_1,
                         "checkbox2": questionnaire_obj.checkbox_2,
                         "checkbox3": questionnaire_obj.checkbox_3,
                         "checkbox4": questionnaire_obj.checkbox_4,
                         "checkbox5": questionnaire_obj.checkbox_5,
                         "checkbox6": questionnaire_obj.checkbox_6,
                         "checkbox7": questionnaire_obj.checkbox_7,
                         "checkbox8": questionnaire_obj.checkbox_8,
                         "checkbox9": questionnaire_obj.checkbox_9,
                         "checkbox10": questionnaire_obj.checkbox_10,
                         "checkbox11": questionnaire_obj.checkbox_11,
                         "checkbox12": questionnaire_obj.checkbox_12,
                         "checkbox13": questionnaire_obj.checkbox_13,
                         "checkbox14": questionnaire_obj.checkbox_14,
                         "checkbox15": questionnaire_obj.checkbox_15,
                         "checkbox16": questionnaire_obj.checkbox_16,
                         "checkbox17": questionnaire_obj.checkbox_17,
                         "checkbox18": questionnaire_obj.checkbox_18,
                         "checkbox19": questionnaire_obj.checkbox_19,
                         "checkbox20": questionnaire_obj.checkbox_20,
                         "checkbox21": questionnaire_obj.checkbox_21,
                         "inputText": questionnaire_obj.input_text}

        return JsonResponse(response_data, status=200)

    except QuestionnaireIssueChecking.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireIssueChecking not found"}, status=402)

    except QuestionnaireIssueChecking.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireIssueChecking found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_self_diagnosis_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")
        update_result_10 = request.POST.get("result10")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireSelfDiagnosis(user_info_id=user_info_obj,
                                                    date=update_date,
                                                    result_1=update_result_1,
                                                    result_2=update_result_2,
                                                    result_3=update_result_3,
                                                    result_4=update_result_4,
                                                    result_5=update_result_5,
                                                    result_6=update_result_6,
                                                    result_7=update_result_7,
                                                    result_8=update_result_8,
                                                    result_9=update_result_9,
                                                    result_10=update_result_10)

        update_records.save()

        response_data = {"message": "updated questionnaire(self diagnosis) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(self diagnosis) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_self_diagnosis_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireSelfDiagnosis.objects.filter(user_info_id=user_info_obj,
                                                                      date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9,
                         "result10": questionnaire_obj.result_10}

        return JsonResponse(response_data, status=200)

    except QuestionnaireSelfDiagnosis.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireSelfDiagnosis not found"}, status=402)

    except QuestionnaireSelfDiagnosis.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireSelfDiagnosis found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_well_being_scale_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireWellBeingScale(user_info_id=user_info_obj,
                                                     date=update_date,
                                                     result_1=update_result_1,
                                                     result_2=update_result_2,
                                                     result_3=update_result_3,
                                                     result_4=update_result_4,
                                                     result_5=update_result_5,
                                                     result_6=update_result_6,
                                                     result_7=update_result_7)

        update_records.save()

        response_data = {"message": "updated questionnaire(well being scale) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(well being scale) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_well_being_scale_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireWellBeingScale.objects.filter(user_info_id=user_info_obj,
                                                                       date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7}

        return JsonResponse(response_data, status=200)

    except QuestionnaireWellBeingScale.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireWellBeingScale not found"}, status=402)

    except QuestionnaireWellBeingScale.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireWellBeingScale found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_phq9_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnairePHQ9(user_info_id=user_info_obj,
                                           date=update_date,
                                           result_1=update_result_1,
                                           result_2=update_result_2,
                                           result_3=update_result_3,
                                           result_4=update_result_4,
                                           result_5=update_result_5,
                                           result_6=update_result_6,
                                           result_7=update_result_7,
                                           result_8=update_result_8,
                                           result_9=update_result_9)

        update_records.save()

        response_data = {"message": "updated questionnaire(PHQ9) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(PHQ9) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_phq9_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnairePHQ9.objects.filter(user_info_id=user_info_obj, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9}

        return JsonResponse(response_data, status=200)

    except QuestionnairePHQ9.DoesNotExist:

        return JsonResponse({"message": "QuestionnairePHQ9 not found"}, status=402)

    except QuestionnairePHQ9.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnairePHQ9 found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_gad7_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireGAD7(user_info_id=user_info_obj,
                                           date=update_date,
                                           result_1=update_result_1,
                                           result_2=update_result_2,
                                           result_3=update_result_3,
                                           result_4=update_result_4,
                                           result_5=update_result_5,
                                           result_6=update_result_6,
                                           result_7=update_result_7)

        update_records.save()

        response_data = {"message": "updated questionnaire(GAD7) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(GAD7) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_gad7_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireGAD7.objects.filter(user_info_id=user_info_obj, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7}

        return JsonResponse(response_data, status=200)

    except QuestionnaireGAD7.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireGAD7 not found"}, status=402)

    except QuestionnaireGAD7.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireGAD7 found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_pss10_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")
        update_result_10 = request.POST.get("result10")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnairePSS10(user_info_id=user_info_obj,
                                            date=update_date,
                                            result_1=update_result_1,
                                            result_2=update_result_2,
                                            result_3=update_result_3,
                                            result_4=update_result_4,
                                            result_5=update_result_5,
                                            result_6=update_result_6,
                                            result_7=update_result_7,
                                            result_8=update_result_8,
                                            result_9=update_result_9,
                                            result_10=update_result_10)

        update_records.save()

        response_data = {"message": "updated questionnaire(PSS10) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(PSS10) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_pss10_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnairePSS10.objects.filter(user_info_id=user_info_obj, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9,
                         "result10": questionnaire_obj.result_10}

        return JsonResponse(response_data, status=200)

    except QuestionnairePSS10.DoesNotExist:

        return JsonResponse({"message": "QuestionnairePSS10 not found"}, status=402)

    except QuestionnairePSS10.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnairePSS10 found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_stress_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")
        update_result_10 = request.POST.get("result10")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireStress(user_info_id=user_info_obj,
                                             date=update_date,
                                             result_1=update_result_1,
                                             result_2=update_result_2,
                                             result_3=update_result_3,
                                             result_4=update_result_4,
                                             result_5=update_result_5,
                                             result_6=update_result_6,
                                             result_7=update_result_7,
                                             result_8=update_result_8,
                                             result_9=update_result_9,
                                             result_10=update_result_10)

        update_records.save()

        response_data = {"message": "updated questionnaire(stress) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(stress) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_stress_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireStress.objects.filter(user_info_id=user_info_obj, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9,
                         "result10": questionnaire_obj.result_10}

        return JsonResponse(response_data, status=200)

    except QuestionnaireStress.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireStress not found"}, status=402)

    except QuestionnaireStress.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireStress found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_exercise_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")
        update_result_10 = request.POST.get("result10")
        update_result_11 = request.POST.get("result11")
        update_result_12 = request.POST.get("result12")
        update_input_text = request.POST.get("inputText")

        exer_type_list = [request.POST.get("exerciseType1"),
                          request.POST.get("exerciseType2"),
                          request.POST.get("exerciseType3")]

        exer_type_instance_list = [ExerciseType.objects.get(type=exercise_type) for exercise_type in
                                   exer_type_list]

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireExercise(user_info_id=user_info_obj,
                                               date=update_date,
                                               result_1=update_result_1,
                                               result_2=update_result_2,
                                               result_3=update_result_3,
                                               result_4=update_result_4,
                                               result_5=update_result_5,
                                               result_6=update_result_6,
                                               result_7=update_result_7,
                                               result_8=update_result_8,
                                               result_9=update_result_9,
                                               result_10=update_result_10,
                                               result_11=update_result_11,
                                               result_12=update_result_12,
                                               result_13_input_text=update_input_text)

        update_records.save()

        update_records.result_13_exer_type.set(exer_type_instance_list)

        response_data = {"message": "updated questionnaire(exercise) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(exercise) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_exercise_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireExercise.objects.filter(user_info_id=user_info_obj, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9,
                         "result10": questionnaire_obj.result_10,
                         "result11": questionnaire_obj.result_11,
                         "result12": questionnaire_obj.result_12,
                         "exerciseType1": questionnaire_obj.result_13_exer_type[0].get('type'),
                         "exerciseType2": questionnaire_obj.result_13_exer_type[1].get('type'),
                         "exerciseType3": questionnaire_obj.result_13_exer_type[2].get('type'),
                         "inputText": questionnaire_obj.result_13_input_text}

        return JsonResponse(response_data, status=200)

    except QuestionnaireExercise.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireExercise not found"}, status=402)

    except QuestionnaireExercise.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireExercise found"}, status=403)

    except UserInfo.DoesNotExist:
        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_nutrition_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_result_1 = request.POST.get("result1")
        update_result_2 = request.POST.get("result2")
        update_result_3 = request.POST.get("result3")
        update_result_4 = request.POST.get("result4")
        update_result_5 = request.POST.get("result5")
        update_result_6 = request.POST.get("result6")
        update_result_7 = request.POST.get("result7")
        update_result_8 = request.POST.get("result8")
        update_result_9 = request.POST.get("result9")
        update_result_10 = request.POST.get("result10")
        update_result_11_snack_type = request.POST.get("snackType")
        update_result_11_consume_num = request.POST.get("consumeNum")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireNutrition(user_info_id=user_info_obj,
                                                date=update_date,
                                                result_1=update_result_1,
                                                result_2=update_result_2,
                                                result_3=update_result_3,
                                                result_4=update_result_4,
                                                result_5=update_result_5,
                                                result_6=update_result_6,
                                                result_7=update_result_7,
                                                result_8=update_result_8,
                                                result_9=update_result_9,
                                                result_10=update_result_10,
                                                result_11_snack_type=update_result_11_snack_type,
                                                result_11_consume_num=update_result_11_consume_num)

        update_records.save()

        response_data = {"message": "updated questionnaire(nutrition) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(nutrition) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_nutrition_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireNutrition.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": questionnaire_obj.result_1,
                         "result2": questionnaire_obj.result_2,
                         "result3": questionnaire_obj.result_3,
                         "result4": questionnaire_obj.result_4,
                         "result5": questionnaire_obj.result_5,
                         "result6": questionnaire_obj.result_6,
                         "result7": questionnaire_obj.result_7,
                         "result8": questionnaire_obj.result_8,
                         "result9": questionnaire_obj.result_9,
                         "result10": questionnaire_obj.result_10,
                         "snackType": questionnaire_obj.result_11_snack_type,
                         "consumeNum": questionnaire_obj.result_11_consume_num}

        return JsonResponse(response_data, status=200)

    except QuestionnaireNutrition.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireNutrition not found"}, status=402)

    except QuestionnaireNutrition.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireNutrition found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_smoking_drinking_survey(request):
    try:
        update_id = request.POST.get("user_id")
        update_date = request.POST.get("date")
        update_smoking_result_1 = request.POST.get("smoking_result1")
        update_smoking_result_2 = request.POST.get("smoking_result2")
        update_smoking_result_3 = request.POST.get("smoking_result3")
        update_smoking_result_4 = request.POST.get("smoking_result4")
        update_smoking_result_5 = request.POST.get("smoking_result5")
        update_smoking_result_6 = request.POST.get("smoking_result6")
        update_smoking_result_7 = request.POST.get("smoking_result7")
        update_smoking_result_8 = request.POST.get("smoking_result8")
        update_smoking_result_9 = request.POST.get("smoking_result9")
        update_drinking_result_1 = request.POST.get("drinking_result1")
        update_drinking_result_2 = request.POST.get("drinking_result2")
        update_drinking_result_3 = request.POST.get("drinking_result3")
        update_drinking_result_4 = request.POST.get("drinking_result4")
        update_drinking_result_5 = request.POST.get("drinking_result5")
        update_drinking_result_6 = request.POST.get("drinking_result6")
        update_drinking_result_7 = request.POST.get("drinking_result7")
        update_drinking_result_8 = request.POST.get("drinking_result8")
        update_drinking_result_9 = request.POST.get("drinking_result9")
        update_drinking_result_10 = request.POST.get("drinking_result10")

        if not update_id or not update_date:
            return JsonResponse({"message": "update_id and update_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=update_id)

        update_records = QuestionnaireSmokingDrinking(user_info_id=user_info_obj,
                                                      date=update_date,
                                                      smoking_result_1=update_smoking_result_1,
                                                      smoking_result_2=update_smoking_result_2,
                                                      smoking_result_3=update_smoking_result_3,
                                                      smoking_result_4=update_smoking_result_4,
                                                      smoking_result_5=update_smoking_result_5,
                                                      smoking_result_6=update_smoking_result_6,
                                                      smoking_result_7=update_smoking_result_7,
                                                      smoking_result_8=update_smoking_result_8,
                                                      smoking_result_9=update_smoking_result_9,
                                                      drinking_result_1=update_drinking_result_1,
                                                      drinking_result_2=update_drinking_result_2,
                                                      drinking_result_3=update_drinking_result_3,
                                                      drinking_result_4=update_drinking_result_4,
                                                      drinking_result_5=update_drinking_result_5,
                                                      drinking_result_6=update_drinking_result_6,
                                                      drinking_result_7=update_drinking_result_7,
                                                      drinking_result_8=update_drinking_result_8,
                                                      drinking_result_9=update_drinking_result_9,
                                                      drinking_result_10=update_drinking_result_10)

        update_records.save()

        response_data = {"message": "updated questionnaire(smoking & drinking) records successfully"}
        return JsonResponse(response_data, status=200)

    except UserInfo.DoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(smoking & drinking) records"}
        return JsonResponse({"message": "UserInfo not found"}, status=402)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_smoking_drinking_survey(request):
    try:
        search_id = request.POST.get("user_id")
        search_date = request.POST.get("date")

        if not search_id or not search_date:
            return JsonResponse({"message": "search_id and search_date are required"}, status=401)

        user_info_obj = UserInfo.objects.get(user_id=search_id)

        questionnaire_obj = QuestionnaireSmokingDrinking.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"smoking_result1": questionnaire_obj.smoking_result_1,
                         "smoking_result2": questionnaire_obj.smoking_result_2,
                         "smoking_result3": questionnaire_obj.smoking_result_3,
                         "smoking_result4": questionnaire_obj.smoking_result_4,
                         "smoking_result5": questionnaire_obj.smoking_result_5,
                         "smoking_result6": questionnaire_obj.smoking_result_6,
                         "smoking_result7": questionnaire_obj.smoking_result_7,
                         "smoking_result8": questionnaire_obj.smoking_result_8,
                         "smoking_result9": questionnaire_obj.smoking_result_9,
                         "drinking_result1": questionnaire_obj.drinking_result_1,
                         "drinking_result2": questionnaire_obj.drinking_result_2,
                         "drinking_result3": questionnaire_obj.drinking_result_3,
                         "drinking_result4": questionnaire_obj.drinking_result_4,
                         "drinking_result5": questionnaire_obj.drinking_result_5,
                         "drinking_result6": questionnaire_obj.drinking_result_6,
                         "drinking_result7": questionnaire_obj.drinking_result_7,
                         "drinking_result8": questionnaire_obj.drinking_result_8,
                         "drinking_result9": questionnaire_obj.drinking_result_9,
                         "drinking_result10": questionnaire_obj.drinking_result_10}

        return JsonResponse(response_data, status=200)

    except QuestionnaireSmokingDrinking.DoesNotExist:

        return JsonResponse({"message": "QuestionnaireSmokingDrinking not found"}, status=402)

    except QuestionnaireSmokingDrinking.MultipleObjectsReturned:

        return JsonResponse({"message": "Multiple QuestionnaireSmokingDrinking found"}, status=403)

    except UserInfo.DoesNotExist:

        return JsonResponse({"message": "UserInfo not found"}, status=404)
