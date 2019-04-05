# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# from . import models


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Post
#         fields = (
#             'id', 
#             'title', 
#             'author', 
#             'body_text', 
#             'date',
#             )

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = (
#             'id',
#             'username',
#         )