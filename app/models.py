from django.db import models

STATE_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Barishal', 'Barishal'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)


class Resume(models.Model):
    name = models.CharField(max_length=55)
    dob = models.DateTimeField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=55)
    locality = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=55)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=55)
    profile_image = models.ImageField(upload_to='proimg', blank=True)
    my_file = models.ImageField(upload_to='docs',blank=True)