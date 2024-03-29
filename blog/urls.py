from . import views
from django.urls import path



urlpatterns = [
    path('',views.post_list_view,name='post_list'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/edit/<int:id>',views.post_edit,name='post_edit'),
    path('post/draft/',views.draft_list_view,name='post_draft'),

#ajax
    path('post/draft/publish/',views.draft_list_publish,name='post_publish'),


    path('post/comment/<int:id>',views.comment_to_post,name='comment_to_post'),
    path('post/comment/remove/<int:id>',views.remove_comment,name='remove_comment'),
    path('post/comment/approve/<int:id>',views.approve_comment,name='approve_comment'),

    

]