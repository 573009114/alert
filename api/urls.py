from django.conf.urls import include, url
from django.urls import path,re_path
from api import notice,event,prometheus,log_app,log_rules
from rest_framework.schemas import get_schema_view
#from rest_framework.authtoken import views

schema_view = get_schema_view(title='alert system API',version='v1.0')

urlpatterns = [
    path('notice/',notice.notice_list),
    re_path('notice/(?P<id>\d+)/$', notice.notice_detail),
]

urlpatterns += [
    path('event/',event.event_list),
    re_path('event/(?P<id>\d+)/$', event.event_detail),
]

urlpatterns += [
    path('prometheus/',prometheus.prometheus_list),
    re_path('prometheus/(?P<id>\d+)/$', prometheus.prometheus_detail),
]

urlpatterns += [
    path('app/',log_app.app_list),
    re_path('app/(?P<id>\d+)/$', log_app.app_detail),
]

urlpatterns += [
    path('rules/',log_rules.rules_list),
    re_path('rules/(?P<id>\d+)/$', log_rules.rules_detail),
]


urlpatterns += [
    path('',schema_view),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#    path('api-token-auth/', views.obtain_auth_token),
]
