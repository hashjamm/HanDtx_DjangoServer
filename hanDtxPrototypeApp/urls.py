"""
URL configuration for hanDtxPrototype project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from hanDtxPrototypeApp import views

from . import views as test_views

app_name = 'hanDtxPrototypeApp'

urlpatterns = [
    path("home/", test_views.home, name="home"),
    path("app_login/", views.login),
    path("app_get_emotion_diary_records/", views.EmotionDiaryRecordsAPIView.as_view(), name='get'),
    path("app_get_emotion_diary_records_monthly", views.EmotionDiaryRecordsAPIView.as_view(), name='another_get'),
    path("app_update_emotion_diary_records/", views.EmotionDiaryRecordsAPIView.as_view(), name='post'),
    path("app_get_issue_checking_survey/", views.get_issue_checking_survey),
    path("app_update_issue_checking_survey/", views.update_issue_checking_survey),
    path("app_get_self_diagnosis_survey/", views.get_self_diagnosis_survey),
    path("app_update_self_diagnosis_survey/", views.update_self_diagnosis_survey),
    path("app_get_well_being_scale_survey/", views.get_well_being_scale_survey),
    path("app_update_well_being_scale_survey/", views.update_well_being_scale_survey),
    path("app_get_phq9_survey/", views.get_phq9_survey),
    path("app_update_phq9_survey/", views.update_phq9_survey),
    path("app_get_gad7_survey/", views.get_gad7_survey),
    path("app_update_gad7_survey/", views.update_gad7_survey),
    path("app_get_pss10_survey/", views.get_pss10_survey),
    path("app_update_pss10_survey/", views.update_pss10_survey),
    path("app_get_stress_survey/", views.get_stress_survey),
    path("app_update_stress_survey/", views.update_stress_survey),
    path("app_get_exercise_survey/", views.get_exercise_survey),
    path("app_update_exercise_survey/", views.update_exercise_survey),
    path("app_get_nutrition_survey/", views.get_nutrition_survey),
    path("app_update_nutrition_survey/", views.update_nutrition_survey),
    path("app_get_smoking_drinking_survey/", views.get_smoking_drinking_survey),
    path("app_update_smoking_drinking_survey/", views.update_smoking_drinking_survey),
    path("app_get_all_survey_checked/", views.get_all_survey_checked)
]
