from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^', include('mobile_detector.urls')),

    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'sample/index.html',
    }),

)
