# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from rest_framework import routers
from junction.schedule import views as schedule_views
from junction.conferences import views as conference_views

router = routers.DefaultRouter()

router.register('conferences', conference_views.ConferenceView)
router.register('venues', conference_views.VenueView)
router.register('rooms', conference_views.RoomView)

router.register('schedules', schedule_views.ScheduleView)

'''
Root url routering file.

You should put the url config in their respective app putting only a
reference to them here.
'''

urlpatterns = patterns(
    '',

    # Django Admin
    url(r'^nimda/', include(admin.site.urls)),

    # Third Party Stuff
    url(r'^accounts/', include('allauth.urls')),
    url('^markdown/', include('django_markdown.urls')),

    # Proposals related
    url(r'^(?P<conference_slug>[\w-]+)/proposals/', include('junction.proposals.urls')),
    url(r'^(?P<conference_slug>[\w-]+)/dashboard/reviewers/',
        'junction.proposals.dashboard.reviewer_comments_dashboard',
        name='proposal-reviewers-dashboard'),
    url(r'^(?P<conference_slug>[\w-]+)/dashboard/$',
        'junction.proposals.dashboard.proposals_dashboard', name='proposal-dashboard'),
    url(r'^(?P<conference_slug>[\w-]+)/dashboard/votes/$',
        'junction.proposals.dashboard.reviewer_votes_dashboard',
        name='proposal-reviewer-votes-dashboard'),
    url(r'^(?P<conference_slug>[\w-]+)/dashboard/votes/export/$',
        'junction.proposals.dashboard.export_reviewer_votes',
        name='export-reviewer-votes'),

    url(r'^api/v1/', include(router.urls)),

    # User Dashboard
    url(r'^profiles/', include('junction.profiles.urls', namespace="profiles")),

    # Schedule related
    url(r'^(?P<conference_slug>[\w-]+)/schedule/',
        include('junction.schedule.urls')),
    # Static Pages. TODO: to be refactored
    url(r'^speakers/$', TemplateView.as_view(template_name='static-content/speakers.html',), name='speakers-static'),
    url(r'^schedule/$', TemplateView.as_view(template_name='static-content/schedule.html',), name='schedule-static'),
    url(r'^venue/$', TemplateView.as_view(template_name='static-content/venue.html',), name='venue-static'),
    url(r'^sponsors/$', TemplateView.as_view(template_name='static-content/sponsors.html',), name='sponsors-static'),
    url(r'^blog/$', TemplateView.as_view(template_name='static-content/blog-archive.html',), name='blog-archive'),
    url(r'^coc/$', TemplateView.as_view(template_name='static-content/coc.html',), name='coc-static'),
    url(r'^faq/$', TemplateView.as_view(template_name='static-content/faq.html',), name='faq-static'),

    # Proposals as conference home page. TODO: Needs to be enhanced
    url(r'^(?P<conference_slug>[\w-]+)--/',
        RedirectView.as_view(pattern_name="proposals-list"),
        name='conference-detail'),

    # add at the last for minor performance gain
    url(r'^', include('junction.pages.urls', namespace='pages')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^400/$', 'django.views.defaults.bad_request'),  # noqa
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    )
