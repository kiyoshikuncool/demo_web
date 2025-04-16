class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Database connection
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to improve performance
    JWT_SECRET_KEY = 'CoLamMoiCoAn!@99'  # Secret key for JWT authentication
    DEBUG = True  # Enable debugging (turn off in production)