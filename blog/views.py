from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# This is a local file /blog/forms.py, can also do blog.forms
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	stuff_for_frontend = {'posts': posts}
	return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	stuff_for_frontend = {'post': post}
	return render(request, 'blog/post_detail.html', stuff_for_frontend)

def post_new(request):
	# If someone is doing a Post request, do this stuff
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	# If someone is doing a Get request, do this
	else:

		# see all the items in that dictionary object
		# print(request.__dict__)
		form = PostForm()
		stuff_for_frontend = {'form': form}
	return render(request, 'blog/post_edit.html', stuff_for_frontend)

	