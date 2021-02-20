from django.forms import ModelForm
from django import forms
from .models import Log, Collaborator
from users.models import User

class CreateLogForm(ModelForm):
    class Meta:
        exclude = ('user', 'created_date')
        model = Log

    def save(self, user):
        log = Log.objects.create(
            text = self.cleaned_data['text'],
            user = user,
        )
        return log


class ShareForm(ModelForm):
    doctor = forms.CharField(max_length=100)
    class Meta:
        exclude = ('mother', 'doctor',)
        model = Collaborator

    def save(self, user):
        doctor = User.objects.filter(username=self.cleaned_data['doctor']),
        if doctor[0].exists():
            if doctor[0][0].user_type == 1:
                existing_collaborators = Collaborator.objects.filter(doctor = doctor[0][0], mother=user)
                if existing_collaborators.exists():
                    return False
                else:
                    collaborator = Collaborator.objects.create(
                        doctor = doctor[0][0],
                        mother = user
                    )
                    return collaborator
        return False