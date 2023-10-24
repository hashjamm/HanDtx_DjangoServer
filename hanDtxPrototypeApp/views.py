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
            return JsonResponse(response_data, status=200)
        else:
            response_data = {"message": "패스워드가 일치하지 않습니다.", "code": 2}
            return JsonResponse(response_data, status=400)

    except ObjectDoesNotExist:
        response_data = {"message": "등록되지 않은 사용자 계정입니다.", "code": 3}
        return JsonResponse(response_data, status=400)
