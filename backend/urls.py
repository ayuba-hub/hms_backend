from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restAPI import views
from rest_framework_simplejwt.views import TokenRefreshView



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile',views.ProfileViewSet)
router.register(r'department',views.DepartmentVieSet)
router.register(r'position',views.JobPositionViewSet)
router.register(r'patients',views.PatientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),

]
