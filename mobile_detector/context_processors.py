
from mobile_detector import use_mobile

def detect_mobile(request):
    return {
        'use_mobile': use_mobile(request),
    }