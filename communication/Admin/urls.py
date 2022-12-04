
from django.urls import path
import Admin.views
urlpatterns = [
    path('adminhome/', Admin.views.adminhome),
    path('', Admin.views.index,name='index'),
    path('gallery/', Admin.views.gallery, name='gallery'),
    path('service/', Admin.views.service, name='service'),
    path('contact/', Admin.views.contact, name='contact'),
    path('login/', Admin.views.login, name='login'),
    path('major/', Admin.views.addmajor, name='major'),
    path('operations/', Admin.views.operations, name='operations'),
    path('viewcitizen/', Admin.views.viewcitizen, name='viewcitizen'),
    path('approve/<id>', Admin.views.approve, name='approve'),
    path('reject/<id>', Admin.views.reject, name='reject'),
    path('viewcomplaint/', Admin.views.viewcomplaint, name='viewcomplaint'),
    path('accept/<id>', Admin.views.accept, name='accept'),
    path('reject1/<id>', Admin.views.reject1, name='reject1'),
    path('viewrequest/', Admin.views.viewrequest, name='viewrequest'),
    path('acceptre/<id>', Admin.views.acceptre, name='acceptre'),
    path('rejectre1/<id>', Admin.views.rejectre1, name='rejectre1'),

]