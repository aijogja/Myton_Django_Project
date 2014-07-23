from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Myton_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^trade/$', 'trade.views.hello'),
    url(r'^trade/$', 'trade.views.home'),
    url(r'^trade/create/$', 'trade.views.create'),
    url(r'^latest-news/$', 'trade.views.articles'),
   # url(r'^part-search/$', 'trade.views.partsearch'),
    url(r'^search/$', 'Myton_Django.views.search'),
    url(r'^downloads/$', 'trade.views.downloads'),
    url(r'^my-details/$', 'trade.views.details'),
    url(r'^my-orders/$', 'trade.views.orders'),
    url(r'^about/$', 'trade.views.about'),
    url(r'^login/$', 'trade.views.login'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'trade.views.language'),

    #user auth urls
    url(r'^accounts/login/$', 'Myton_Django.views.login'),
    url(r'^accounts/auth/$', 'Myton_Django.views.auth_view'),
    url(r'^accounts/logout/$', 'Myton_Django.views.logout'),
    url(r'^accounts/loggedin/$', 'Myton_Django.views.loggedin'),
    url(r'^accounts/invalid/$', 'Myton_Django.views.invalid_login'),
    url(r'^accounts/register/$', 'Myton_Django.views.register_user'),
    url(r'^accounts/register_success/$', 'Myton_Django.views.register_success'),


   # url(r'^latest-news/$', include('trade.urls')),

   #toms experiment - 03.07.2014
   url(r'^experiment/$', 'Myton_Django.views.ua_display_good1'),

)
