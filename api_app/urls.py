from django.urls import path
from .views import UserViews,ArchiveUserViews,CourViews,ArchiveCourViews,Getlogger,ArchiveUserDataViews


from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('user_login',Getlogger.as_view(), name='user_login'),
    # path('user_login',Getlogger.as_view(), name='user_login'),
    path('user', UserViews.as_view(), name='user_index'),
    path('user/<int:id>',UserViews.as_view(), name='user_id'),
    path('archive_user', ArchiveUserViews.as_view(), name='archive_user_index'),
    path('archive_user/<int:id>', ArchiveUserViews.as_view(), name='archive_user_id'),
    path('archive_cour', ArchiveCourViews.as_view(), name='archive_cour_index'),
    path('archive_cour/<int:id>', ArchiveCourViews.as_view(), name='arcive_cour_id'),
    path('cour', CourViews.as_view(), name='cour_index'),
    path('cour/<int:id>', CourViews.as_view(), name='cour_id'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    

]



