from django.conf.urls import url
from views import index, process, result, goback
app_name="survey_form"
urlpatterns = [
    url(r'^$',index, name="survey_form_index"),
    url(r'^process$', process,  name="survey_form_process"),
    url(r'^result$', result, name="survey_form_result"),
    url(r'^goback$', goback, name="survey_form_goback")
]
