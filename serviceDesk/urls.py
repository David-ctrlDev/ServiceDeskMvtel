from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from requirements import views as requirements_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('home/', user_views.home, name ='home'),
    path('', user_views.login_view, name ='login'),
    path('logout', user_views.logout_view, name ='logout'),
    path('requirements/services', requirements_views.services_page, name ='services'),
    path('requirements/newservices', requirements_views.get_name, name ='newservices'),
    path('requirements/newservices/succes', requirements_views.registersucces, name ='succes'),
    path('requirements/newservices/viewsucces', requirements_views.view_succes, name ='viewsucces'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
