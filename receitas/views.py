from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, ReviewForm
from .models import Post, Comment, Category
from django.views import generic


# CRUD
####################### READ ##################################

class IndexView(generic.ListView):
    model = Post
    template_name = 'receitas/index.html'


def detail_receita(request, receita_id):
    receita = get_object_or_404(Post, pk=receita_id)
    comments = Comment.objects.filter(post=receita).order_by('-date')
    context = {'receita': receita,
               'comments': comments}
    return render(request, 'receitas/detail.html', context)
####################################################################

####################### SEARCH ##################################
def search_receita(request):
    context = {"receita_list": []}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(title__icontains=search_term)
        context = {
            'receita_list': post_list
        }
    return render(request, 'receitas/search.html', context)
#####################################################################

####################### CREATE ##################################
def create_receita(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Post(**post_form.cleaned_data)
            post.save()
            return HttpResponseRedirect(reverse('receitas:detail', args=(post.pk,)))
    else: 
        post_form = PostForm()
    context = {'form': post_form}
    return render(request, 'receitas/create.html', context)
#####################################################################

####################### UPDATE ##################################
def update_receita(request, receita_id):
   receita = get_object_or_404(Post, pk=receita_id)
   if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=receita)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('receitas:detail', args=(receita_id,)))
   else: 
       form = PostForm(instance=receita)
   context = {'receita': receita, 'form': form}
   return render(request, 'receitas/update.html', context)
#####################################################################

####################### DELETE ##################################
def delete_receita(request, receita_id):
    post = get_object_or_404(Post, pk=receita_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('receitas:index'))
    context = {'receita': post}
    return render(request, 'receitas/delete.html', context)
#####################################################################
def view_comments(request, receita_id):
    receita = get_object_or_404(Post, pk=receita_id)
    comments = Comment.objects.filter(post=receita).order_by('-date')
    context = {'receita': receita,
               'comments': comments}
    return render(request, 'receitas/comments.html', context)

def create_comment(request, receita_id):
    post = get_object_or_404(Post, pk=receita_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment_autor = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(post=post, autor=comment_autor, text=comment_text)
            comment.save()
            return HttpResponseRedirect(reverse('receitas:detail', args=(receita_id,)))
    else:
        form = ReviewForm()
    context = {'form': form, 'receita': post}
    return render(request, 'receitas/create_comment.html', context)
#############################################################################

class CategoryView(generic.ListView):
    model = Category
    template_name = 'receitas/categoria.html'
    context_object_name = 'categorias'

def category_detail(request, categoria_id):
    categoria = get_object_or_404(Category, pk=categoria_id)
    receitas = categoria.receitas.all()
    context = {
        "categoria": categoria,
        "receitas": receitas
    }
    return render(request, "receitas/category_detail.html", context)