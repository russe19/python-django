from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from app_news.models import News, Comment
from app_news.forms import NewsForm, CommentForm


class NewsView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()

class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(news_name=kwargs['object'])
        return context

    def post(self, request, news_id):
        if request.POST.get('user_name'):
            comment_form = CommentForm(request.POST, request.FILES)
            if comment_form.is_valid():
                comment = Comment(user_name=request.POST['user_name'],
                                  text = request.POST['text'], news_name = News.objects.get(id=news_id))
                comment.save()
                return redirect('news_list')
        else:
            comment_form = CommentForm()
            news = str(News.objects.get(id=news_id))
            return render(request, 'app_news/create_comment.html',
                          context={'comment_form': comment_form, 'news': news, 'news_id': news_id})


class CreateView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/create.html', context={'news_form': news_form})

    def post(self, request):
        news = News()
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return redirect('news_list')
        return render(request, 'app_news/create.html', context={'news_form': news_form})

class UpdateView(View):

    def get(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/update.html', context={'news_form': news_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
            return redirect('news_list')
        return render(request, 'app_news/update.html', context={'news_form': news_form, 'profile_id': profile_id})





