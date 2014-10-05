from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext
from Myton_Django.views import custom_proc
from apps.article.models import Article
# Create your views here.

@login_required
def latest_news(request):
    last_article = Article.objects.all()
    data = {'breadcrumb':'latest-news', 'last_article':last_article}
    return render_to_response('article/latest_news.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def detail_article(request, slug):
    article = Article.objects.get(slug=slug)
    data = {'breadcrumb':'latest-news', 'article':article}
    return render_to_response('article/article_detail.html', data, context_instance=RequestContext(request, processors=[custom_proc]))
