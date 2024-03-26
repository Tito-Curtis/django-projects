
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
import logging

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            logging.debug(f"Attempting authentication with email: {email}")
            
            if user.password == password:  # Compare plain text passwords
                logging.debug(f"Attempting authentication with password: {password}")#
                return user
            else:
                return None  # Incorrect password
        except User.DoesNotExist:
            return None  # Email does not exist