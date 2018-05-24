from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment/list/$',views.ListCommentView.as_view(), name='listComment'),
    url(r'^comment/add/$',views.AddCommentView.as_view(), name='addComment'),
    url(r'^comment/(?P<pk>[0-9]+)/$',views.DetailCommentView.as_view(), name='detailComment'),
    url(r'^comment/(?P<pk>[0-9]+)/update/$',views.UpdateCommentView.as_view(), name='updateComment'),
    url(r'^comment/(?P<pk>[0-9]+)/delete/$',views.DeleteCommentView.as_view(), name='deleteComment'),

    url(r'^reply/add/$',views.AddReplyView.as_view(), name='addReply'),
    url(r'^reply/(?P<pk>[0-9]+)/$',views.DetailReplyView.as_view(), name='detailReply'),
    url(r'^reply/(?P<pk>[0-9]+)/update/$',views.UpdateReplyView.as_view(), name='updateReply'),
    url(r'^reply/(?P<pk>[0-9]+)/delete/$',views.DeleteReplyView.as_view(), name='deleteReply'),

    url(r'^comment/(?P<pk>[0-9]+)/thread/$',views.CommentThreadView.as_view(), name='commentThread'),
]
