from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from api.serializer import *
from accounts.models import *
from exam_online.models import *
# Create your views here.

"""
5
979
10
1261
"""
# -------------------------------------------------------------------------------
# ---------------------------------Accounts--------------------------------------
# -------------------------------------------------------------------------------


class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = (UserRateThrottle,)


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

# -------------------------------------------------------------------------------
# ---------------------------------ExamOnline------------------------------------
# -------------------------------------------------------------------------------


class QuestionInfoViewSet(viewsets.ModelViewSet):
    queryset = QuestionInfo.objects.all()
    serializer_class = QuestionInfoSerializer


class OptionInfoViewSet(viewsets.ModelViewSet):
    queryset = OptionInfo.objects.all()
    serializer_class = OptionInfoSerializer


class ExaminationInfoViewSet(viewsets.ModelViewSet):
    queryset = ExaminationInfo.objects.all()
    serializer_class = ExaminationInfoSerializer


class ExaminationInfoQuestionInfoProfileViewSet(viewsets.ModelViewSet):
    queryset = ExaminationInfoQuestionInfoProfile.objects.all()
    serializer_class = ExaminationInfoQuestionInfoProfileSerializer
