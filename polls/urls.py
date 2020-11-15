from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/user/', views.list_by_user, name='list_by_user'),
    path('add/', views.polls_add, name='add_pool'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.poll_vote, name='vote'),
    path('<int:question_id>/edit/', views.editq, name='editq'),
    path('<int:question_id>/delete/', views.polls_delete, name='delete_poll'),
    path('end/<int:question_id>/', views.endpoll, name='end_poll'),
    path('<int:question_id>/choice/add/', views.add_choice, name='add_choice'),
    path('edit/choice/<int:choice_id>/', views.choice_edit, name='choice_edit'),
    path('delete/choice/<int:choice_id>/', views.choice_delete, name='choice_delete'),
]