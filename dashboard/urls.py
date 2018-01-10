from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.mainboard, name='mainboard'),
    path('report_list', views.report_list, name='report_list'),
    path('report/<int:report_id>', views.report_detail, name='report_detail'),
    path('report/new/', views.new_report, name='new_report'),
    path('report/edit/<int:report_id>', views.edit_report, name='edit_report'),
    path('associate/new/', views.new_associate, name='new_associate'),
    path('associate/edit/<int:associate_id>', views.edit_associate, name='edit_associate'),
    path('associate_list', views.associate_list, name='associate_list'),
    path('associate/<int:associate_id>', views.associate_detail, name='associate_detail'),
]
