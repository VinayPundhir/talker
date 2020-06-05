from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
urlpatterns=[
     url(r'^all_users/$',views.all_users,name='all_users'),
    url(r'^friends/$',views.friends,name='friends'),
      url(r'^requests/$',views.requests,name="requests"),
    url(r'^accept_request/(\w+)$',views.accept_request,name='accept_request'),
      url(r'^decline_request/(\w+)$',views.decline_request,name='decline_request'),
url(r'^$',views.start,name='start'),
url(r'^chat_size/(\w+)$',views.chat_size,name='chat_size'),
url(r'^video_call/(\w+)$',views.video_call,name='video_call'),
url(r'^public/$',TemplateView.as_view(template_name='public_profile.html')),

url(r'^logout/$',views.logout,name='logout'),
url(r'^json/(\w+)$',views.json,name='json'),
url(r'^sinup/$',TemplateView.as_view(template_name='sinup.html')),
    url(r'^sinup_process/$',views.sinup_process,name='sinup_process'),
   url(r'^process/$',views.process,name='process'),
 url(r'^process_recieved/$',views.process_recieved,name='process_recieved'),
  url(r'^login_process/$',views.login_process,name='login_process'),
 url(r'^send_request/(\w+)/$',views.send_request,name='send_request'),
url(r'^chatting/(\w+)$',views.chatting,name='chatting'),
url(r'^chatting_process/(\w+)$',views.chatting_process,name='chatting_process')
  ]
