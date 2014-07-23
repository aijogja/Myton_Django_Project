from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from trade.models import Article
from django.http import HttpResponse
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    name = "Welcome JSquare"
    t = get_template('base.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html',
                              {'articles' : Article.objects.all(),
                              'language' : language,
                              'session_language' : session_language})

def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

def article(request, article_id=1):
    return render_to_response('article.html',
        {'article': Article.objects.get(id=article_id)})

def partsearch(request):
    return render_to_response('partsearch.html')

def details(request):
    return render_to_response('my-detail.html')

def downloads(request):
    return render_to_response('downloads.html')

def orders(request):
    return render_to_response('my-orders.html')

def about(request):
    return render_to_response('about.html')

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

