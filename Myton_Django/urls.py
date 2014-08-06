from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.template.loader import add_to_builtins
add_to_builtins('apps.templatetags.myton_tags')

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'Myton_Django.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^staff/$', 'staff.views.home'),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^chaining/', include('smart_selects.urls')),

                       # url(r'^trade/$', 'trade.views.hello'),
                       # url(r'^trade/$', 'trade.views.home'),
                       url(r'^trade/create/$', 'trade.views.create'),
                       url(r'^latest-news/$', 'trade.views.articles'),
                       url(r'^article/(\d+)/$', 'trade.views.article'),
                       # url(r'^part-search/$', 'trade.views.partsearch'),
                       url(r'^search/$', 'Myton_Django.views.search'),
                       url(r'^downloads/$',
                           'apps.files.views.list_file_downloads'),
                       url(r'^my-details/$', 'apps.customer.views.details'),
                       url(r'^my-orders/$', 'trade.views.orders'),
                       url(r'^about/$', 'trade.views.about'),
                       url(r'^login/$', 'trade.views.login'),
                       url(r'^language/(?P<language>[a-z\-]+)/$',
                           'trade.views.language'),

                       # cart
                       url(r'^addcart/(\d+)/$', 'Myton_Django.views.add_to_cart'),
                       url(r'^my-cart/$', 'Myton_Django.views.mycart'),

                       # user auth urls
                       url(r'^accounts/login/$', auth_views.login,
                           {'template_name': 'safe_login.html'}, name='auth_login'),
                       url(r'^accounts/logout/$', auth_views.logout,
                           {'next_page': '?next=/'}, name='auth_logout'),
                       url(r'^accounts/register/$',
                           'apps.customer.views.register_user'),
                       url(r'^accounts/register_success/$',
                           'apps.customer.views.register_success'),


                       # url(r'^latest-news/$', include('trade.urls')),

                       # toms experiment - 03.07.2014
                       url(r'^experiment/$',
                           'Myton_Django.views.ua_display_good1'),

                       )
