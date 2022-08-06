from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from news.models import News, Category
from news.forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeNews(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 4
    # extra_context = {'title': 'Главная'}
    # mixin_prop = 'hello, home!'
    # paginate_by = 2
#    select_related = 'category'
#    queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Главная страница'
            return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# def index(request):
#     return HttpResponse('<b>Hello, world!</b>')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})

class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'
    
    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.incrementViewCount()
        return item



    # News.objects.filter(pk).update(counter=F('counter') + 1)

    # def get_article_view(request, article_id, *args, **kwagrs):
    # if request.method == "GET":
    #     # increment counter with update method to avoid race conditions
    #     Article.objects.filter(id=article_id).update(counter=F('counter') + 1)
    #     article = Article.objects.get(id=article_id)
    #     return render_article(article)
    

# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    raise_exception = True


def test(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news/test.html', context)
