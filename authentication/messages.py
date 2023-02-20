"""
messages
"""
MESSAGE_1 = "complete update"
MESSAGE_2 = 'partial data updated'
MESSAGE_3 = 'data deleted'
"""
validation errors
"""
VALIDATION_ERROR="Password fields didn't match."

VALIDATION = {
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
    },
    "Login":"Login_INVALID"

}