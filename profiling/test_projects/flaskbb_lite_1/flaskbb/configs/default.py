# -*- coding: utf-8 -*-
"""
    flaskbb.configs.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    This is the default configuration for FlaskBB that every site should have.
    You can override these configuration variables in another class.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys

_VERSION_STR = '{0.major}{0.minor}'.format(sys.version_info)


class DefaultConfig(object):

    # Get the app root path
    #            <_basedir>
    # ../../ -->  flaskbb/flaskbb/configs/base.py
    _basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
                            os.path.dirname(__file__)))))

    DEBUG = False
    TESTING = False

    # Logs
    # If SEND_LOGS is set to True, the admins (see the mail configuration) will
    # recieve the error logs per email.
    SEND_LOGS = False

    # The filename for the info and error logs. The logfiles are stored at
    # flaskbb/logs
    INFO_LOG = "info.log"
    ERROR_LOG = "error.log"

    # Default Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + _basedir + '/' + \
                              'flaskbb.sqlite'

    # This option will be removed as soon as Flask-SQLAlchemy removes it.
    # At the moment it is just used to suppress the super annoying warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # This will print all SQL statements
    SQLALCHEMY_ECHO = False

    # Security
    # This is the secret key that is used for session signing.
    # You can generate a secure key with os.urandom(24)
    SECRET_KEY = 'secret key'

    # Protection against form post fraud
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "reallyhardtoguess"

    # Searching
    WHOOSH_BASE = os.path.join(_basedir, "whoosh_index", _VERSION_STR)

    # Auth
    LOGIN_VIEW = "auth.login"
    REAUTH_VIEW = "auth.reauth"
    LOGIN_MESSAGE_CATEGORY = "info"
    REFRESH_MESSAGE_CATEGORY = "info"

    # Caching
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 60

    ## Captcha
    RECAPTCHA_ENABLED = False
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = "your_public_recaptcha_key"
    RECAPTCHA_PRIVATE_KEY = "your_private_recaptcha_key"
    RECAPTCHA_OPTIONS = {"theme": "white"}

    ## Mail
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False
    MAIL_USERNAME = "noreply@example.org"
    MAIL_PASSWORD = ""
    MAIL_DEFAULT_SENDER = ("Default Sender", "noreply@example.org")
    # Where to logger should send the emails to
    ADMINS = ["admin@example.org"]

    # Flask-Redis
    REDIS_ENABLED = False
    REDIS_URL = "redis://:password@localhost:6379"
    REDIS_DATABASE = 0

    # URL Prefixes
    FORUM_URL_PREFIX = ""
    USER_URL_PREFIX = "/user"
    MESSAGE_URL_PREFIX = "/message"
    AUTH_URL_PREFIX = "/auth"
    ADMIN_URL_PREFIX = "/admin"
