import requests
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
import json

from .models import UserInfo
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
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_pw = data["user_pw"]

        obj = UserInfo.objects.get(user_id=search_id)

        if search_pw == obj.user_pw:
            response_data = {"message": "로그인 성공"}

            # 로그인 성공 시 LoginInfo 모델에 로그인 기록 저장
            login_info = LoginInfo(user_info_id=obj.user_id)  # user_info_id에 user_id 값을 저장
            login_info.save()

            return JsonResponse(response_data, status=200)
        else:
            response_data = {"message": "패스워드가 일치하지 않습니다."}
            return JsonResponse(response_data, status=201)

    except ObjectDoesNotExist:

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 감정 다이어리 정보 전체를 반환
@csrf_exempt
@require_POST
def get_emotion_diary_records(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = EmotionDiaryRecords.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"score1": obj.score_type_1,
                         "inputText1": obj.input_text_type_1,
                         "score2": obj.score_type_2,
                         "inputText2": obj.input_text_type_2,
                         "score3": obj.score_type_3,
                         "inputText3": obj.input_text_type_3}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_emotion_diary_records(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_score_type_1 = data["score1"]
        update_input_text_type_1 = data["inputText1"]
        update_score_type_2 = data["score2"]
        update_input_text_type_2 = data["inputText2"]
        update_score_type_3 = data["score3"]
        update_input_text_type_3 = data["inputText3"]

        update_records = EmotionDiaryRecords(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_issue_checking_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_checkbox_1 = data["checkbox1"]
        update_checkbox_2 = data["checkbox2"]
        update_checkbox_3 = data["checkbox3"]
        update_checkbox_4 = data["checkbox4"]
        update_checkbox_5 = data["checkbox5"]
        update_checkbox_6 = data["checkbox6"]
        update_checkbox_7 = data["checkbox7"]
        update_checkbox_8 = data["checkbox8"]
        update_checkbox_9 = data["checkbox9"]
        update_checkbox_10 = data["checkbox10"]
        update_checkbox_11 = data["checkbox11"]
        update_checkbox_12 = data["checkbox12"]
        update_checkbox_13 = data["checkbox13"]
        update_checkbox_14 = data["checkbox14"]
        update_checkbox_15 = data["checkbox15"]
        update_checkbox_16 = data["checkbox16"]
        update_checkbox_17 = data["checkbox17"]
        update_checkbox_18 = data["checkbox18"]
        update_checkbox_19 = data["checkbox19"]
        update_checkbox_20 = data["checkbox20"]
        update_checkbox_21 = data["checkbox21"]
        update_checkbox_22 = data["checkbox22"]
        update_input_text = data["inputText"]

        update_records = QuestionnaireIssueChecking(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(issue checking) records"}
        return JsonResponse([], status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 이슈 확인 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_issue_checking_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireIssueChecking.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"checkbox1": obj.checkbox_1,
                         "checkbox2": obj.checkbox_2,
                         "checkbox3": obj.checkbox_3,
                         "checkbox4": obj.checkbox_4,
                         "checkbox5": obj.checkbox_5,
                         "checkbox6": obj.checkbox_6,
                         "checkbox7": obj.checkbox_7,
                         "checkbox8": obj.checkbox_8,
                         "checkbox9": obj.checkbox_9,
                         "checkbox10": obj.checkbox_10,
                         "checkbox11": obj.checkbox_11,
                         "checkbox12": obj.checkbox_12,
                         "checkbox13": obj.checkbox_13,
                         "checkbox14": obj.checkbox_14,
                         "checkbox15": obj.checkbox_15,
                         "checkbox16": obj.checkbox_16,
                         "checkbox17": obj.checkbox_17,
                         "checkbox18": obj.checkbox_18,
                         "checkbox19": obj.checkbox_19,
                         "checkbox20": obj.checkbox_20,
                         "checkbox21": obj.checkbox_21,
                         "inputText": obj.input_text}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"checkbox1": None,
        #                  "checkbox2": None,
        #                  "checkbox3": None,
        #                  "checkbox4": None,
        #                  "checkbox5": None,
        #                  "checkbox6": None,
        #                  "checkbox7": None,
        #                  "checkbox8": None,
        #                  "checkbox9": None,
        #                  "checkbox10": None,
        #                  "checkbox11": None,
        #                  "checkbox12": None,
        #                  "checkbox13": None,
        #                  "checkbox14": None,
        #                  "checkbox15": None,
        #                  "checkbox16": None,
        #                  "checkbox17": None,
        #                  "checkbox18": None,
        #                  "checkbox19": None,
        #                  "checkbox20": None,
        #                  "checkbox21": None,
        #                  "inputText": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_self_diagnosis_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]
        update_result_10 = data["result10"]

        update_records = QuestionnaireSelfDiagnosis(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(self diagnosis) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_self_diagnosis_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireSelfDiagnosis.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9,
                         "result10": obj.result_10}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None,
        #                  "result10": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_well_being_scale_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]

        update_records = QuestionnaireWellBeingScale(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(well being scale) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_well_being_scale_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireWellBeingScale.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_phq9_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]

        update_records = QuestionnairePHQ9(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(PHQ9) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_phq9_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnairePHQ9.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_gad7_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]

        update_records = QuestionnaireGAD7(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(GAD7) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_gad7_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireGAD7.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_pss10_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]
        update_result_10 = data["result10"]

        update_records = QuestionnairePSS10(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(PSS10) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_pss10_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnairePSS10.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9,
                         "result10": obj.result_10}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None,
        #                  "result10": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_stress_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]
        update_result_10 = data["result10"]

        update_records = QuestionnaireStress(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(stress) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_stress_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireStress.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9,
                         "result10": obj.result_10}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None,
        #                  "result10": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_exercise_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]
        update_result_10 = data["result10"]
        update_result_11 = data["result11"]
        update_result_12 = data["result12"]
        update_input_text = data["inputText"]

        exer_type_list = [data["exerciseType1"], data["exerciseType2"], data["exerciseType3"]]

        exer_type_instance_list = [ExerciseType.objects.get(type=exercise_type) for exercise_type in
                                   exer_type_list]

        update_records = QuestionnaireExercise(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(exercise) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_exercise_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireExercise.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9,
                         "result10": obj.result_10,
                         "result11": obj.result_11,
                         "result12": obj.result_12,
                         "exerciseType1": obj.result_13_exer_type[0],
                         "exerciseType2": obj.result_13_exer_type[1],
                         "exerciseType3": obj.result_13_exer_type[2],
                         "inputText": obj.result_13_input_text}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None,
        #                  "result10": None,
        #                  "result11": None,
        #                  "result12": None,
        #                  "exerciseType1": None,
        #                  "exerciseType2": None,
        #                  "exerciseType3": None,
        #                  "inputText": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_nutrition_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_result_1 = data["result1"]
        update_result_2 = data["result2"]
        update_result_3 = data["result3"]
        update_result_4 = data["result4"]
        update_result_5 = data["result5"]
        update_result_6 = data["result6"]
        update_result_7 = data["result7"]
        update_result_8 = data["result8"]
        update_result_9 = data["result9"]
        update_result_10 = data["result10"]
        update_result_11_snack_type = data["snackType"]
        update_result_11_consume_num = data["consumeNum"]

        update_records = QuestionnaireNutrition(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(nutrition) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_nutrition_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireNutrition.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"result1": obj.result_1,
                         "result2": obj.result_2,
                         "result3": obj.result_3,
                         "result4": obj.result_4,
                         "result5": obj.result_5,
                         "result6": obj.result_6,
                         "result7": obj.result_7,
                         "result8": obj.result_8,
                         "result9": obj.result_9,
                         "result10": obj.result_10,
                         "snackType": obj.result_11_snack_type,
                         "consumeNum": obj.result_11_consume_num}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"result1": None,
        #                  "result2": None,
        #                  "result3": None,
        #                  "result4": None,
        #                  "result5": None,
        #                  "result6": None,
        #                  "result7": None,
        #                  "result8": None,
        #                  "result9": None,
        #                  "result10": None,
        #                  "snackType": None,
        #                  "consumeNum": None}

        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디, 날짜, 데이터 내용을 전달 받으면 해당 내용을 save 하는 함수
@csrf_exempt
@require_POST
def update_smoking_drinking_survey(request):
    try:
        data = JSONParser().parse(request)
        update_id = data["user_id"]
        update_date = data["date"]
        update_smoking_result_1 = data["smoking_result1"]
        update_smoking_result_2 = data["smoking_result2"]
        update_smoking_result_3 = data["smoking_result3"]
        update_smoking_result_4 = data["smoking_result4"]
        update_smoking_result_5 = data["smoking_result5"]
        update_smoking_result_6 = data["smoking_result6"]
        update_smoking_result_7 = data["smoking_result7"]
        update_smoking_result_8 = data["smoking_result8"]
        update_smoking_result_9 = data["smoking_result9"]
        update_drinking_result_1 = data["drinking_result1"]
        update_drinking_result_2 = data["drinking_result2"]
        update_drinking_result_3 = data["drinking_result3"]
        update_drinking_result_4 = data["drinking_result4"]
        update_drinking_result_5 = data["drinking_result5"]
        update_drinking_result_6 = data["drinking_result6"]
        update_drinking_result_7 = data["drinking_result7"]
        update_drinking_result_8 = data["drinking_result8"]
        update_drinking_result_9 = data["drinking_result9"]
        update_drinking_result_10 = data["drinking_result10"]

        update_records = QuestionnaireSmokingDrinking(user_info_id=update_id,
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

    except ObjectDoesNotExist:

        # response_data = {"message": "Unexpected error during updating questionnaire(smoking & drinking) records"}
        return JsonResponse({}, status=400)


# POST 요청으로 유저의 아이디와 날짜를 전달받으면, 해당 아이디와 날짜에 해당하는 설문 응답 정보 전체를 반환
@csrf_exempt
@require_POST
def get_smoking_drinking_survey(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        search_date = data["date"]

        obj = QuestionnaireSmokingDrinking.objects.filter(user_info_id=search_id, date=search_date).get()

        response_data = {"smoking_result1": obj.smoking_result_1,
                         "smoking_result2": obj.smoking_result_2,
                         "smoking_result3": obj.smoking_result_3,
                         "smoking_result4": obj.smoking_result_4,
                         "smoking_result5": obj.smoking_result_5,
                         "smoking_result6": obj.smoking_result_6,
                         "smoking_result7": obj.smoking_result_7,
                         "smoking_result8": obj.smoking_result_8,
                         "smoking_result9": obj.smoking_result_9,
                         "drinking_result1": obj.drinking_result_1,
                         "drinking_result2": obj.drinking_result_2,
                         "drinking_result3": obj.drinking_result_3,
                         "drinking_result4": obj.drinking_result_4,
                         "drinking_result5": obj.drinking_result_5,
                         "drinking_result6": obj.drinking_result_6,
                         "drinking_result7": obj.drinking_result_7,
                         "drinking_result8": obj.drinking_result_8,
                         "drinking_result9": obj.drinking_result_9,
                         "drinking_result10": obj.drinking_result_10}

        return JsonResponse(response_data, status=200)

    except ObjectDoesNotExist:

        # response_data = {"smoking_result1": None,
        #                  "smoking_result2": None,
        #                  "smoking_result3": None,
        #                  "smoking_result4": None,
        #                  "smoking_result5": None,
        #                  "smoking_result6": None,
        #                  "smoking_result7": None,
        #                  "smoking_result8": None,
        #                  "smoking_result9": None,
        #                  "drinking_result1": None,
        #                  "drinking_result2": None,
        #                  "drinking_result3": None,
        #                  "drinking_result4": None,
        #                  "drinking_result5": None,
        #                  "drinking_result6": None,
        #                  "drinking_result7": None,
        #                  "drinking_result8": None,
        #                  "drinking_result9": None,
        #                  "drinking_result10": None}

        return JsonResponse({}, status=400)
