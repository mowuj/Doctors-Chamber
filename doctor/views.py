from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and Doctor.objects.filter(user=user).exists():
                login(request, user)
                return redirect('doctor-home')
            elif user is not None and Staff.objects.filter(user=user).exists():
                login(request, user)
                return redirect('staff-home')
            
            elif user is not None and LabAssistant.objects.filter(user=user).exists():
                login(request, user)
                return redirect('lab-home')
            elif user is not None and Admin.objects.filter(user=user).exists():
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def doctorHome(request):
    doctor=Doctor.objects.all()
    announcement=Announcement.objects.all()
    images=RelatedImages.objects.all()
    return render(request, 'doctor/doctorHome.html', { 'doctor': doctor, 'announcement': announcement, 'images': images})

def my_view2(request):
    doctor=Doctor.objects.all()
    announcement=Announcement.objects.all()
    images=RelatedImages.objects.all()
    return render(request, 'main2.html', { 'doctor': doctor, 'announcement': announcement, 'images': images})


def user_logout(request):
    logout(request)
    return redirect('doctor-login')

# def banner(request):
#     h='Habib'
#     doctor = Doctor.objects.all()
#     staff = Staff.objects.all()
#     dept = Department.objects.all()
#     announcement = Announcement.objects.all()
#     images = RelatedImages.objects.all()
    
#     context = {'doctor': doctor, 'staff': staff,
#                'dept': dept, 'announcement': announcement, 'images': images,'h':h}
#     return render (request,'banner.html',context)
def adminHome(request): 
    h='Ahsan'
    doctor=Doctor.objects.all()
    staff=Staff.objects.all()
    dept=Department.objects.all()
    announcement=Announcement.objects.all()
    images=RelatedImages.objects.all()
    patient = Serial.objects.filter(visit_date__date=datetime.now(
    ), waiting_status=False, submit_status=False, done_status=False)
    # print(dept.doctor.count())
    context = {'doctor': doctor, 'staff': staff,
               'dept': dept, 'announcement': announcement, 'images': images, 'patient': patient,'h':h}
    return render(request,'admin/adminHome.html',context)

# def doctorHome(request):
#     doctor = Doctor.objects.all()
#     staff = Staff.objects.all()
#     images = RelatedImages.objects.all()
#     announcement = Announcement.objects.all()
#     patient = Serial.objects.filter(visit_date__date=datetime.now(
#     ), waiting_status=False, submit_status=False, done_status=False)
#     context = {'doctor': doctor, 'staff': staff, 'images': images}
#     return render(request,'doctor/doctorHome.html')
def addRelatedImages(request):
    form = RelatedImagesForm()
    if request.method == 'POST':
        form = RelatedImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            context = {'form': form}
            return redirect('add-images')
    form = RelatedImagesForm()
    context = {'form': form}
    return render(request, 'admin/related-images.html', context)
def addAnnouncement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            context = {'form': form}
            return redirect('/')
    form = AnnouncementForm()
    context = {'form': form}
    return render(request, 'admin/add-announcement.html', context)
def addDepartment(request):
    form = DepartmentAddForm()
    if request.method == 'POST':
        form = DepartmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return redirect('/')
    form = DepartmentAddForm()
    context = {'form': form}
    return render(request, 'admin/add-department.html', context)
def editDepartment(request,id):
    department = Department.objects.get(id=id)
    form = DepartmentAddForm(instance=department)
    if request.method == 'POST':
        form = DepartmentAddForm(request.POST, request.FILES,instance=department)
        if form.is_valid():
            form.save()
            return redirect('department')
    context = {'form': form}
    return render(request, 'admin/edit-department.html', context)
def department(request):
    dept=Department.objects.all()
    return render (request,'admin/department.html',{'dept':dept})
def addDoctor(request):
    if request.method=='POST':
        form=DoctorAddForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('/')
    form=DoctorAddForm()
    return render (request,'add-doctor.html',{'form':form})

def create_doctor(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        form = DoctorAddForm(request.POST,request.FILES)
        if fm.is_valid() and form.is_valid():
            user = fm.save()
            user.set_password(user.password)
            user_form = form.save(commit=False)
            user_form.user = user
            user_form.save()
            return redirect('/')
    else:
        fm = SignUpForm()
        form = DoctorAddForm()

    context = {'fm': fm, 'form': form}
    return render(request, 'admin/add-doctor.html', context)


def allDoctors(request):
    doctor = Doctor.objects.all()
    context = {'doctor': doctor}
    return render(request, 'admin/all-doctors.html', context)

def doctorDetail(request,id):
    detail=Doctor.objects.filter(id=id)
    context={'detail':detail}
    return render(request,'doctor/doctor-detail.html',context)


def doctorProfile(request):
    profile=Doctor.objects.get(user=request.user)
    department=profile.department
    dept=Doctor.objects.filter(department=department)
    context={'profile':profile,'dept':dept}
    return render(request,'doctor/doctorProfile.html',context)

def editDoctorProfile(request,id):
    doctor=Doctor.objects.get(id=id)
    form=DoctorAddForm(instance=doctor)
    if request.method=='POST':
        form=DoctorAddForm(request.POST,request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-profile')
    context={'form':form}
    return render(request,'doctor/doctor-profile-edit.html',context)

# Staff 


def create_staff(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        form = StaffAddForm(request.POST, request.FILES)
        if fm.is_valid() and form.is_valid():
            user = fm.save()
            user.set_password(user.password)
            user_form = form.save(commit=False)
            user_form.user = user
            user_form.save()
            return redirect('/')
    else:
        fm = SignUpForm()
        form = StaffAddForm()

    context = {'fm': fm, 'form': form}
    return render(request, 'admin/add-staff.html', context)

def staffHome(request):
    doctor=Doctor.objects.all()
    announcement=Announcement.objects.all()
    images=RelatedImages.objects.all()
    return render(request, 'staff/staffHome.html', { 'doctor': doctor, 'announcement': announcement, 'images': images})

def allStaff(request):
    staff = Staff.objects.all()
    context = {'staff': staff}
    return render(request, 'admin/all-staff.html', context)

def staffDetail(request,id):
    detail=Staff.objects.filter(id=id)
    context={'detail':detail}
    return render(request,'staff/staff-detail.html',context)

def staffProfile(request):
    profile=Staff.objects.get(user=request.user)   
    context={'profile':profile}
    return render(request,'staff/staffProfile.html',context)

def editStaffProfile(request,id):
    doctor=Staff.objects.get(id=id)
    form=StaffAddForm(instance=doctor)
    if request.method=='POST':
        form=StaffAddForm(request.POST,request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('staff-profile')
    context={'form':form}
    return render(request,'staff/staff-profile-edit.html',context)

def takeSerial(request):
    if request.method=='POST':
        form = SerialForm(request.POST, request.FILES)
        if form.is_valid():
            serial=form.save(commit=False)
            serial.waiting_status=True
            serial.save()
            return redirect('take-serial')
    form = SerialForm()
    return render (request,'staff/take-serial.html',{'form':form})

def todaySerial(request):
    today=Serial.objects.filter(visit_date__date=datetime.now())
    waiting_status = Serial.objects.filter(visit_date__date=datetime.now(), waiting_status=True)
    submit_status = Serial.objects.filter(
        visit_date__date=datetime.now(), submit_status=True)
    done_status = Serial.objects.filter(
        visit_date__date=datetime.now(), done_status=True)
    previous = Serial.objects.filter(
        visit_date__date=datetime.now(),waiting_status=False, submit_status=False, done_status=False,)
    print(today)
    context = {'today': today, 'previous': previous, 'waiting_status': waiting_status, 'submit_status': submit_status,"done_status": done_status}
    return render(request,'doctor/today-serial.html',context)

def moveSerial(request,id,sts):
    serial=Serial.objects.get(id=id)
    if sts=='waiting':
        serial.waiting_status=True
        serial.submit_status = False
        serial=serial.save()
        return redirect('today-serial')
    
    if sts == 'submit':
        serial.done_status = False
        serial.submit_status = True
        serial.waiting_status = False
        serial = serial.save()
        return redirect('today-serial')
    
    if sts=='done':
        serial.done_status = False
        serial.submit_status = False
        serial.waiting_status = False
        serial = serial.save()
        return redirect('today-serial')
    
def deleteSerial(request,id):
    serial=Serial.objects.get(id=id)
    serial=serial.delete()
    return redirect('today-serial')

def patient(request,id):
    serial=Serial.objects.get(id=id)
    print=(serial)
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            patient=form.save(commit=False)
            patient.patient = serial
            patient.save()
            return redirect('patient' ,id)
    form = MedicineForm()

    if request.method == 'POST':
        testForm = TestForm(request.POST, request.FILES)
        if testForm.is_valid():
            test = testForm.save(commit=False)
            test.patient = serial
            test.submit_status=True
            test.save()
            serial.test_submit=True
            serial.save()
            return redirect('patient' ,id)
    testForm = TestForm()

    if request.method == 'POST':
        symForm = SymptomForm(request.POST, request.FILES)
        if symForm.is_valid():
            sym = symForm.save(commit=False)
            sym.patient = serial
            sym.save()
            return redirect('patient' ,id)
    symForm = SymptomForm()

    context={
        'serial': serial, 'form': form, 'testForm': testForm, 'symForm':symForm
    }
    return render(request, 'doctor/patient.html',context)


def deleteMedicine(request, id):
    medicine = Medicine.objects.get(id=id)
    medicine = medicine.delete()
    return redirect('patient',id)
# Test 
def labHome(request):
    lab=Lab.objects.all()
    doctor=Doctor.objects.all()
    announcement=Announcement.objects.all()
    images=RelatedImages.objects.all()
    return render(request, 'lab/labHome.html', {'lab':lab, 'doctor': doctor, 'announcement': announcement, 'images': images})

def addLab(request):
    form = LabAddForm()
    if request.method == 'POST':
        form = LabAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return redirect('admin/adminHome')
    form = LabAddForm()
    context = {'form': form}
    return render(request, 'admin/add-lab.html', context)

def editLab(request,id):
    lab = Lab.objects.get(id=id)
    form = LabAddForm(instance=lab)
    if request.method == 'POST':
        form = LabAddForm(request.POST, request.FILES,instance=lab)
        if form.is_valid():
            form.save()
            return redirect('all-lab')
    context = {'form': form}
    return render(request, 'admin/edit-lab.html', context)

def allLab(request):
    lab=Lab.objects.all()
    return render (request,'admin/all-lab.html',{'lab':lab})

def addLabAssistant(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        form = LabAssistantForm(request.POST, request.FILES)
        if fm.is_valid() and form.is_valid():
            user = fm.save()
            user.set_password(user.password)
            user_form = form.save(commit=False)
            user_form.user = user
            user_form.save()
            return redirect('/')
    else:
        fm = SignUpForm()
        form = LabAssistantForm()

    context = {'fm': fm, 'form': form}
    return render(request, 'admin/add-lab-assistant.html', context)

def allLabAssistant(request):
    lab = LabAssistant.objects.all()
    context = {'lab': lab}
    return render(request, 'admin/all-assistant.html', context)

def assistantDetail(request,id):
    detail=LabAssistant.objects.filter(id=id)
    context={'detail':detail}
    return render(request,'lab/assistant-detail.html',context)

def assistantProfile(request):
    profile=LabAssistant.objects.get(user=request.user)   
    context={'profile':profile}
    return render(request,'lab/assistantProfile.html',context)

def editAssistantProfile(request,id):
    assistant=LabAssistant.objects.get(id=id)
    form=LabAssistantForm(instance=assistant)
    if request.method=='POST':
        form=LabAssistantForm(request.POST,request.FILES,instance=assistant)
        if form.is_valid():
            form.save()
            return redirect('assistant-profile')
    context={'form':form}
    return render(request,'lab/assistant-profile-edit.html',context)

def goForTest(request,id):
    # test_id=request.session.get("test_id",None)
    # test = Test.objects.get(id=test_id)
    # print(test_id)
    # print(test)
    lab=Lab.objects.all()
    patient=Serial.objects.get(id=id)
    test = patient.test_set.filter(pending_status=False, submit_status=False, done_status=False)
    context = {'lab': lab, 'patient': patient, 'test': test}
    return render(request,'lab/goForTest.html',context)

# def ttest(request,pk):
#     test=TestReport.objects.filter(id=pk)
#     form = TestReportForm()
#     if request.method == 'POST':
#         form = TestReportForm(request.POST, request.FILES)
#         if form.is_valid():
#             testForm = form.save(commit=False)
#             testForm.test_name=test
#             testForm.save()
#             # form.save()
#             return redirect('report', id)
#     form = TestReportForm()
#     return redirect(request.META['HTTP_REFERER'])



def PendingTest(request):
    patient = Serial.objects.filter(test_submit=True)
    context = {'patient': patient}
    return render(request, 'lab/testList.html', context)

def tests(request,id,sts):
    patient = Serial.objects.get(id=id)
    pending = Serial.objects.filter(
        test_pending=False, test_submit=True, test_done=False)
    # amount=0.0
    # total=0.0
    # test=[p for p in LabTest.objects.all()]
    # if test:
    #     for p in test:
    #         amount+=p.price
    #         print(amount)
    if sts == 'submit':
        patient.test_pending = True
        patient.test_submit = False
        patient.test_done = False
        patient=patient.save()
        return redirect('test',id)

def testReportAdd(request,id):
    # serial_id = request.session.get("serial_id", None)
    # patient = Serial.objects.get(id=serial_id)
    # print(patient)
    # test_id=request.session.get("test_id",None)
    # print(test_id)
    test = Test.objects.get(id=id)
    print(test)
    form = TestReportForm()
    if request.method == 'POST':
        form = TestReportForm(request.POST, request.FILES)
        if form.is_valid():
            testForm = form.save(commit=False)
            testForm.test_name=test
            testForm.save()
            # form.save()
            return redirect('report', id)
    form = TestReportForm()
    context = {'form': form, 'test': test, 'patient': patient}
    return render(request, 'addReport.html', context)

def testReport(request,id):
    lab=Lab.objects.all()
    serial=Serial.objects.get(id=id)
    context = {'lab': lab, 'serial': serial}
    return render(request, 'testReport.html', context)
