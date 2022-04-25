from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePost, CommentForm
from .models import Post
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):

	post = Post.objects.all()	
	p = Paginator(post, 5)
	page_number = request.GET.get('page')
	page = p.get_page(page_number)

	context = {
		'post':post, 'page':page
	}	
	return render(request, 'blog/home.html',context)

def postview(request,pk):
	context = {'posts':Post.objects.get(id=pk)}
	return render(request,'blog/viewpost.html', context)

@login_required
def CreateNewPost(request):
	profile = request.user
	form = CreatePost()
	if request.method == 'POST':
		form = CreatePost(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.author = profile
			project.save()
			return redirect('blog-home')

	context = {'form':form}

	return render(request, 'blog/post.html', context)

@login_required
def updatepost(request,pk):
	post = Post.objects.get(id=pk)
	form = CreatePost(instance=post)
	if request.method == 'POST':
		form = CreatePost(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('blog-home')

	context = {'form':form}

	return render(request, 'blog/post.html', context)

def deletepost(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('blog-home')
	context = {'post':post}
	return render(request, 'blog/delete.html', context)

def bloguser(request,pk):
	# user = User.objects.get(id=pk)
	post = Post.objects.get(id=pk)
	postnum = len(Post.objects.filter(author=pk))
	print(postnum)
	context = {'post':post,'postnum':postnum}
	return render(request, 'blog/user.html', context)

def addcomment(request):
	return render(request, 'blog/comment.html')

def about(request):
	return render(request, 'blog/about.html',{'title':'Conclusion'})
	return HttpResponse("<h1>Welcome</h1>")
	
