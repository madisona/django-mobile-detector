from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mobile_detector.views',
    url(r'^force-mobile/', 'force_mobile', name="force_mobile"),
    url(r'^force-desktop/', 'force_desktop', name="force_desktop"),
)
