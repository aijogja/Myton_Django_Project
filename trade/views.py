from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from trade.models import Article
from django.http import HttpResponse
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.loader import render_to_string
# Create your views here.

# def home(request):
#     name = "Welcome JSquare"
#     data = {'name':name, 'breadcrumb':'home'}
#     return render_to_response('base.html', data, context_instance=RequestContext(request))

@login_required
def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    data = {
        'articles' : Article.objects.all(),
        'language' : language,
        'session_language' : session_language,
        'breadcrumb':'latest-news'
    }
    return render_to_response('articles.html', data, context_instance=RequestContext(request))

def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

@login_required
def article(request, article_id=1):
    data = {'article': Article.objects.get(id=article_id)}
    return render_to_response('article.html', data, context_instance=RequestContext(request))

def partsearch(request):
    return render_to_response('partsearch.html')

@login_required
def details(request):
    data = {'breadcrumb':'my-details'}
    return render_to_response('my-detail.html', data, context_instance=RequestContext(request))

@login_required
def downloads(request):
    data = {'breadcrumb':'downloads'}
    return render_to_response('downloads.html', data, context_instance=RequestContext(request))

@login_required
def orders(request):
    data = {'breadcrumb':'my-orders'}
    return render_to_response('my-orders.html', data, context_instance=RequestContext(request))

def about(request):
    data = {}
    return render_to_response('about.html', data, context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html')

def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/trade/all')
        else:
            form = ArticleForm()

        args ={}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('create_article.html', args)

