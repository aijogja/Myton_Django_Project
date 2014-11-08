from apps.log.models import Session
from django.utils import timezone

class SessionLogMiddleware(object):
    def process_request(self,request):        
        if request.user.is_authenticated():
            # import pdb; pdb.set_trace()
            session_key = request.session.session_key
            try:
                visit = Session.objects.get(session_key=session_key)
            except:
	            visit = Session()
	            visit.session_key = session_key
	            visit.ipaddress = request.META.get('REMOTE_ADDR')
	            visit.user = request.user
	            visit.save()
            now = timezone.now()
            time_on_site = 0
            if visit.created_on:
                time_on_site = (now-visit.created_on).seconds
            visit.time_on_site = time_on_site
            visit.save()
