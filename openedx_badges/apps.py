"""
Badges Application Configuration

Signal handlers are connected here.
"""


from django.apps import AppConfig


class OpenedxBadgesConfig(AppConfig):
    """
    Application Configuration for Badges.
    """
    name = 'openedx_badges'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "openedx_badges",
                "regex": r"^badges",
                'relative_path': 'api.urls',
            }
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "production": {"relative_path": "settings.production"},
            }
        },
    }

    def ready(self):
        """
        Connect signal handlers.
        """
        from . import handlers  # pylint: disable=unused-import
