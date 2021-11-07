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
        fields = ("name",)


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_date", "member")

    member = UserSerializer()
