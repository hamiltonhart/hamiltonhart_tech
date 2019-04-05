
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'HamiltonHart.tech'
API_DESCRIPTION = 'An API for hamiltonhart.tech.'
schema_view = get_swagger_view(title=API_TITLE)




urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include(
        'rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),
]
