# proyecto-final

1 - en settings  agregar esto  


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#! Login


LOGIN_URL = reverse_lazy("home:login")
LOGIN_REDIRECT_URL = reverse_lazy("home:index")


#! Media

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"



2- urls principal y de home, hecho en 