from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST

from .models import UserInfo
from .models import LoginInfo
from .models import EmotionDiaryRecords
from .models import QuestionnaireSmoking
from .models import QuestionnaireStress
from .models import QuestionnaireDrinking
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
from .serializers import QuestionnaireSmokingSerializer
from .serializers import QuestionnaireStressSerializer
from .serializers import QuestionnaireDrinkingSerializer
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
def login(request):
    try:
        data = JSONParser().parse(request)
        search_id = data["user_id"]
        obj = UserInfo.objects.get(user_id=search_id)

        if data["user_pw"] == obj.user_pw:
            response_data = {"message": "로그인 성공", "code": 1}

            # 로그인 성공 시 LoginInfo 모델에 로그인 기록 저장
            login_info = LoginInfo(user_info_id=obj.user_id)  # user_info_id에 user_id 값을 저장
            login_info.save()

            return JsonResponse(response_data, status=200)
        else:
            response_data = {"message": "패스워드가 일치하지 않습니다.", "code": 2}
            return JsonResponse(response_data, status=400)

    except ObjectDoesNotExist:
        response_data = {"message": "등록되지 않은 사용자 계정입니다.", "code": 3}
        return JsonResponse(response_data, status=400)


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
        response_data = {"score1": None,
                         "inputText1": None,
                         "score2": None,
                         "inputText2": None,
                         "score3": None,
                         "inputText3": None}

        return JsonResponse(response_data, status=400)


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

        response_data = {"message": "Unexpected error during updating emotion diary records"}
        return JsonResponse(response_data, status=400)
