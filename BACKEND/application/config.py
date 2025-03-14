class Config():
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class LocalDevelopmentConfig(Config): # Inherited from Config
    # Configuration for Development
    SQLALCHEMY_DATABASE_URI='sqlite:///quizmaster.sqlite3' # Database URI
    DEBUG=True # True in Development mode

    # Configuration for Security
    SECRET_KEY="jdnfr34ir39jfi#$@#" # Helps in hashing the user credentials in the session
    SECURITY_PASSWORD_HASH="bcrypt" # Password Hashing Algorithm
    SECURITY_PASSWORD_SALT="73hrq498hr0920#$2@90ERT" # Salt for Password Hashing
    WTF_CSRF_ENABLED=False # Cross Site Request Forgery
    SECURITY_TOKEN_AUTHENTICATION_HEADER='Authentication-Token' # Token Authentication Header