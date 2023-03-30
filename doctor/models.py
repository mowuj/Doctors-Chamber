from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import datetime
from PIL import Image
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg',upload_to='media/admins', blank=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class RelatedImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    caption = models.CharField(max_length=250)
    photo = models.ImageField(default='default.jpg',upload_to='media/images', blank=True)
    def __str__(self):
        return self.description

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=150)
    manager = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='default.jpg',upload_to='media/images', blank=True)
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    GENDER = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE')
    )
    # DEPARTMENT = (
    #     ('Anesthesiology', 'Anesthesiology'),
    #     ('Medicine', 'Medicine'),
    #     ('Neurology', 'Neurology'),
    #     ('Orthopaedics', 'Orthopaedics'),
    #     ('Radiology', 'Radiology'),
    #     ('Surgery', 'Surgery')
    # )
    UNDERGRADUATE = (
        ('MBBS', 'MBBS'),
        ('BMBS', 'BMBS'),
        ('MBChB', 'MBChB'),
        ('MBBCh', 'MBBCh'),
        ('B.Med', 'B.Med'),
        ('MB', 'MB'),
        ('BM', 'BM'),
        ('B.S', 'B.S'),
        ('B.Surg', 'B.Surg')

    )
    GRADUATE = (
        ('MD', 'MD'),
        ('Dr.MuD', 'Dr.MuD'),
        ('Dr.Med', 'Dr.Med'),
        ('DO', 'DO')
    )
    VISIT_DAY = (
        ('Saturday', 'SATURDAY'),
        ('Sunday', 'SUNDAY'),
        ('Monday', 'MONDAY'),
        ('Tuesday', 'TUESDAY'),
        ('Wednesday', 'WEDNESDAY'),
        ('Thursday', 'THURSDAY'),
        ('Friday', 'FRIDAY')

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_id = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=GENDER,default='Male')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL ,null=True)
    visit_day = MultiSelectField(
        max_length=150, max_choices=7, choices=VISIT_DAY, default='Friday')
    birth_date = models.DateField()
    nid = models.CharField(max_length=150, blank=True, null=True)
    undergraduate = MultiSelectField(
        max_length=150, max_choices=3, choices=UNDERGRADUATE, default='MBBS')
    college = models.CharField(max_length=250)
    graduate = MultiSelectField(
        max_length=150, max_choices=3, choices=GRADUATE, default='MD')
    institute = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    hospital = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField()
    permanent_address = models.CharField(max_length=250, blank=True, null=True)
    present_address = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(default='default.jpg',upload_to='media/images', blank=True)
    join_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

class Staff(models.Model):
    GENDER = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL ,null=True)
    staff_id = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    nid = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, choices=GENDER, default='Male')
    birth_date = models.DateField()
    ssc = models.CharField(max_length=150)
    hsc = models.CharField(max_length=150)
    honor = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    permanent_address = models.CharField(max_length=250, blank=True, null=True)
    present_address = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(default='default.jpg',
                            upload_to='media/images', blank=True)
    join_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name



class Serial(models.Model):
    GENDER = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE')
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=GENDER, default='Male')
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    pressure = models.CharField(max_length=150, blank=True, null=True)
    number=models.CharField(max_length=150)
    visit_date = models.DateTimeField(default=datetime.now())
    issue_date = models.DateTimeField(default=datetime.now())
    paid = models.BooleanField(default=False)
    address = models.CharField(max_length=150, blank=True, null=True)
    waiting_status = models.BooleanField(default=False)
    submit_status = models.BooleanField(default=False)
    done_status = models.BooleanField(default=False)
    test_submit = models.BooleanField(default=False)
    test_pending = models.BooleanField(default=False)
    test_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number) +" "+ str(self.name)

class Patient(models.Model):
    patient=models.ForeignKey(Serial, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.patient)
    
class Medicine(models.Model):
    patient = models.ForeignKey(Serial, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=150)
    before_breakfast=models.IntegerField(default=0)
    morning=models.IntegerField(default=0)
    before_lunch=models.IntegerField(default=0)
    midday=models.IntegerField(default=0)
    before_dinner=models.IntegerField(default=0)
    night=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)  

class Lab(models.Model):
    name = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    photo = models.ImageField(default='default.jpg',
                            upload_to='lab/images', blank=True)
    def __str__(self):
        return str(self.name)
    
class LabAssistant(models.Model):
    GENDER = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lab=models.ForeignKey(Lab, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    nid = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, choices=GENDER, default='Male')
    birth_date = models.DateField()
    degree1 = models.CharField(max_length=150)
    institute1=models.CharField(max_length=150,blank=True, null=True)
    degree2 = models.CharField(max_length=150,blank=True, null=True)
    institute2=models.CharField(max_length=150,blank=True, null=True)
    degree3 = models.CharField(max_length=150,blank=True, null=True)
    institute3=models.CharField(max_length=150,blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    permanent_address = models.CharField(max_length=250, blank=True, null=True)
    present_address = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(default='default.jpg',
                            upload_to='media/images', blank=True)
    join_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return str(self.name)

class LabTest(models.Model):
    lab=models.ForeignKey(Lab, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=150)
    price=models.PositiveIntegerField(default=0)
    min_point= models.FloatField(blank=True,null=True)
    mix_point = models.FloatField(blank=True, null=True)
    total_price=models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.name)

class Test(models.Model):
    patient = models.ForeignKey(Serial, on_delete=models.CASCADE,blank=True,null=True)
    name=models.ForeignKey(LabTest, on_delete=models.CASCADE,blank=True,null=True)
    # go_status = models.BooleanField(default=False)
    submit_status = models.BooleanField(default=False)
    pending_status = models.BooleanField(default=False)
    done_status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)
    
class Symptom(models.Model):
    patient = models.ForeignKey(Serial, on_delete=models.CASCADE,blank=True,null=True)
    symptom=models.CharField(max_length=150)
    def __str__(self):
        return str(self.patient.name)

class TestReport(models.Model):
    report_by=models.ForeignKey(LabAssistant, on_delete=models.CASCADE,blank=True,null=True)
    # doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True,null=True)
    # patient = models.ForeignKey(Serial, on_delete=models.CASCADE,blank=True,null=True)
    test_name = models.ForeignKey(Test, on_delete=models.CASCADE,blank=True,null=True)
    point= models.FloatField()

