from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'trade.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'trade.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/%', 'trade.views.language'),
    url(r'^create/$', 'trade.views.create'),
)