
# Open edX Badges (Badgr Backend)

This Django app integrates Open Badges support into Open edX using a Badgr-compatible badge server. It handles badge class creation, awarding badges, and managing badge assertions automatically in response to platform events like enrollments and certificate generation.

## Key Features

* Integrates Open edX with a Badgr-compatible badge server
* Automatically creates badge classes for courses when needed
* Awards badges when learners complete courses and certificates are issued
* Tracks awarded badges locally
* Provides an API endpoint to fetch user badge assertions

---

## Installation

1. Add this app to your Open edX environment (mounted app or installed package)
2. Add it to `INSTALLED_APPS`
3. Add the `issue_badges` field to CourseFields
4. Configure the required Badgr settings (see below)
5. Run migrations for the models

---

## Important: add the following field to the `CourseFields` class in `xmodule`:

```python
issue_badges = Boolean(
    display_name=_("Issue Open Badges"),
    help=_(
        "Issue Open Badges badges for this course. Badges are generated when certificates are created."
    ),
    scope=Scope.settings,
    default=True
)
````

This field enables per-course control over badge issuance.

---

## Required Settings

Configure the following (typically in `common.py`) to connect to your badge server:

* `BADGR_USERNAME` – Badge server username
* `BADGR_PASSWORD` – Badge server password
* `BADGR_TOKENS_CACHE_KEY` – Cache key for access token
* `BADGR_ISSUER_SLUG` – Issuer slug on the badge server
* `BADGR_BASE_URL` – Base URL of the badge server API (e.g., `https://api.badgr.io`)

These settings allow the app to authenticate and manage badges on your server.

---

## Models Overview

The app introduces models for tracking badges:

* **BadgeClass** – Defines badges per course and mode
* **BadgeAssertion** – Tracks badges awarded to users
* **CourseCompleteImageConfiguration** – Configures badge images per course mode
* **CourseEventBadgesConfiguration** – Supports event-based or meta badges

Migrations must be run to create these models.

---

## API Endpoint

* **Endpoint:** `/assertions/user/<username>/`
* **Purpose:** Retrieve all badge assertions for a user

---

## Notes

* Requires a Badgr-compatible server with correct issuer permissions
* Access tokens are cached
* Badge creation and awarding are automated

---

This app provides a streamlined, event-driven badging system for Open edX with full course-level control.

