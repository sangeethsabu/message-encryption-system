from django.urls import path
import Major.views

urlpatterns = [
    path('majorhome/', Major.views.majorhome, name='majorhome'),
    path('officers/', Major.views.officers, name='officers'),
    path('viewoperation/', Major.views.viewoperation, name='viewoperation'),
    path('team/', Major.views.teams, name='team'),
    path('staffmsg/', Major.views.staffmsg, name='staffmsg'),
    path('staffs/', Major.views.staffs),
    path('encstaff/', Major.views.encstaffmsg, name='encstaff'),
    path('viewofficermsg/',Major.views.viewofficermsg,name='viewofficermsg'),
    path('viewofficermsg1/<id>', Major.views.viewofficermsg1, name='viewofficermsg1'),
    path('staffmsgdecrypt1/', Major.views.staffmsgdecrypt1, name='staffmsgdecrypt1'),
]
