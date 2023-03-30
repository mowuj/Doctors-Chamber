from django.urls import path
from .views import *
urlpatterns = [
    # Admin 
    path('', adminHome, name='home'),
    path('doctor-login', user_login, name='doctor-login'),
    path('logout', user_logout, name='logout'), 
    # path('banner', banner, name='banner'), 
    path('doctor-home', doctorHome, name='doctor-home'),
    path('def', my_view2, name='def'),
    # path('doctor-home',  doctorHome, name='doctor-home'),
    path('add-images', addRelatedImages, name='add-images'),
    path('add-announcement', addAnnouncement, name='add-announcement'),
    path('add-department', addDepartment, name='add-department'),
    path('add-lab', addLab, name='add-lab'),
    path('all-lab', allLab, name='all-lab'),
    path('edit-lab/<int:id>', editLab, name='edit-lab'),
    path('department', department, name='department'),
    path('edit-department/<int:id>', editDepartment, name='edit-department'),
    path('add-doctor', create_doctor, name='add-doctor'),
    path('all-doctor', allDoctors, name='all-doctor'),
    path('doctor-detail/<int:id>', doctorDetail, name='doctor-detail'),
    path('doctor-profile', doctorProfile, name='doctor-profile'),
    path('doctor-profile-edit/<int:id>',editDoctorProfile, name='doctor-profile-edit'),
    # Staff 
    path('add-staff', create_staff, name='add-staff'),
    path('add-lab-assistant', addLabAssistant, name='add-lab-assistant'),
    path('all-lab-assistant', allLabAssistant, name='all-lab-assistant'),
    path('assistant-detail/<int:id>', assistantDetail, name='assistant-detail'),
    path('assistant-profile>', assistantProfile, name='assistant-profile'),
    path('assistant-profile-edit/<int:id>', editAssistantProfile, name='assistant-profile-edit'),
    path('lab-home', labHome, name='lab-home'),
    # Staff 

    path('staff-home',  staffHome, name='staff-home'),
    path('all-staff',  allStaff, name='all-staff'),
    path('staff-detail/<int:id>', staffDetail, name='staff-detail'),
    path('staff-profile', staffProfile, name='staff-profile'),
    path('staff-profile-edit/<int:id>',editStaffProfile, name='staff-profile-edit'),
    # serial 
    path('take-serial',  takeSerial, name='take-serial'),
    path('today-serial',  todaySerial, name='today-serial'),
    path('move-serial/<int:id>/<sts>',  moveSerial, name='move-serial'),
    path('delete-serial/<int:id>',  deleteSerial, name='delete-serial'),

    path('patient/<int:id>',  patient, name='patient'),
    path('delete-medicine/<int:id>',  deleteMedicine, name='delete-medicine'),
    path('test/<int:id>',  goForTest, name='test'),
    path('tests/<int:id>/<sts>', tests, name='tests'),
    # path('ttest/<int:pk>', ttest, name='ttest'),
    path('pending-test', PendingTest, name='pending-test'),
    path('report/<int:id>', testReportAdd, name='report'),
    path('testReport/<int:id>', testReport, name='testReport'),
]
