from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    copies_number = models.IntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.EmailField(max_length=80, unique=True)

    REQUIRED_FIELDS = ['groups_id']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username


class Loan(models.Model):
    loan_date = models.DateField()
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.name} {self.loan_date}"
