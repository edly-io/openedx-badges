"""
Dummy backend, for use in testing.
"""


from openedx_badges.backends.base import BadgeBackend
from openedx_badges.tests.factories import BadgeAssertionFactory


class DummyBackend(BadgeBackend):
    """
    Dummy backend that creates assertions without contacting any real-world backend.
    """
    def award(self, badge_class, user, evidence_url=None):
        return BadgeAssertionFactory(badge_class=badge_class, user=user)
