from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^$',
        include(
            'core.urls',
            namespace='core'
        )
    ),
    url(
        r'^palestrantes/',
        include(
            'speakers.urls',
            namespace='speakers'
        )
    ),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/', include('api.urls')),
)


urlpatterns = format_suffix_patterns(
    urlpatterns,
    allowed=['json', 'api']
)

# Default login/logout views
urlpatterns += patterns(
    '',
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
)
