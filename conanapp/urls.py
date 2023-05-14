from django.urls import path
from . import views


urlpatterns = [
   path('', views.home ,name='index'),
   path('ar', views.home_ar ,name='index-ar'),
   path('team', views.team ,name='team'),
   path('team/ar', views.team_ar ,name='team-ar'),
   path('web', views.web ,name='web'),
   path('web/ar', views.web_ar ,name='web-ar'),
   path('ui', views.ui ,name='ui'),
   path('ui/ar', views.ui_ar ,name='ui-ar'),
   path('contact', views.contact ,name='contact'),
   path('contact/ar', views.contact_ar ,name='contact-ar'),
   path('graphic', views.graphic ,name='graphic'),
   path('graphic/ar', views.graphic_ar ,name='graphic-ar'),
   path('mobile', views.mobile ,name='mobile'),
   path('mobile/ar', views.mobile_ar ,name='mobile-ar'),
   path('motion', views.motion ,name='motion'),
   path('motion/ar', views.motion_ar ,name='motion-ar'),
   path('social', views.social ,name='social'),
   path('social/ar', views.social_ar ,name='social-ar'),
   
   

]
