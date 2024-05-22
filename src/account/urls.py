from django.urls import path

from .views import GetUserProfile, DocumentTypeList

urlpatterns = [
    path('get_user_profile/<int:pk>/', GetUserProfile.as_view(), name='get_user_profile'),
    path('document_type_list/', DocumentTypeList.as_view(), name='document_type_list'),
]
