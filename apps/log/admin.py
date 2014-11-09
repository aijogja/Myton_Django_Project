from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect, HttpResponse
from datetime import timedelta
from apps.log.models import Search, Session
from djqscsv import render_to_csv_response, generate_filename

class SearchAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['keyword', 'user', 'created_on']
    list_filter = ['user']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user', 'keyword')
        return self.readonly_fields

    # Export
    def export_csv(self, request):
        queryset_search = Search.objects.values('id', 'keyword', 'user__username')
        return render_to_csv_response(queryset_search, filename='log_search', append_datestamp=True)

    # Define the url
    def get_urls(self):
        urls = super(SearchAdmin,self).get_urls()
        my_urls = patterns('',
            (r'^export/$',self.export_csv),
            )
        return my_urls + urls

class SessionAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['session_key', 'user', 'ipaddress', 'convert_time_on_site', 'created_on']
    list_filter = ['user']

    def convert_time_on_site(self, obj):
        if obj.time_on_site is not None:
            return timedelta(seconds=obj.time_on_site)
    convert_time_on_site.short_description = 'Online Time'
    convert_time_on_site.admin_order_field = 'time_on_site'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('session_key', 'user', 'ipaddress')
        return self.readonly_fields

    # Export
    def export_csv(self, request):
        queryset_session = Session.objects.values('id', 'session_key', 'user__username', 'ipaddress')        
        return render_to_csv_response(queryset_session, filename='log_session', append_datestamp=True)

    # Define the url
    def get_urls(self):
        urls = super(SessionAdmin,self).get_urls()
        my_urls = patterns('',
            (r'^export/$',self.export_csv),
            )
        return my_urls + urls

# Register your models here.
admin.site.register(Search,SearchAdmin)
admin.site.register(Session,SessionAdmin)
