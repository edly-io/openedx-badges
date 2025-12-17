"""
Badges Application Configuration

Signal handlers are connected here.
"""

import logging
from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

log = logging.getLogger(__name__)

class OpenedxBadgesConfig(AppConfig):
    """
    Application Configuration for Badges.
    """
    name = 'openedx_badges'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: "openedx_badges",
                PluginURLs.REGEX: "^badges/",
                PluginURLs.RELATIVE_PATH: "api.urls",
            },
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
            },
            ProjectType.CMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
            },
        },
    }

    def ready(self):
        """
        Connect signal handlers.
        """
        from . import handlers  # pylint: disable=unused-import
        log.info("Loading badger app...")
