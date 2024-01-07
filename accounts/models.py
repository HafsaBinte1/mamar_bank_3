from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE

# admin: admin pass: 123
# user: rahim pass: hafsa123

# django amaderk built in user make korar facility dei
class UserBankAccount(models.Model):
    # One to one field karon ekjon user er ektai city sob kichui ektai thakbe
    # related_name newar karone emailt firtstname last name newa jabe
    user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    account_type = models.CharField(max_length = 10, choices = ACCOUNT_TYPE)
    #unique use korci karon 2jon user er account no kokhono same hobe nah
    account_no = models.IntegerField(unique = True)
    # null and blank true dichi jate user chaile birth date nah  dileo cholbe
    birth_date = models.DateField(null = True, blank = True)
    gender = models.CharField(max_length = 10, choices = GENDER_TYPE)
    # auto_now_add holo jedin account korbe sei date automaticly save hoy jabe
    initial_deposit_date = models.DateField(auto_now_add = True)
    # decimal_places = 2 mane 2 doshomik sthan pojonto rakhte parbe
    balance = models.DecimalField(default = 0, max_digits = 12, decimal_places = 2)
    
    def __str__(self):
        # str use kore account no k integer theke string a convert korci nah dile error dekhachilo
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        # related_name newar karone emailt firtstname last name newa jabe
        return str(self.user.email)



