from django.contrib import admin
from django.urls import path, include
from todos.views import register_user, login_user
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/signup/", register_user, name="signup"),
    path("api/signin/", login_user, name="signin"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
