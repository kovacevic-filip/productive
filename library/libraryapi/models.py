from django.db import models


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


class Member(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Loan(models.Model):
    loan_date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.name} {self.loan_date}"
