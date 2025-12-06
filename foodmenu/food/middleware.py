import time
from django.http import HttpResponseForbidden
class LogRequestMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        #before view
        print(f"[MIDDLEWARE] Request Path: {request.path}")
        response= self.get_response(request)
        #after view
        print(f"[MIDDLEWARE] Response Status Code: {response.status_code}")
        return response
    
class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self,request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"[MIDDLEWARE] Response Time : {duration:.2f}")
        return response
    
"""class BlockedIPMiddleware:
    blocked_ip = [ "11.0.0.0"]
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self,request):
       ip = request.META.get('REMOTE_ADDR')
       if ip in self.blocked_ip:
           return HttpResponseForbidden("Your IP is blocked")"""