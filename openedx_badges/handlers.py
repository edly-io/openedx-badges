"""
Badges related signal handlers.
"""

from django.dispatch import receiver

from common.djangoapps.student.models import EnrollStatusChange
from common.djangoapps.student.signals import ENROLL_STATUS_CHANGE
from openedx.core.djangoapps.signals.signals import COURSE_CERT_AWARDED
from lms.djangoapps.certificates.models import GeneratedCertificate

from openedx_badges.events.course_complete import course_badge_check
from openedx_badges.events.course_meta import award_enrollment_badge, completion_check, course_group_check
from openedx_badges.utils import badges_enabled


@receiver(ENROLL_STATUS_CHANGE)
def award_badge_on_enrollment(sender, event=None, user=None, **kwargs):  # pylint: disable=unused-argument
    """
    Awards enrollment badge to the given user on new enrollments.
    """
    if badges_enabled and event == EnrollStatusChange.enroll:
        award_enrollment_badge(user)

@receiver(COURSE_CERT_AWARDED, sender=GeneratedCertificate)
# pylint: disable=unused-argument
def create_course_badge(sender, user, course_key, status, **kwargs):
    """
    Standard signal hook to create course badges when a certificate has been generated.
    """
    course_badge_check(user, course_key)


@receiver(COURSE_CERT_AWARDED, sender=GeneratedCertificate)
def create_completion_badge(sender, user, course_key, status, **kwargs):  # pylint: disable=unused-argument
    """
    Standard signal hook to create 'x courses completed' badges when a certificate has been generated.
    """
    completion_check(user)


@receiver(COURSE_CERT_AWARDED, sender=GeneratedCertificate)
def create_course_group_badge(sender, user, course_key, status, **kwargs):  # pylint: disable=unused-argument
    """
    Standard signal hook to create badges when a user has completed a prespecified set of courses.
    """
    course_group_check(user, course_key)
