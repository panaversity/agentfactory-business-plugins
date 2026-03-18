USER STORIES: User Authentication
================================================================
Epic: User Authentication — Enable users to authenticate via SSO,
magic link, or password, with each flow working independently.
Stories: 9 | Sprints: 2 | Persona(s): Enterprise IT Admin, Individual User

-- ENTERPRISE IT ADMIN STORIES ------------------------------------

Story 1: SSO Provider Configuration
  As an Enterprise IT Admin,
  I want to configure my organisation's SSO identity provider,
  So that my employees can sign in using their existing corporate credentials.

  Acceptance Criteria:
  AC1: Given I am on the SSO configuration page, when I enter a valid
       SAML 2.0 or OIDC metadata URL, then the provider details are
       fetched and saved to my organisation's settings.
  AC2: Given I have saved a provider configuration, when I view the
       SSO settings, then I see the provider name, protocol, and
       connection status.
  AC3: Given I enter an unreachable or malformed metadata URL, when I
       submit, then I receive a specific error message describing the
       failure reason.
  AC4: Given an SSO provider is already configured, when I update the
       metadata URL, then the previous configuration is replaced and
       the new configuration is validated before saving.

  Size:         M
  Dependencies: None
  Notes:        Must support both SAML 2.0 and OIDC. Metadata parsing
                is a sub-task owned by engineering.

Story 2: SSO Connection Verification
  As an Enterprise IT Admin,
  I want to test the SSO connection before rolling it out to employees,
  So that I can confirm authentication works end-to-end without
  affecting production users.

  Acceptance Criteria:
  AC1: Given I have a saved SSO configuration, when I click "Test
       Connection," then the system initiates a test authentication
       flow with the identity provider.
  AC2: Given the test authentication succeeds, when the flow completes,
       then I see a success confirmation with the returned user
       attributes (email, name, groups).
  AC3: Given the identity provider rejects the test authentication,
       when the flow completes, then I see the specific error returned
       by the provider.
  AC4: Given the identity provider is unreachable, when I click "Test
       Connection," then I receive a timeout error within 10 seconds.

  Size:         S
  Dependencies: Story 1 (SSO Provider Configuration)
  Notes:        Test flow must not create a real user session.

Story 3: SSO Enforcement Policy
  As an Enterprise IT Admin,
  I want to enforce SSO as the only authentication method for my
  organisation,
  So that employees cannot bypass corporate security policies by
  using password or magic link login.

  Acceptance Criteria:
  AC1: Given I have a working SSO configuration, when I enable "SSO
       Only" enforcement, then password and magic link login options
       are hidden for all users in my organisation.
  AC2: Given SSO enforcement is enabled, when an organisation user
       tries to access the password login endpoint directly, then they
       are redirected to the SSO flow.
  AC3: Given SSO enforcement is enabled, when the SSO provider is
       down, then organisation users see an error page explaining SSO
       is unavailable and to contact their IT admin.
  AC4: Given I disable SSO enforcement, when organisation users visit
       login, then password and magic link options are available again.

  Size:         M
  Dependencies: Story 1 (SSO Provider Configuration)
  Notes:        Must not affect users outside the organisation.
                Admin accounts should have a break-glass bypass
                mechanism — flag for engineering discussion.

-- INDIVIDUAL USER STORIES ----------------------------------------

Story 4: Magic Link Request
  As an Individual User,
  I want to request a sign-in link sent to my email,
  So that I can authenticate without remembering a password.

  Acceptance Criteria:
  AC1: Given I am on the login page, when I enter a valid email
       address and select "Send magic link," then a one-time sign-in
       link is sent to that email within 30 seconds.
  AC2: Given I enter an email that is not registered, when I select
       "Send magic link," then I see the same confirmation message as
       a valid email (no account enumeration).
  AC3: Given I request multiple magic links in quick succession, when
       I exceed 3 requests in 5 minutes, then further requests are
       rate-limited with a clear message.
  AC4: Given the email delivery service is unavailable, when I
       request a magic link, then I see an error asking me to try
       again later.

  Size:         M
  Dependencies: None
  Notes:        Rate limiting thresholds should be configurable.
                Email template is a sub-task.

Story 5: Magic Link Authentication
  As an Individual User,
  I want to click the sign-in link in my email and be logged in,
  So that I can access my account in a single step.

  Acceptance Criteria:
  AC1: Given I received a valid magic link, when I click it within 15
       minutes of issuance, then I am authenticated and redirected to
       my dashboard.
  AC2: Given I received a magic link, when I click it after 15
       minutes, then I see a message that the link has expired with
       an option to request a new one.
  AC3: Given I have already used a magic link, when I click the same
       link again, then I see a message that the link has already been
       used.
  AC4: Given I click a link with a tampered or invalid token, then I
       see an "Invalid link" error page.

  Size:         S
  Dependencies: Story 4 (Magic Link Request)
  Notes:        Expiry window (15 min) and single-use enforcement are
                non-negotiable security requirements.

Story 6: Password Account Registration
  As an Individual User,
  I want to create an account with my email and a password,
  So that I can sign in with credentials I control.

  Acceptance Criteria:
  AC1: Given I am on the registration page, when I enter a valid
       email and a password meeting the strength requirements, then
       my account is created and I receive a verification email.
  AC2: Given I enter a password shorter than 8 characters or without
       mixed case and a digit, when I submit, then I see a specific
       password-strength error before the form is submitted.
  AC3: Given I enter an email already associated with an account,
       when I submit, then I see a generic message (no account
       enumeration) and the existing user receives a notification
       email.
  AC4: Given I complete registration, when I have not verified my
       email, then I can log in with limited access and see a banner
       prompting verification.

  Size:         M
  Dependencies: None
  Notes:        Password strength requirements should follow OWASP
                guidelines. Verification email template is a sub-task.

Story 7: Password Sign-In
  As an Individual User,
  I want to sign in with my email and password,
  So that I can access my account using my saved credentials.

  Acceptance Criteria:
  AC1: Given I have a registered account, when I enter correct
       credentials, then I am authenticated and redirected to my
       dashboard.
  AC2: Given I enter an incorrect password, when I submit, then I
       see a generic "Invalid email or password" error (no account
       enumeration).
  AC3: Given I fail authentication 5 times consecutively, when I try
       again, then my account is temporarily locked for 15 minutes
       with a clear message.
  AC4: Given my account is locked, when the lockout period expires,
       then I can attempt sign-in again normally.

  Size:         S
  Dependencies: Story 6 (Password Account Registration)
  Notes:        Lockout thresholds and duration should be
                configurable. Brute-force protection is a security
                requirement.

Story 8: Password Reset
  As an Individual User,
  I want to reset my forgotten password via email,
  So that I can regain access to my account without contacting
  support.

  Acceptance Criteria:
  AC1: Given I am on the login page, when I select "Forgot password"
       and enter my email, then a password reset link is sent to that
       email within 30 seconds.
  AC2: Given I click a valid reset link within 1 hour, when I enter
       a new password meeting strength requirements, then my password
       is updated and all existing sessions are invalidated.
  AC3: Given I click a reset link after 1 hour, when the page loads,
       then I see an expiry message with an option to request a new
       reset link.
  AC4: Given I enter an email not associated with an account, when I
       submit the reset request, then I see the same confirmation
       message as a valid email (no account enumeration).
  AC5: Given I have an active SSO-enforced organisation account, when
       I request a password reset, then I see a message directing me
       to contact my IT admin instead.

  Size:         M
  Dependencies: Story 7 (Password Sign-In)
  Notes:        Session invalidation on password change is a security
                requirement. Reset link is single-use.

Story 9: Authentication Method Selection
  As an Individual User,
  I want to see all available sign-in options on one login page,
  So that I can choose the method that is most convenient for me.

  Acceptance Criteria:
  AC1: Given I am not part of an SSO-enforced organisation, when I
       visit the login page, then I see options for SSO, magic link,
       and password sign-in.
  AC2: Given I am part of an SSO-enforced organisation, when I visit
       the login page, then I see only the SSO sign-in option.
  AC3: Given one authentication method's backend service is degraded,
       when I visit the login page, then the degraded method shows a
       "temporarily unavailable" indicator while other methods remain
       functional.

  Size:         S
  Dependencies: Stories 1, 4, 7 (all three flows must exist)
  Notes:        This is the integration story that ties the three
                independent flows together on the login page.

================================================================

COVERAGE ANALYSIS
================================================================

Spec Flows Covered:
  ✓ SSO flow — Stories 1, 2, 3 (configure → test → enforce)
  ✓ Magic link flow — Stories 4, 5 (request → authenticate)
  ✓ Password flow — Stories 6, 7, 8 (register → sign-in → reset)
  ✓ Flow independence — Story 9 (selection page, degradation handling)

Error States Covered:
  ✓ SSO provider unreachable (Stories 1, 2, 3)
  ✓ Magic link expired / reused / tampered (Story 5)
  ✓ Magic link rate limiting (Story 4)
  ✓ Email service unavailable (Story 4)
  ✓ Invalid password / account lockout (Story 7)
  ✓ Reset link expired (Story 8)
  ✓ Account enumeration prevention (Stories 4, 6, 7, 8)
  ✓ SSO enforcement bypass attempt (Story 3)
  ✓ Service degradation on login page (Story 9)

Flagged for Engineering Discussion:
  ⚠ Break-glass admin bypass when SSO enforcement is on (Story 3)
  ⚠ Rate limiting thresholds — configurable vs hardcoded (Stories 4, 7)
  ⚠ Session invalidation strategy on password change (Story 8)

Sprint Estimate:
  Sprint 1: Stories 1, 4, 6 (foundations — SSO config, magic link
            request, password registration — all independent, can
            be parallelised across 3 engineers)
  Sprint 2: Stories 2, 3, 5, 7, 8, 9 (dependent stories — SSO
            test/enforce, magic link auth, password sign-in/reset,
            login page integration)

================================================================
ALL OUTPUTS REQUIRE REVIEW BY THE PM AND ENGINEERING LEAD BEFORE
SPRINT PLANNING.
================================================================
