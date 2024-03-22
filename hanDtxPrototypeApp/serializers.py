from rest_framework import serializers

from .models import UserInfo
from .models import LoginInfo
from .models import EmotionDiaryRecords
from .models import QuestionnaireIssueChecking
from .models import QuestionnaireSelfDiagnosis
from .models import QuestionnaireWellBeingScale
from .models import QuestionnairePHQ9
from .models import QuestionnaireGAD7
from .models import QuestionnairePSS10
from .models import ExerciseType
from .models import QuestionnaireExercise
from .models import QuestionnaireExerciseExerciseType
from .models import QuestionnaireSmokingDrinking
from .models import QuestionnaireStress
from .models import QuestionnaireNutrition


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = '__all__'


class QuestionnaireExerciseExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireExerciseExerciseType
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class LoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginInfo
        fields = '__all__'


class EmotionDiaryRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionDiaryRecords
        fields = '__all__'


class QuestionnaireIssueCheckingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireIssueChecking
        fields = '__all__'


class QuestionnaireSelfDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireSelfDiagnosis
        fields = '__all__'


class QuestionnaireWellBeingScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireWellBeingScale
        fields = '_all_'


class QuestionnairePHQ9Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnairePHQ9
        fields = '__all__'


class QuestionnaireGAD7Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireGAD7
        fields = '__all__'


class QuestionnairePSS10Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnairePSS10
        fields = '__all__'


class QuestionnaireExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireExercise
        fields = '__all__'


class QuestionnaireSmokingDrinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireSmokingDrinking
        fields = '__all__'


class QuestionnaireStressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireStress
        fields = '__all__'


class QuestionnaireNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireNutrition
        fields = '__all__'
