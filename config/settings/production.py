from .base import *

# _______________Static & Media Files__________________
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Database
if env.bool("DJANGO_USE_MEMORY_DATABASE", True):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": env.str("DJANGO_DB_ENGINE"),
            "NAME": env.str("DJANGO_DB_NAME"),
            "USER": env.str("DJANGO_DB_USER"),
            "PASSWORD": env.str("DJANGO_DB_PASSWORD"),
            "HOST": env.str("DJANGO_DB_HOST"),
            "PORT": env.int("DJANGO_DB_PORT", 5432),
        }
    }
