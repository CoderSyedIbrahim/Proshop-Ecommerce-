"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse

from django.conf import settings
from django.conf.urls.static import static

def maintenance_view(request, *args, **kwargs):
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Site Under Maintenance</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8f9fa;
            color: #343a40;
            text-align: center;
            padding: 150px 20px;
            margin: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        h1 {
            font-size: 40px;
            margin-bottom: 10px;
            font-weight: 600;
        }
        p {
            font-size: 18px;
            color: #6c757d;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Site Under Maintenance</h1>
        <p>This service is temporarily unavailable. We apologize for the inconvenience and will be back online shortly.</p>
    </div>
</body>
</html>"""
    return HttpResponse(html, status=503)

urlpatterns = [
    re_path(r'^.*$', maintenance_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
