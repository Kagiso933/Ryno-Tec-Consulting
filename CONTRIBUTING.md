# Contributing to Axiom Infrastructure Business Repository

Thank you for contributing to the Axiom Infrastructure business development! This document outlines how to work with this repository.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Git Workflow](#git-workflow)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Documentation Standards](#documentation-standards)
- [Review Process](#review-process)

---

## 🤝 Code of Conduct

- Treat all collaborators with respect
- Maintain confidentiality of business information
- Focus on quality and accuracy
- Be open to feedback and suggestions

---

## 🚀 Getting Started

### Prerequisites

- Git installed (v2.30 or higher)
- GitHub/GitLab account with access to repository
- Text editor (VS Code recommended)
- Familiarity with Markdown format

### Initial Setup

```bash
# 1. Clone the repository
git clone https://github.com/ryno-tec-consulting/business.git
cd ryno-tec-consulting

# 2. Configure Git (if first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 3. Create local tracking branch
git checkout -b develop origin/develop

# 4. Verify setup
git status
```

---

## 🔄 Git Workflow

### Branch Naming Conventions

Use descriptive branch names with prefixes:

```
feature/   - New features or content
  feature/service-roadmap
  feature/marketing-plan
  
fix/       - Bug fixes or corrections
  fix/financial-projections
  fix/typo-in-services
  
docs/      - Documentation updates
  docs/update-readme
  docs/operations-manual
  
refactor/  - Restructuring content
  refactor/services-organization
```

### Standard Workflow

#### 1. Start a New Feature

```bash
# Update develop branch
git checkout develop
git pull origin develop

# Create feature branch from develop
git checkout -b feature/your-feature-name

# Create corresponding tracking branch
git push -u origin feature/your-feature-name
```

#### 2. Make Changes

```bash
# Edit files
nano docs/business-plan/04-services.md

# Check status
git status

# Stage changes
git add docs/business-plan/04-services.md

# Commit with descriptive message (see below)
git commit -m "feat: Add MLOps consulting service description"

# Push regularly
git push origin feature/your-feature-name
```

#### 3. Create Pull Request

When ready for review:

```bash
# Push final changes
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
# - Title: Clear description of changes
# - Body: Detailed explanation and rationale
# - Link: Reference any related issues
```

#### 4. Address Review Feedback

```bash
# Make requested changes
nano docs/business-plan/04-services.md

# Commit changes
git commit -m "refactor: Incorporate PR feedback on service descriptions"

# Push updates
git push origin feature/your-feature-name

# PR automatically updates with new commits
```

#### 5. Merge to Develop

After approval:

```bash
# Ensure branch is up-to-date
git fetch origin
git merge origin/develop

# Resolve any conflicts if needed
# Then push
git push origin feature/your-feature-name

# Click "Merge" on GitHub
# Choose "Squash and merge" for cleaner history
```

#### 6. Cleanup

```bash
# Delete local branch
git branch -d feature/your-feature-name

# Delete remote branch
git push origin --delete feature/your-feature-name
```

---

## 📝 Commit Guidelines

### Commit Message Format

Use conventional commits for consistency:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat:** New feature or content
- **fix:** Bug fix or correction
- **docs:** Documentation updates
- **refactor:** Restructuring (no functional change)
- **style:** Formatting/style improvements
- **perf:** Performance improvements
- **test:** Test-related changes
- **chore:** Maintenance/tooling changes

### Scope

Optional but recommended. Indicates what area is affected:

```
feat(services): Add AI infrastructure service
feat(financial): Update Year 2 projections
feat(marketing): Create brand guidelines
fix(operations): Correct SLA response times
docs(readme): Add git workflow instructions
```

### Subject

- Use imperative mood ("add" not "added")
- Don't capitalize first letter
- No period at end
- Limit to 50 characters

### Body

Explain what and why (not how). Wrap at 72 characters:

```
feat(services): Add AI infrastructure consulting

Add comprehensive AI Infrastructure service offering covering:
- MLOps pipeline architecture and implementation
- Model deployment and monitoring solutions
- Cloud AI platform optimization (Azure ML, AWS SageMaker)

This addresses market demand from fintech and tech startups
seeking specialized AI infrastructure expertise.
```

### Footer

Reference issues or breaking changes:

```
Closes #42
Relates to #15
BREAKING CHANGE: Service pricing model updated
```

### Examples

```
feat(services): Add MLOps consulting service

docs(readme): Update repository structure documentation

fix(financial): Correct Year 2 EBITDA calculation
- Changed from 28% to 30% margin
- Updated projections spreadsheet accordingly

Closes #12

refactor(business-plan): Reorganize services section
- Move pricing to separate document
- Update service descriptions
- Add service roadmap

chore(config): Update financial configuration parameters
```

---

## 🔍 Pull Request Process

### Before Creating PR

- [ ] Branch created from `develop`
- [ ] All commits follow guidelines
- [ ] Files follow naming conventions
- [ ] Content is accurate and complete
- [ ] Markdown is properly formatted
- [ ] No sensitive data included
- [ ] `.gitignore` respected

### PR Title & Description

**Title Format:**
```
[TYPE] Brief description of changes
Example: [FEAT] Add virtual CIO service offering
```

**Description Template:**
```markdown
## Description
Brief summary of what changed and why.

## Type of Change
- [ ] New feature or content
- [ ] Bug fix or correction
- [ ] Documentation update
- [ ] Restructuring
- [ ] Other: ___

## Scope
Which areas are affected?
- Services
- Financial Models
- Operations
- Marketing
- Other: ___

## Changes Made
- Point 1
- Point 2
- Point 3

## Rationale
Why are these changes important?

## Related Issues
Closes #XX
Relates to #YY

## Checklist
- [ ] Changes are accurate
- [ ] No sensitive data included
- [ ] Follows documentation standards
- [ ] Tested/reviewed locally
```

### Review Standards

- At least one review before merge
- All conversations resolved
- No merge conflicts
- Passes any automated checks

---

## 📖 Documentation Standards

### Markdown Format

```markdown
# Main Heading (H1)

Introduction paragraph explaining section purpose.

## Subheading (H2)

Content describing the topic in detail.

### Sub-subheading (H3)

More specific content or examples.

#### H4 and beyond used sparingly

#### Example

```code
code example
```

> Blockquotes for important notes

- Bullet lists
- For multiple items
- Short descriptions

1. Numbered lists
2. For sequential items
3. Clear ordering
```

### File Organization

- Use H1 (# ) only once per file
- Use H2 (## ) for major sections
- Use H3 (### ) for subsections
- Tables for structured data

### Naming Conventions

- **Directory names:** lowercase-with-hyphens
  - `docs/business-plan/`
  - `docs/financial-models/`
  - `config/`

- **File names:** lowercase-with-hyphens, numbered if sequential
  - `01-executive-summary.md`
  - `market-analysis.md`
  - `pricing-models.md`

- **Internal links:** Use relative paths
  - `[Business Plan](../business-plan/README.md)`
  - `[Services](./SERVICES.md)`

### Content Guidelines

- Clear and concise writing
- Use active voice
- Avoid jargon where possible
- Use South African English (colour, organisation, etc.)
- Ensure accuracy with citations/sources
- Update date in footer when significantly changed

---

## ✅ Review Process

### What Reviewers Check

- **Accuracy:** Verify numbers, dates, claims
- **Consistency:** Align with existing content and strategy
- **Clarity:** Ensure content is understandable
- **Format:** Check Markdown and naming standards
- **Sensitivity:** Ensure no sensitive data exposed
- **Completeness:** Verify all sections are addressed

### Reviewer Responsibilities

- Provide constructive feedback
- Approve or request changes within 3-5 business days
- Tag related issues
- Verify before approving

### Author Responsibilities

- Respond to feedback promptly
- Make requested changes or discuss
- Update PR based on reviews
- Ensure final version is approved

---

## 🔐 Security & Confidentiality

### DO NOT COMMIT

- API keys or credentials
- Passwords or secrets
- Sensitive financial data
- Client-specific information
- Private contract details
- Personal contact information
- Proprietary source code

### Use Instead

- Environment variables (.env files - not committed)
- Secure password managers
- Separate private repositories for sensitive docs
- Encrypted storage for confidential files
- OAuth tokens/secrets management

### Accidental Commits

If sensitive data is accidentally committed:

1. **Never push** to public repository
2. Contact repository owner immediately
3. Remove using `git filter-branch` or similar
4. Invalidate any exposed credentials
5. Document incident

---

## 📞 Questions or Issues?

- Create an issue on GitHub/GitLab
- Contact repository owner: `kagiso@ryno-tec-consulting.co.za`
- Reference relevant sections of this guide

---

## 📜 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-03 | Initial CONTRIBUTING guide |

---

**Last Updated:** 2026-02-03  
**Next Review:** 2026-06-03

Thank you for contributing to Axiom Infrastructure! 🚀
