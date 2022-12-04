from django.urls import path
import Officer.views

urlpatterns = [
    path('officerhome/', Officer.views.officerhome, name='officerhome'),
    path('viewoperationofficer/', Officer.views.viewoperationofficer, name='viewoperationofficer'),
    path('viewmajormsg/',Officer.views.viewmajormsg,name='viewmajormsg'),
    path('viewmajormsg1/<id>', Officer.views.viewmajormsg1, name='viewmajormsg1'),
    path('staffmsgdecrypt/', Officer.views.staffmsgdecrypt, name='staffmsgdecrypt'),
    path('staffmsg1/', Officer.views.staffmsg1, name='staffmsg1'),
    path('staffs/', Officer.views.staffs),
    path('encstaffmsg1/', Officer.views.encstaffmsg1, name='encstaffmsg1')

]

