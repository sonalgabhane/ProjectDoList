from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("registration/", UserCreate.as_view(), name='registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("create_list/", TodosListCreateView.as_view(), name='create_list'),
    path("todos_list/", TodosListView.as_view(), name='todos_list'),
    path('retrive_list/<int:pk>/', TodosRetrieveAPIView.as_view(), name='retrive_view'),
    path("update_list/<int:pk>/", TodosUpdateAPIView.as_view(), name='update_list'),
    path("delete_list/<int:pk>/", TodosDestroyAPIViewView.as_view(), name='delete_list')
]