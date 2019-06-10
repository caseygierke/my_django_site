from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		# Select the model to generate for
		model = Post
		# Pick which fields you want it to render
		fields = ('title', 'text')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)