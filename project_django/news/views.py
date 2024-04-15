from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForms
from django.views.generic import DetailView, UpdateView, DeleteView




def news_home(requests):
    news = Articles.objects.order_by('-date')
    return render(requests, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForms


class NewsDeleteView(DeleteView):
    success_url = '/news/'
    model = Articles
    template_name = 'news/news_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'
    form = ArticlesForms()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)