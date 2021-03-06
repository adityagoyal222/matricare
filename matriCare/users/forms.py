from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django.db.transaction import commit
import random
class UserForm(UserCreationForm):
   

    class Meta:
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','user_type')


        @transaction.atomic()
        def save(self):
            user = User.objects.create(
                user_type=self.cleaned_data['user_type'],
                user_color= "%06x" % random.randint(0, 0xFFFFFF)
            )
            return user