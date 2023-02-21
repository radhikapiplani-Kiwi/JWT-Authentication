"""
messages
"""
MESSAGES={

"MESSAGE_1" : "complete update",
"MESSAGE_2 ": "partial data updated",
"MESSAGE_3" : "data deleted"

}
"""
validation errors
"""

SIGNUP_VALIDATION_ERROR = {
  'first_name': {
        "blank": "first_name_BLANK",
        "invalid": "first_name_INVALID",
        "required": "first_name_REQUIRED",
    },
  'last_name': {
        "blank": "last_name_BLANK",
        "invalid": "last_name_INVALID",
        "required": "last_name_REQUIRED",
    },
   'username': {
        "blank": "username_BLANK",
        "invalid": "username_INVALID",
        "required": "username_REQUIRED",
         "exits":"username_EXISTS"
    },

    'password': {
        "blank": "PASSWORD_BLANK",
        "invalid": "PASSWORD_INVALID",
        "required": "PASSWORD_REQUIRED",
        "not-match":"Password fields didn't match"
    },
    'confirm_password': {
        "blank": "PASSWORD_BLANK",
        "invalid": "PASSWORD_INVALID",
        "required": "PASSWORD_REQUIRED",
    },
   'email': {
        "blank": "Email_BLANK",
        "required": "Email_REQUIRED",
         "exits":"email_EXISTS"
    }

}
LOGIN_VALIDATION_ERROR = {
        "Login":"Login_INVALID"

}
BOOK_VALIDATION_ERROR = {
  'name_of_book': {
        "blank": "name_of_book_BLANK",
        "invalid": "name_of_book_INVALID",
        "required": "name_of_book_REQUIRED",
    },
  'book_price': {
        "blank": "book_price_BLANK",
        "invalid": "book_price_INVALID",
        "required": "book_price_REQUIRED",
    },
   'authors_name': {
        "blank": "authors_name_BLANK",
        "invalid": "authors_name_INVALID",
        "required": "authors_name_REQUIRED"
    },
  'author_phone': {
        "blank": "author_phone_BLANK",
        "invalid": "author_phone_INVALID",
        "required": "author_phone_REQUIRED"
    }
}