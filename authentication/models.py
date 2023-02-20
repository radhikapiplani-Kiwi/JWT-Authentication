from django.db import models


class Book(models.Model):
    """
    Book model to store Books data
    """
    name_of_book = models.CharField(max_length=20,null=False,blank=False)
    book_price = models.CharField(max_length=100,null=False,blank=False)
    authors_name = models.CharField(max_length=20,null=False,blank=False)
    author_phone = models.CharField(max_length=20,null=False,blank=False)

    class Meta:
        """
        class Meta for Book
        """
        db_table = 'Books'