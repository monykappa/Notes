# notes/urls.py
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.create_note, name='create_note'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('profile/', views.user_profile_view, name='profile'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('trash/', views.trash_view, name='trash_view'),
    path('restore/<int:note_id>/', views.restore_note, name='restore_note'),
    path('delete-permanently/<int:note_id>/', views.delete_permanently, name='delete_permanently'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)