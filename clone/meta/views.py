from django.shortcuts import render, redirect
from django.views.generic import CreateView
from . models import Post, BlogCategory, TeamMember,Blogcat,Comment
from . forms import CommentForm
from django.db.models import Q
from . forms import PostForm

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-created')[:3]
  
    return render(request, 'meta/index.html', {'posts': post})

def blog(request):
    post = Post.objects.all().order_by('created')
    
    return render(request, 'meta/blog.html',{'posts':post})

def singleblog(request, slug):
    commentlist = Comment.objects.all()
    post1 = Post.objects.all()[:4]
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        forms= CommentForm(request.POST)

        if forms.is_valid():
            comment = forms.save(commit=False)
            comment.post = posts
            comment.save()
            return redirect('/')
    
    else:
        forms= CommentForm()

    context = {
        'forms': forms,
        'commentlist': commentlist,
        'post': post,
        'recent': post1
    }
    return render(request, 'meta/singleblog.html', context)

def base(request):
    return render(request, 'meta/base.html')


def room(request):
    return render(request, 'meta/room.html')


def fashion(request):
    return render(request, 'meta/fashion.html')

# class AddPost(CreateView):
#     model = Post
#     template_name= 'meta/addpost.html'
#     fields = '__all__'

def CategoryView(request, cate):
    post_category = Post.objects.filter(blogcat=cate)
    return render(request, 'category.html', {'cate': cate, 'post_category':post_category})






class AddCategoryView(CreateView):
    model = Blogcat
    template_name= 'category.html'
    fields = '__all__'








class TeamMember(CreateView):
    model = TeamMember
    template_name= 'meta/teammember.html'
    fields = '__all__'

def admintable(request):
    return render(request, 'meta/admintable.html')
   
class Form(CreateView):
    model = PostForm
    template_name = 'meta/form.html'


def dashboard(request):
    andrew = Post.objects.all()
    return render(request, 'meta/dashboard.html', {'list': andrew})

def SearchView(request):
    if request.method == 'POST':
        searched = request.POST['search-bar']
        post = Post.objects.filter(Q(title__contains=searched) | Q(content__contains=searched))                                                                        

    return render(request, 'meta/search.html', {'search': searched, 'searchedpost':post})




def deleteProject(request, pk):
    project = Post.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    context = {'object': project}
    return render(request, 'meta/deleteproject.html', context)

# def createProject(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')

#     context = {'form': form}
#     return render(request, 'meta/addpost.html', context)




def addPost(request):

    form = PostForm()
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'meta/addpost.html', context)
       
        
    

def updateProject(request, pk):
    project = Post.objects.get(id=pk)
    form = PostForm(instance=project)
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            

    context = {'form': form}
    return render(request, 'meta/addpost.html', context)
       
        
    