from django.urls import path
import Citizen.views

urlpatterns = [
    path('citizenhome/',Citizen.views.citizenhome,name='citizenhome'),
    path('citizenreg/', Citizen.views.citizenreg, name='citizenreg'),
    path('complaints/', Citizen.views.complaints, name='complaints'),
    path('viewcstatus/', Citizen.views.viewcstatus, name='viewcstatus'),
    path('request/', Citizen.views.requests, name='request'),
    path('viewrstatus/', Citizen.views.viewrstatus, name='viewrstatus'),

]