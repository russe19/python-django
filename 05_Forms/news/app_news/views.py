from django.shortcuts import render
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


class CreateView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/create.html', context={'news_form': news_form})

    def post(self, request):
        news = News()
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return render(request, 'app_news/created_news.html', context={'news_form': news_form})
        return render(request, 'app_news/create.html', context={'news_form': news_form})


class CreateView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/create.html', context={'news_form': news_form})

    def post(self, request):
        news = News()
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return render(request, 'app_news/created_news.html', context={'news_form': news_form})
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
            return render(request, 'app_news/created_news.html', context={'news_form': news_form})
        return render(request, 'app_news/update.html', context={'news_form': news_form, 'profile_id': profile_id})


class CreateCommentView(View):

    def get(self, request, news_id):
        comment_form = CommentForm()
        return render(request, 'app_news/create_comment.html', context={'comment_form': comment_form, 'news_id': news_id})

    def post(self, request, news_id):
        comment = Comment()
        comment
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment.save()
            return render(request, 'app_news/created_comm.html', context={'comment_form': comment_form, 'news_id': news_id})
        return render(request, 'app_news/create_comment.html', context={'comment_form': comment_form, 'news_id': news_id})




