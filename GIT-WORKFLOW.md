# GIT WORKFLOW GUIDE - Axiom Infrastructure

A practical guide to using Git for managing the Axiom Infrastructure business plan and documentation.

---

## 📁 Repository Structure

```
ryno-tec-consulting/
├── README.md                          # Repository overview
├── CONTRIBUTING.md                    # Contribution guidelines
├── VERSION                            # Current version (0.1.0)
├── .gitignore                         # Git ignore patterns
├── docs/
│   ├── business-plan/
│   │   ├── README.md                 # Business plan index
│   │   ├── 01-executive-summary.md   # ✅ COMPLETED
│   │   ├── 02-company-overview.md    # ✅ COMPLETED
│   │   ├── 03-market-analysis.md     # 🔄 IN PROGRESS
│   │   ├── 04-services.md            # 📋 PLANNED
│   │   ├── 05-marketing-sales.md     # 📋 PLANNED
│   │   ├── 06-operations.md          # 📋 PLANNED
│   │   ├── 07-team-org.md            # 📋 PLANNED
│   │   └── 08-risks-assumptions.md   # 📋 PLANNED
│   ├── financial-models/
│   │   ├── README.md
│   │   ├── projections.md            # 📋 PLANNED
│   │   └── funding-strategy.md       # 📋 PLANNED
│   ├── services/
│   │   └── SERVICES.md               # 📋 PLANNED
│   └── operations/
│       └── README.md                 # 📋 PLANNED
├── config/
│   └── company.yml                   # 📋 PLANNED
└── scripts/
    └── generate-documents.sh         # 📋 PLANNED
```

---

## 🔄 Current Repository Status

### Branches

| Branch | Purpose | Status |
|--------|---------|--------|
| **master** | Production-ready stable releases | Main branch |
| **develop** | Integration branch for features | Development branch |
| **feature/add-company-overview** | Company overview document | In progress |

### Commits

```
17edffc feat(business-plan): Add company overview document
a0620ea chore(init): Initialize repository with initial structure
```

### Current Version
**0.1.0** - Initial business planning phase

---

## 🚀 Getting Started with the Repository

### Clone the Repository

```bash
# If using GitHub/GitLab
git clone https://github.com/ryno-tec-consulting/business.git
cd ryno-tec-consulting

# If using local path
git clone /path/to/ryno-tec-consulting
cd ryno-tec-consulting
```

### Initial Setup

```bash
# Configure Git (one-time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list

# View all branches
git branch -a

# Switch to develop branch
git checkout develop
```

---

## ✅ Completed Documents

### 1. Executive Summary (01-executive-summary.md)
- Business overview and opportunity
- Three-year financial projections
- Founder background and expertise
- Market opportunity and competitive advantages
- Key success factors and risks
- Investment thesis

**Status:** ✅ COMPLETED  
**Size:** ~15 pages equivalent  
**Last Updated:** 2026-02-03

### 2. Company Overview (02-company-overview.md)
- Legal structure and registration
- Founder background (Kagiso Tshukudu)
- Company model and positioning
- Strategic focus areas
- Capitalization and funding
- Growth strategy

**Status:** ✅ COMPLETED  
**Size:** ~12 pages equivalent  
**Last Updated:** 2026-02-03

---

## 📋 In Progress & Planned Documents

### 3. Market Analysis (03-market-analysis.md) - PLANNED
- South African IT market size and growth
- Target market segments
- Competitive landscape analysis
- Market trends and opportunities
- Customer pain points and needs

### 4. Services & Offerings (04-services.md) - PLANNED
- Platform Engineering service details
- Azure Modern Workplace services
- AI Infrastructure & MLOps
- Service delivery models
- Pricing and packaging

### 5. Marketing & Sales Strategy (05-marketing-sales.md) - PLANNED
- Go-to-market strategy
- Brand positioning
- Customer acquisition strategy
- Sales process and cycle
- Partnership strategy

### 6. Operations Plan (06-operations.md) - PLANNED
- Service delivery processes
- Quality assurance
- Technology infrastructure
- Client onboarding
- Team and resource planning

### 7. Team & Organization (07-team-org.md) - PLANNED
- Current team (Kagiso)
- Team structure and hiring plan
- Skills and expertise
- Compensation and benefits
- Organizational growth

### 8. Risk Analysis (08-risks-assumptions.md) - PLANNED
- Key business risks
- Risk mitigation strategies
- Critical assumptions
- Contingency planning
- Success metrics

---

## 🔄 Git Workflow Examples

### Example 1: Creating a Feature Branch for Market Analysis

```bash
# 1. Start with develop branch and ensure latest
git checkout develop
git pull origin develop

# 2. Create feature branch
git checkout -b feature/add-market-analysis

# 3. Create the document
nano docs/business-plan/03-market-analysis.md

# 4. Stage the file
git add docs/business-plan/03-market-analysis.md

# 5. Commit with descriptive message
git commit -m "feat(business-plan): Add market analysis document

- South African IT market overview
- Target market segments analysis
- Competitive landscape
- Market trends and opportunities
- Customer pain points"

# 6. Push feature branch
git push -u origin feature/add-market-analysis
```

### Example 2: Updating a Document with Bug Fix

```bash
# 1. Make sure you're on correct branch
git checkout feature/add-company-overview

# 2. Edit the file to fix issues
nano docs/business-plan/02-company-overview.md

# 3. Check what changed
git diff docs/business-plan/02-company-overview.md

# 4. Stage the changes
git add docs/business-plan/02-company-overview.md

# 5. Commit the fix
git commit -m "fix(company-overview): Correct capitalization and formatting

- Fix heading levels in Company Structure section
- Update table formatting for consistency
- Correct typo in Funding Sources section"

# 6. Push the update
git push origin feature/add-company-overview
```

### Example 3: Merging Feature to Develop

```bash
# 1. Ensure feature branch is pushed and up-to-date
git push origin feature/add-market-analysis

# 2. Switch to develop
git checkout develop

# 3. Pull latest develop
git pull origin develop

# 4. Merge feature branch
git merge feature/add-market-analysis

# 5. Push merged changes
git push origin develop

# 6. Delete feature branch (local)
git branch -d feature/add-market-analysis

# 7. Delete feature branch (remote)
git push origin --delete feature/add-market-analysis
```

### Example 4: Creating a Release from Develop to Master

```bash
# 1. Ensure develop is latest
git checkout develop
git pull origin develop

# 2. Switch to master
git checkout master

# 3. Merge develop into master
git merge --no-ff develop

# 4. Create version tag
git tag -a v0.2.0 -m "Release version 0.2.0 - Market analysis and services complete"

# 5. Push to remote
git push origin master --tags

# 6. Update VERSION file
echo "0.2.0" > VERSION
git add VERSION
git commit -m "chore(version): Bump to 0.2.0"
git push origin master
```

---

## 📝 Commit Message Examples

### Good Commit Messages

```
feat(business-plan): Add market analysis with competitor research

docs(readme): Update repository structure and branch strategy

fix(executive-summary): Correct financial projection for Year 2

refactor(business-plan): Reorganize services section with new structure

chore(config): Update financial configuration parameters
```

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` - New document or feature
- `fix` - Bug fix or correction
- `docs` - Documentation updates
- `refactor` - Restructuring
- `chore` - Maintenance
- `style` - Formatting

**Scope:**
- `business-plan` - Documents in business plan
- `financial` - Financial models
- `services` - Service offerings
- `marketing` - Marketing/sales
- `readme` - Repository README

---

## 🔍 Useful Git Commands

### View Commit History

```bash
# View commit log (one line per commit)
git log --oneline

# View commits with details
git log --oneline --graph

# View commits for specific file
git log -- docs/business-plan/01-executive-summary.md

# View commits by author
git log --author="Kagiso"
```

### View Changes

```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged

# View changes in specific file
git diff docs/business-plan/02-company-overview.md

# View changes in last commit
git show HEAD
```

### Branch Management

```bash
# List all branches
git branch -a

# Create new branch
git checkout -b feature/new-document

# Switch branch
git checkout develop

# Delete branch (local)
git branch -d feature/completed

# Delete branch (remote)
git push origin --delete feature/completed

# Rename branch (local)
git branch -m old-name new-name
```

### Undo Changes

```bash
# Discard changes in working directory
git checkout -- docs/business-plan/file.md

# Unstage a file
git reset HEAD docs/business-plan/file.md

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

---

## 📊 Repository Statistics

### Current State (as of 2026-02-03)

| Metric | Value |
|--------|-------|
| **Total Commits** | 2 |
| **Branches** | 3 (master, develop, feature/...) |
| **Documents** | 2 completed, 6 planned |
| **Repository Size** | ~50KB |
| **Version** | 0.1.0 |

### Progress Tracking

- ✅ **Completed:** 2 documents (~27 pages)
- 🔄 **In Progress:** 0 documents
- 📋 **Planned:** 6 documents (~100+ pages)
- **Overall Progress:** ~20% of business plan complete

---

## 🎯 Next Steps

### Immediate (This Week)
1. Review executive summary and company overview
2. Provide feedback on content and structure
3. Plan market analysis document

### Short Term (Next 2 Weeks)
1. Complete market analysis document (feature/add-market-analysis branch)
2. Create services document (feature/add-services-catalog branch)
3. Merge completed features to develop

### Medium Term (Next Month)
1. Complete remaining business plan sections
2. Develop financial models
3. Create supporting documents (legal templates, etc.)
4. Merge develop branch to master (v0.2.0 release)

---

## 💡 Best Practices

### Do's ✅
- Create feature branches for new content
- Write descriptive commit messages
- Keep commits focused and logical
- Pull latest before starting work
- Use consistent naming conventions
- Test documents locally before committing
- Review changes before committing

### Don'ts ❌
- Don't commit sensitive data (credentials, private keys)
- Don't directly edit master branch
- Don't skip descriptive commit messages
- Don't overwrite others' work
- Don't commit uncommonly large files
- Don't ignore merge conflicts
- Don't push work-in-progress files

---

## 🚨 Troubleshooting

### Merge Conflicts

If you encounter merge conflicts:

```bash
# View conflicting files
git status

# Open conflicting file and resolve manually
nano docs/business-plan/conflicting-file.md

# Mark as resolved
git add docs/business-plan/conflicting-file.md

# Complete merge
git commit -m "Merge: Resolve conflicts in business-plan"
```

### Accidental Commits

If you commit something accidentally:

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Fix the file and recommit
nano docs/file.md
git add docs/file.md
git commit -m "feat(business-plan): Corrected version of previous commit"
```

### Branch Out of Sync

If your branch is behind develop:

```bash
# Fetch latest
git fetch origin

# Rebase on develop
git rebase origin/develop

# Fix any conflicts
# Then continue rebase
git rebase --continue
```

---

## 📞 Support & Questions

- Review CONTRIBUTING.md for detailed guidelines
- Check README.md for repository overview
- Reference git documentation: `git help <command>`
- Contact: kagiso@ryno-tec-consulting.co.za

---

**Document Version:** 1.0  
**Created:** 2026-02-03  
**Last Updated:** 2026-02-03  
**Owner:** Kagiso Tshukudk
