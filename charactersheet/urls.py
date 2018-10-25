from django.conf.urls import url
from charactersheet.views.character_general_info_view import CharacterGeneralInfoView

urlpatterns = [
    url(r'^new/$', CharacterGeneralInfoView.as_view()),
]
