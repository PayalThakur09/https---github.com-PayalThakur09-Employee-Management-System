from django.urls import path
from . import views
from django.conf.urls.static import static
from task import settings


urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),

    path('adminpage/', views.admin, name='adminpage'),
    path('manager/', views.manager, name='manager'),
    path('teamleader/', views.teamleader, name='teamleader'),
    path('employee/', views.employee, name='employee'),

    path('meeting/', views.meeting, name='meeting'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
    path('teams_man/', views.teams_man, name='teams_man'),
    path('teams_tl/', views.teams_tl, name='teams_tl'),


    path('allemployees/', views.allemployees, name='allemployees'),
    path('allteamleaders/', views.allteamleaders, name='allteamleaders'),
    path('allmanagers/', views.allmanagers, name='allmanagers'),

    path('profile/', views.profile, name='profile'),
    path('viewdetail/<eid>', views.viewdetail, name='viewdetail'),
    path('tl_viewdetail/<eid>', views.tl_viewdetail, name='tl_viewdetail'),
    path('m_viewdetail/<eid>', views.m_viewdetail, name='m_viewdetail'),

    # path('e_profile/<int:user_id>', views.e_profile, name='e_profile'),
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)