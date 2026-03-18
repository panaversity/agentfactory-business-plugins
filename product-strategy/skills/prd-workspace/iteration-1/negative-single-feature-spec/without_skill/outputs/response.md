# Feature Spec: Dark Mode Toggle

## Overview

Add a dark mode toggle to the settings page that allows users to switch between light and dark themes. The preference should persist across sessions and respect the user's system preference as the default.

## Motivation

Users frequently work in low-light environments and have requested dark mode support. Most modern applications offer this as a standard accessibility and comfort feature. A dark theme reduces eye strain, improves readability in dim conditions, and can reduce battery consumption on OLED displays.

## User Stories

- As a user, I want to toggle between light and dark mode from the settings page so I can choose the theme that's most comfortable for me.
- As a user, I want my theme preference to persist across sessions so I don't have to set it every time I visit.
- As a user, I want the app to default to my operating system's theme preference so it matches my other applications out of the box.

## Requirements

### Functional Requirements

1. **Toggle Control**: A toggle switch on the settings page with three options: Light, Dark, System (default).
2. **Immediate Application**: Theme changes apply instantly without requiring a page reload.
3. **Persistence**: The selected preference is saved to the user's profile (authenticated users) or localStorage (unauthenticated users).
4. **System Preference Detection**: When set to "System," the app uses `prefers-color-scheme` media query and responds to OS-level changes in real time.
5. **Default Behavior**: New users default to "System." If the system preference cannot be detected, fall back to Light.

### Non-Functional Requirements

1. **Performance**: Theme switch must complete in under 100ms with no visible flash of unstyled content (FOUC).
2. **Accessibility**: Both themes must meet WCAG 2.1 AA contrast ratios (minimum 4.5:1 for normal text, 3:1 for large text).
3. **Compatibility**: Support the same browser matrix as the rest of the application.

## Design

### Settings Page UI

- Location: Settings > Appearance section
- Control: Three-option segmented control (Light | Dark | System)
- Preview: A small inline preview swatch showing the selected theme's primary colors

### Theme Implementation

- Use CSS custom properties (variables) for all theme-sensitive colors.
- Define two token sets: `light` and `dark`, applied via a `data-theme` attribute on `<html>`.
- Existing component styles should reference the CSS variables rather than hardcoded color values.

### Token Examples

| Token                   | Light       | Dark        |
|-------------------------|-------------|-------------|
| `--color-bg-primary`    | `#FFFFFF`   | `#1A1A2E`   |
| `--color-bg-secondary`  | `#F5F5F5`   | `#16213E`   |
| `--color-text-primary`  | `#1A1A2E`   | `#E8E8E8`   |
| `--color-text-secondary`| `#6B7280`   | `#9CA3AF`   |
| `--color-border`        | `#E5E7EB`   | `#2D3748`   |
| `--color-accent`        | `#3B82F6`   | `#60A5FA`   |

*Final token values to be confirmed with design.*

## Technical Approach

1. **Theme Provider**: Create a React context (`ThemeProvider`) that wraps the app, manages the current theme state, and applies the `data-theme` attribute.
2. **Persistence Layer**: On login, sync localStorage preference to user profile. On logout, retain localStorage value.
3. **SSR/Hydration**: Inject a blocking `<script>` in `<head>` that reads the preference before React hydrates, preventing FOUC.
4. **Migration**: Audit existing styles for hardcoded colors and replace with CSS variable references. This is the bulk of the work.

## Scope

### In Scope

- Settings page toggle (Light / Dark / System)
- CSS variable token system for light and dark themes
- Theme persistence (localStorage + user profile)
- System preference detection and real-time sync
- Migration of existing component styles to CSS variables
- FOUC prevention

### Out of Scope

- Custom/user-defined themes beyond light and dark
- Per-page or per-component theme overrides
- Dark mode for emails or exported/printed content
- Third-party embed theming (these inherit their own styles)

## Success Criteria

- [ ] Toggle on settings page switches between Light, Dark, and System
- [ ] Theme applies immediately without page reload or FOUC
- [ ] Preference persists across browser sessions
- [ ] "System" option tracks OS-level changes in real time
- [ ] All pages pass WCAG 2.1 AA contrast checks in both themes
- [ ] No visual regressions in existing light theme after migration to CSS variables
- [ ] Page load performance (LCP) does not regress by more than 50ms

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Hardcoded colors missed during migration | Medium | Medium | Lint rule to flag hex/rgb values outside CSS variables; visual regression tests |
| FOUC on first load | Medium | High | Blocking inline script reads preference before paint |
| Third-party components ignore theme | Low | Low | Document as known limitation; address case-by-case post-launch |
| Contrast ratio violations in dark theme | Medium | High | Automated contrast checks in CI; design review before merge |

## Estimated Effort

**Total: ~1 sprint (2 weeks)**

| Task | Estimate |
|------|----------|
| Theme provider + context + persistence | 2 days |
| CSS variable token system + FOUC prevention | 1 day |
| Settings page UI (toggle + preview) | 1 day |
| Style migration (audit + replace hardcoded colors) | 3-4 days |
| Testing (unit, visual regression, accessibility) | 2 days |
| Design review + polish | 1 day |

## Open Questions

1. Should the toggle also be accessible from a quick-access location (e.g., header/navbar) in addition to settings?
2. Are there any brand guidelines constraining the dark palette?
3. Do we need analytics events for theme switches (to track adoption)?
