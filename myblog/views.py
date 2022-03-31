from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,UpdatePosForm,PostFormNew
from .models import Post,Catagory
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


class HomeViews(ListView):
    model = Post
    template_name='home.html'
    ordering=['-post_date']
class DetielView(DetailView):
    model = Post
    template_name='detaile.html'
    
class AddPost(CreateView):
    model = Post
    form_class=PostFormNew
    template_name='add_post.html'
    #fields='__all__'
class UpdatePost(UpdateView):
    model=Post
    form_class=UpdatePosForm
    template_name='update.html'
    #fields='__all__'
    # fields=['title','title_tag','body']
class DeletePost(DeleteView):
    model=Post
    template_name='deletePost.html'
    success_url= reverse_lazy('home')
class AddCatagory(CreateView):
    model = Catagory
    #form_class=PostForm
    template_name='add_Catagory.html'
    fields='__all__'

def CatagorView(request,id):
    catagor=Catagory.objects.get(pk=id)
    posts=catagor.post_set.all()
    context={
        'catagory':catagor,
        'posts':posts,

    }
    return render(request,'catagory.html',context)

def likeView(request,post_id):
    Post_like=get_object_or_404(Post, pk=request.POST.get('post_id'))
    Post_like.like.add(request.user)
    return HttpResponseRedirect(reverse('detile', args=[str(post_id)]))