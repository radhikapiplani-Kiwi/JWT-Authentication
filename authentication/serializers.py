from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
from .messages import *
import re
from django.contrib.auth import authenticate


class SignupSerializer(serializers.ModelSerializer):
    """
    serializer for Registering requested user
    """
    first_name = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=SIGNUP_VALIDATION_ERROR['first_name'])
    last_name = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=SIGNUP_VALIDATION_ERROR['last_name'])
    username = serializers.CharField(min_length=4,max_length=20, required=True,allow_blank=False,
                                        error_messages=SIGNUP_VALIDATION_ERROR['username'])
    email = serializers.EmailField(max_length=20, required=True,allow_blank=False,
                                        error_messages=SIGNUP_VALIDATION_ERROR['email'])
    password = serializers.CharField(write_only=True, min_length=8,allow_blank=False,
                                         error_messages=SIGNUP_VALIDATION_ERROR['password'])
    confirm_password = serializers.CharField(write_only=True, min_length=8,allow_null=False,
                                         error_messages=SIGNUP_VALIDATION_ERROR['confirm_password'])

    def validate(self, attrs):
        """
        validates password and confirm_password if equal :return data,
        else: return validation error
        """
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR["not-match"])
        return attrs

    def validate_first_name(self, value):
        """
        Check that the first name contains only letters
        """
        if not all(char.isalpha() for char in value):
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['first_name']['invalid'])
        return value

    def validate_last_name(self, value):
        """
        Check that the last name contains only letters
        """
        if not all(char.isalpha() for char in value):
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['last_name']['invalid'])
        return value

    def validate_username(self, value):
        """
        checks username if valid: return value,
        else: return validation error
        """
        username_regex = r'^[a-zA-Z0-9_-]{4,20}$'
        if not re.match(username_regex, value):
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['username']['invalid'])
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['username']['exits'])
        return value

    def validate_email(self, value):
        """
        checks email if valid : return value,
        else : return validation error
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['email']['exits'])
        return value

    def validate_password(self, value):
        """
        checks password if valid : return value,
        else : return validation error
        """
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])[0-9a-zA-Z!@#$%^&*()_+=-]{8,}$', value):
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['password']['invalid'])
        return value

    def validate_confirm_password(self, value):
        """
        checks confirm_password if valid : return value,
        else : return validation error
        """
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])[0-9a-zA-Z!@#$%^&*()_+=-]{8,}$', value):
            raise serializers.ValidationError(SIGNUP_VALIDATION_ERROR['confirm_password']['invalid'])
        return value

    def create(self, validated_data):
        """
        creates a user
        """
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        """
        class Meta for SignupSerializer
        """
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']


class LoginSerializer(serializers.ModelSerializer):
    """
    serializer for login a requested user
    """
    username = serializers.CharField(max_length=20, required=True,)
    password = serializers.CharField(max_length=20, required=True,allow_null=False)

    def validate(self, data):
        """
        authenticate the user if valid : return authenticated user
        else : return validation error
        """
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError(LOGIN_VALIDATION_ERROR["Login"])
        return user

    class Meta:
        """
        class Meta for LoginSerializer
        """
        model = User
        fields = ['username', 'password']


class CreateBookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Creating Book
    """
    name_of_book = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['name_of_book'])
    book_price = serializers.CharField(max_length=100, required=True,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['book_price'])
    authors_name = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['authors_name'])
    author_phone = serializers.CharField(max_length=20, required=True,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['author_phone'])

    def validate_name_of_book(self, value):
        """
        validates the name_of_book as first letter is in upper case
        """
        if not value[0].isupper():
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['name_of_book']['invalid'])
        return value

    def validate_book_price(self,value):
        """
        validates the book_price as it contains only digits
        """
        if not all(char.isdigit() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['book_price']['invalid'])
        return value

    def validate_authors_name(self, value):
        """
        Check that the first name contains only letters
        """
        if not all(char.isalpha() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['authors_name']['invalid'])
        return value

    def validate_author_phone(self,value):
        """
        validates author_phone
        """
        pattern = r'^\+?1?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['author_phone']['invalid'])
        return value


    def create(self, validated_data):
        """
        creating an instance of Book
        :param validated_data: data to be inserted
        :return: data instance
        """
        user = Book.objects.create(
            name_of_book=validated_data['name_of_book'],
            book_price=validated_data['book_price'],
            authors_name=validated_data['authors_name'],
            author_phone=validated_data['author_phone'],
        )
        return user

    class Meta:
        """
        class Meta for CreateBookSerializer
        """
        model = Book

        fields = ['id', 'name_of_book', 'book_price', 'authors_name', 'author_phone']


class UpdateBookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Updating Book
    """
    name_of_book = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['name_of_book'])
    book_price = serializers.CharField(max_length=100, required=True ,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['book_price'])
    authors_name = serializers.CharField(max_length=20, required=True ,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['authors_name'])
    author_phone = serializers.CharField(max_length=20, required=True ,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['author_phone'])

    def validate_name_of_book(self, value):
        """
        validates the name_of_book as first letter is in upper case
        """
        if not value[0].isupper():
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['name_of_book']['invalid'])
        return value

    def validate_book_price(self,value):
        """
        validates the book_price as it contains only digits
        """
        if not all(char.isdigit() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['book_price']['invalid'])
        return value

    def validate_authors_name(self, value):
        """
        Check that the first name contains only letters
        """
        if not all(char.isalpha() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['authors_name']['invalid'])
        return value

    def validate_author_phone(self,value):
        """
        validates author_phone
        """
        pattern = r'^\+?1?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['author_phone']['invalid'])
        return value

    def update(self, instance, validated_data):
        """
        updating an instance of Book
        :param instance:old Book data
        :param validated_data:new Book data
        :return: updated data instance of Book
        """
        ins = Book.objects.filter(id=instance.id).update(
            name_of_book=validated_data.get('name_of_book'),
            book_price=validated_data.get('book_price'),
            authors_name=validated_data.get('authors_name'),
            author_phone=validated_data.get('author_phone'))
        return ins

    class Meta:
        """
        class Meta for UpdateBookSerializer
        """
        model = Book

        fields = ['id', 'name_of_book', 'book_price', 'authors_name', 'author_phone']
