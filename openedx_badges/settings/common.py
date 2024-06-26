"""
Common settings for Badges Integration.
"""


def plugin_settings(settings):
    """
    Common settings for Openedx Badges
    """
    settings.FEATURES['ENABLE_OPENBADGES'] = True
    settings.BADGING_BACKEND = 'openedx_badges.backends.badgr.BadgrBackend'
    settings.BADGR_USERNAME = ''
    settings.BADGR_PASSWORD = ''
    settings.BADGR_TOKENS_CACHE_KEY = 'openedx-badge'
    settings.BADGR_ISSUER_SLUG = ''
    settings.BADGR_BASE_URL = ''
    settings.BADGR_TIMEOUT = 10
    settings.BADGR_ENABLE_NOTIFICATIONS = False
