Open edX Badges (Badgr Backend)
==============================

This Django app integrates Open Badges support into Open edX using a
Badgr-compatible badge server. It handles badge class creation, awarding
badges, and managing badge assertions automatically in response to
platform events like enrollments and certificate generation.

Key Features
------------

* Integrates Open edX with a Badgr-compatible badge server
* Automatically creates badge classes for courses when needed
* Awards badges when learners complete courses and certificates are issued
* Tracks awarded badges locally
* Provides an API endpoint to fetch user badge assertions

Installation
------------

1. Add this app to your Open edX environment (mounted app or installed package)
2. Add it to ``INSTALLED_APPS``
3. Add the ``issue_badges`` field to ``CourseFields``
4. Configure the required Badgr settings (see below)
5. Run migrations for the models

Add the ``issue_badges`` field to the ``CourseFields`` class in ``xmodule``
-------------------------------------------------------------------------

.. code-block:: python

    issue_badges = Boolean(
        display_name=_("Issue Open Badges"),
        help=_(
            "Issue Open Badges badges for this course. Badges are generated when certificates are created."
        ),
        scope=Scope.settings,
        default=True
    )

This field enables per-course control over badge issuance. Without it,
badges are enabled for all courses by default, and the feature cannot be
toggled at the course level via Advanced Settings.

Required Settings
-----------------

Configure the following (typically in ``common.py``) to connect to your
badge server:

* ``BADGR_USERNAME`` – Badge server username
* ``BADGR_PASSWORD`` – Badge server password
* ``BADGR_TOKENS_CACHE_KEY`` – Cache key for access token
* ``BADGR_ISSUER_SLUG`` – Issuer slug on the badge server
* ``BADGR_BASE_URL`` – Base URL of the badge server API
  (for example: ``https://api.badgr.io``)

These settings allow the app to authenticate and manage badges on your server.

Models Overview
---------------

The app introduces models for tracking badges:

* **BadgeClass** – Defines badges per course and mode
* **BadgeAssertion** – Tracks badges awarded to users
* **CourseCompleteImageConfiguration** – Configures badge images per course mode
* **CourseEventBadgesConfiguration** – Supports event-based or meta badges

Migrations must be run to create these models.

API Endpoint
------------

* **Endpoint:** ``/assertions/user/<username>/``
* **Purpose:** Retrieve all badge assertions for a user

Notes
-----

* Requires a Badgr-compatible server with correct issuer permissions
* Access tokens are cached
* Badge creation and awarding are automated

This app provides a streamlined, event-driven badging system for Open edX
with full course-level control.

More Help
---------

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a
`Slack invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide:

https://github.com/edly-io/openedx-badges/issues

For more information about these options, see the
`Getting Help <https://openedx.org/getting-help>`__ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/

License
-------

The code in this repository is licensed under the Apache Software License
2.0 unless otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
------------

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_
for details.

This project is currently accepting all types of contributions, including
bug fixes, security fixes, maintenance work, and new features. However,
please make sure to have a discussion about your new feature idea with the
maintainers prior to beginning development to maximize the chances of your
change being accepted.

You can start a conversation by creating a new issue on this repo
summarizing your idea.

The Open edX Code of Conduct
---------------------------

All community members are expected to follow the
`Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
------

The assigned maintainers for this component and other project details may
be found in `Backstage`_. Backstage pulls this data from the
``catalog-info.yaml`` file in this repo.

.. _Backstage: https://backstage.openedx.org/catalog/default/component/openedx-badges

Reporting Security Issues
------------------------

Please do not report security issues in public.
Please email security@openedx.org.

Badges
------

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge|
|pyversions-badge| |license-badge| |status-badge|

.. |pypi-badge| image:: https://img.shields.io/pypi/v/openedx-badges.svg
   :target: https://pypi.python.org/pypi/openedx-badges/
   :alt: PyPI

.. |ci-badge| image:: https://github.com/edly-io/openedx-badges/workflows/Python%20CI/badge.svg?branch=main
   :target: https://github.com/edly-io/openedx-badges/actions
   :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/edly-io/openedx-badges/coverage.svg?branch=main
   :target: https://codecov.io/github/edly-io/openedx-badges?branch=main
   :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/openedx-badges/badge/?version=latest
   :target: https://docs.openedx.org/projects/openedx-badges
   :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/openedx-badges.svg
   :target: https://pypi.python.org/pypi/openedx-badges/
   :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edly-io/openedx-badges.svg
   :target: https://github.com/edly-io/openedx-badges/blob/main/LICENSE.txt
   :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
