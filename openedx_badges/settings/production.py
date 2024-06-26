"""
Production settings for Badges Integration.
"""


def plugin_settings(settings):
    """
    Production settings for Openedx Badges
    """
    settings.BADGR_USERNAME = settings.ENV_TOKENS.get('BADGR_USERNAME', settings.BADGR_USERNAME)
    settings.BADGR_PASSWORD = settings.ENV_TOKENS.get('BADGR_PASSWORD', settings.BADGR_PASSWORD)
    settings.BADGR_ISSUER_SLUG = settings.ENV_TOKENS.get('BADGR_ISSUER_SLUG', settings.BADGR_ISSUER_SLUG)
    settings.BADGR_BASE_URL = settings.ENV_TOKENS.get('BADGR_BASE_URL', settings.BADGR_BASE_URL)
    settings.BADGR_TOKENS_CACHE_KEY = settings.ENV_TOKENS.get('BADGR_TOKENS_CACHE_KEY', settings.BADGR_TOKENS_CACHE_KEY)
    settings.BADGR_TIMEOUT = settings.ENV_TOKENS.get('BADGR_TIMEOUT', settings.BADGR_TIMEOUT)
    settings.BADGR_ENABLE_NOTIFICATIONS = settings.ENV_TOKENS.get('BADGR_ENABLE_NOTIFICATIONS', settings.BADGR_ENABLE_NOTIFICATIONS)