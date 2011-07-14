
from django.http import HttpResponseRedirect

from mobile_detector import get_mobile_cookie_name

def force_mobile(request):
    return render_mobile_response(request, 'true')

def force_desktop(request):
    return render_mobile_response(request, 'false')

def render_mobile_response(request, cookie_value):
    response = HttpResponseRedirect(request.GET.get('next', '/'))
    response.set_cookie(get_mobile_cookie_name(), cookie_value)
    return response