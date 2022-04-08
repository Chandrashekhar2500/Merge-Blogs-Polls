from django.utils import timezone
from .models import Post , Category , Tag , User , Comments
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, User_Category, User_Signup, User_Update ,Insert_Comment
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import  AuthenticationForm 

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogs/post_list.html', {'posts': posts})

def category_list(request):
    categorys = Category.objects.all()
    return render (request, 'blogs/category_list.html', {'categorys':categorys})

def tag_list(request):
    tags = Tag.objects.all()
    return render (request, 'blogs/tag_list.html', {'tags':tags})    
   
def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    comments = posts.comments.filter(parent__isnull=True)
    if request.method == 'POST':
        form = Insert_Comment(data=request.POST)
        if form.is_valid():
            parent_obj = None
            parent_id = None
            parent_id =(request.POST.get('reply_id'))
            print(parent_id)
            if parent_id:
                parent_obj = Comments.objects.filter(id=parent_id).last()
            if parent_obj:
                parent_comment = form.save(commit=False)
                parent_comment.parent = parent_obj
                parent_comment.posts = posts
                parent_comment.user = request.user
                parent_comment.save()
            response = form.save(commit=False)
            response.posts = posts
            response.user = request.user
            response.save()    
            return redirect('blogs:post_detail', slug=slug)
    else:
        form = Insert_Comment()
    return render(request, 'blogs/post_detail.html',{'posts': posts,'comments': comments,'form':form})


def category_detail(request, slug):
    categorys = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=categorys)
    return render(request, 'blogs/category_detail.html', {'posts':post})    

def tag_detail(request, slug):
    tags = get_object_or_404(Tag, slug=slug)
    post = Post.objects.filter(tag=tags)
    return render(request, 'blogs/tag_detail.html', {'posts': post}) 


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blogs:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blogs/post_new.html', {'form': form})    

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blogs:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_edit.html', {'form': form})   

def category_new(request):
    if request.method == "POST":
        form = User_Category(request.POST)
        if form.is_valid(): 
            category = form.save(commit=False)
            category.name = request.user
            category.save()
            return redirect('blogs:category_detail', slug=category.slug)
    else:
        form = PostForm()
    return render(request, 'blogs/category_edit.html', {'category': category}) 


def signup_page(request):
    if request.method == 'POST':
        form = User_Signup(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=raw_password)
            return redirect('blogs:login_page')
    else:
        form = User_Signup()
    return render(request, 'blogs/signup_page.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = request.POST['username']
            raw_password = request.POST['password']
            user = authenticate(username=user, password=raw_password)
            login(request,user)
            return redirect('blogs:post_list')
    else:
        form = AuthenticationForm()
    return render(request,'blogs/login_page.html', {'form':form})    


def logout_page(request):
    logout(request)
    return redirect ('blogs:post_list')
        
def user_profile(request):
    # user = get_object_or_404(User)
    # print(user,'uuuuuuuuuuuu')
    return render(request, 'blogs/user_profile.html')


def user_update(request):
    if request.method == 'POST':
        form = User_Update(request.POST, request.FILES ,instance=request.user )
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        return redirect('blogs:user_profile')
    else:
        form = User_Update(instance=request.user)
    return render(request, 'blogs/user_update.html', {'form': form})
    

   
  

    