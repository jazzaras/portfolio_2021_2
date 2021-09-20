from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import contact.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', contact.views.thanks, name='thanks'),
    path('About/', jobs.views.aboutme, name='aboutme'),
    path('resume/', jobs.views.resume, name='resume'),
    path('', jobs.views.home, name='home'),
    path('contact/', contact.views.contact, name='contact'),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls'))
 ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
