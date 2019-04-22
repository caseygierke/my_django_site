from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		# Select the model to generate for
		model = Post
		# Pick which fields you want it to render
		fields = ('title', 'text')