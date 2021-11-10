from rest_framework import serializers

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name",)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "copies_number", "author")

    author = AuthorSerializer()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "password", "groups", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_date", "member")

    member = UserSerializer()
