from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import UpdatePosForm,PostFormNew
from .models import Post,Catagory
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


class HomeViews(ListView):
    model = Post
    template_name='home.html'
    ordering=['-post_date']
class CatagoryView(ListView):
    model = Catagory
    template_name='base.html'
    
class DetielView(DetailView):
    model = Post
    template_name='detaile.html'
    def get_context_data(self, *args, **kwargs):
        context=super(DetailView,self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked = False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context
  
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
    all_catagory=Catagory.objects.all()
    catagor=Catagory.objects.get(pk=id)
    posts=catagor.post_set.all()
    context={
        'catagory':catagor,
        'posts':posts,
        'all_catagory':all_catagory,

    }
    return render(request,'catagory.html',context)

def likeView(request,post_id):
    Post_like=get_object_or_404(Post, pk=request.POST.get('post_id'))
    liked = False
    if Post_like.like.filter(id=request.user.id).exists():
        Post_like.like.remove(request.user)
        liked = False
    else:
        Post_like.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detile', args=[str(post_id)]))