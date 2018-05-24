from django.shortcuts import render
from django.http import Http404
from collections import namedtuple

from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

comment_thread = namedtuple('CommentThread', ('comment', 'reply'))

class AddCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ListCommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DetailCommentView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AddReplyView(CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ListReplyView(ListAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class DeleteReplyView(DestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class UpdateReplyView(UpdateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class DetailReplyView(RetrieveAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class CommentThreadView(APIView):
    def get_object(self, pk):
        try:
            comment = comment_thread(
                comment = Comment.objects.get(id=pk),
                reply = Reply.objects.filter(comment=pk)
                )
            return comment
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment_thread = self.get_object(pk)
        serializer = CommentThreadSerializer(comment_thread)
        return Response(serializer.data)
