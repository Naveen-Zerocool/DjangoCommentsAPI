from .models import *
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(CommentSerializer, self).to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%d-%b-%Y %I:%M")
        representation['updated_at'] = instance.updated_at.strftime("%d-%b-%Y %I:%M")
        return representation

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ReplySerializer, self).to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%d-%b-%Y %I:%M")
        representation['updated_at'] = instance.updated_at.strftime("%d-%b-%Y %I:%M")
        return representation

class CommentThreadSerializer(serializers.Serializer):
    comment = CommentSerializer()
    reply = ReplySerializer(many=True)
