from __future__ import absolute_import

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from filebrowser.sites import site
from config.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("topics/", include("hickup.topics.urls", namespace="topics")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin urls and security
urlpatterns += [
    # Django Admin, use {% url 'admin:index' %}
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("jet/", include("jet.urls", namespace="jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", namespace="jet-dashboard")),
    path("flatpage/", include("django.contrib.flatpages.urls")),
    path(settings.ADMIN_FILEBROWSER_URL, site.urls),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),
]

urlpatterns += [
    # User management
    path("users/", include("hickup.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
]

# SEO url settings
urlpatterns += [
    # Your stuff: custom urls includes go here
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt/",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
    path("tinymce/", include("tinymce.urls")),
    # Cookie consent
    # path('cookies/', include('cookie_consent.urls')),
    # Language switcher support urls for django
    path("i18n/", include("django.conf.urls.i18n")),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
