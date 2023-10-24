from rest_framework import serializers

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


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo


class LoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginInfo


class EmotionDiaryRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionDiaryRecords


class QuestionnaireIssueCheckingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireIssueChecking


class QuestionnaireSelfDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireSelfDiagnosis


class QuestionnaireWellBeingScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireWellBeingScale


class QuestionnairePHQ9Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnairePHQ9


class QuestionnaireGAD7Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireGAD7


class QuestionnairePSS10Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnairePSS10


class QuestionnaireExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireExercise


class QuestionnaireSmokingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireSmoking


class QuestionnaireDrinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireDrinking


class QuestionnaireStressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireStress


class QuestionnaireNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireNutrition
