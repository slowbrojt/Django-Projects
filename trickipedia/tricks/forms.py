from .models import Trick
from django.forms import ModelForm

class TrickForm(ModelForm):
	class Meta:
		model = Trick
		fields = ['name', 'email', 'video', 'skier', 'filmer', 'insta', 'ns']

form = TrickForm()