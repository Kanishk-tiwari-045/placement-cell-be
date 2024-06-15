from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicant/', include('applicant.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include('profiles.urls')),
    path('organization/', include('organization.urls')),
    path('generation/', include('generation.urls'))
]