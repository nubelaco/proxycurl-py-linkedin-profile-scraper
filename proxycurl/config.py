from os import environ


_ = environ.get


BASE_URL = _("BASE_URL", "https://nubela.co")
PROXYCURL_API_KEY = _("PROXYCURL_API_KEY", "")
TIMEOUT = _("TIMEOUT", 90)
MAX_RETRIES = _("MAX_RETRIES", 2)
MAX_BACKOFF_SECONDS = _("MAX_BACKOFF_SECONDS", 60)
MAX_WORKERS = _("MAX_WORKERS", 10)
