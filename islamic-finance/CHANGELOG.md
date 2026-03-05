# Changelog

All notable changes to the Islamic Finance Domain Agents plugin.

## [2.0.0] - 2026-03-05

### Added
- Plugin manifest (`.claude-plugin/plugin.json`) for Claude Code / Cowork auto-discovery
- 4 slash commands: `/if-journal`, `/if-compare`, `/if-screen`, `/if-zakat`
- SessionStart hook for capability announcement
- PostToolUse hook for framework label validation
- Routing validation script (`scripts/validate-routing.py`)
- Golden-file eval suite (13 routing + 6 product test cases)
- Marketplace integration (`agentfactory-business`)

### Changed
- Migrated from standalone repo (`islamic-finance-domain-agents`) to marketplace monorepo
- Restructured skills to Agent Skills spec format (`skills/<name>/SKILL.md`)
- Moved jurisdiction overlays under router as references (progressive disclosure)
- Inlined istisna'a content (removed two-hop redirect from salam.md)

### Previous
- v1.0.0 was the original companion repo at `panaversity/islamic-finance-domain-agents` (content archive, no plugin infrastructure)
