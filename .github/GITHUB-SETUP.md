# GitHub Repository Setup Guide

This guide outlines how to configure GitHub features for Ryno-Tec Consulting.

## 🔧 GitHub Pages Configuration

GitHub Pages is already configured to deploy from the `main` branch.

### Custom Domain Setup
The repository is configured to deploy to `ryno-tec.co.za` via the `CNAME` file in the GitHub Actions workflow.

**To enable:**
1. Go to **Settings > Pages**
2. Source: Deploy from a branch
3. Branch: `main` / folder: `docs`
4. Custom domain: `ryno-tec.co.za`
5. Enforce HTTPS: ✅ Enabled

### Website Access
- **GitHub Pages:** https://kagiso933.github.io/Ryno-Tec-Consulting
- **Custom Domain:** https://ryno-tec.co.za

---

## 🎯 GitHub Issues for Business Milestones

Create these issues to track business progress:

### Phase 1: Launch & Foundation (Q1 2027)
```
Title: Phase 1 - Launch & Foundation
Labels: milestone, q1-2027
Assignee: Kagiso933
Description:
- [ ] Business setup and CIPC registration (complete Q4 2026)
- [ ] Launch operations (January 2027)
- [ ] Initiate customer acquisition
- [ ] Begin project delivery
Target: Acquire 2-3 initial clients, R2M revenue
```

### Phase 2: Ramp & Proof of Concept (Q2 2027)
```
Title: Phase 2 - Ramp & Proof of Concept
Labels: milestone, q2-2027
Assignee: Kagiso933
Description:
- [ ] Complete 2-3 initial projects
- [ ] Build case studies and testimonials
- [ ] Refine service delivery processes
- [ ] Reach 4-6 clients
Target: R3.5M revenue
```

### Phase 3: Break-Even & Scale (Q3-Q4 2027)
```
Title: Phase 3 - Break-Even & Scale
Labels: milestone, q3-q4-2027
Assignee: Kagiso933
Description:
- [ ] Scale to 8-12 clients
- [ ] Achieve break-even (Q3 2027)
- [ ] Establish market reputation
- [ ] Begin Year 2 planning
- [ ] Start team hiring process
Target: R7M Q3-Q4 revenue, positive cash flow, R12.5M Year 1 total
```

### Ongoing
```
Title: Client Acquisition - Year 1
Labels: ongoing, business-dev
Target: 8-12 clients by Q3 2027
```

---

## 📊 GitHub Projects Setup

Create a GitHub Project called **"Ryno-Tec 2026 Roadmap"** with these columns:

1. **Backlog** - Future work items
2. **This Quarter** - Current quarter focus
3. **In Progress** - Active work
4. **Review** - Ready for review
5. **Done** - Completed

### Example Cards (Q4 2026)
- Client acquisition (warm outreach, partnerships)
- Service delivery (initial project execution)
- Marketing content (blog, GitHub presence)
- Infrastructure setup (CI/CD, monitoring)

---

## 🚀 GitHub Actions Workflows

### 1. Deploy Workflow (`.github/workflows/deploy.yml`)
**Triggers:** Push to `main` or `develop`, Pull requests

**What it does:**
- Builds documentation
- Deploys to GitHub Pages
- Updates custom domain CNAME

**Status:** ✅ Configured

### 2. Suggested: Documentation Check (New)
```yaml
name: Documentation Check
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check Markdown
        run: npx markdownlint-cli2 "docs/**/*.md"
      - name: Check links
        run: npx markdown-link-check "docs/**/*.md"
```

---

## 📝 Branch Protection Rules

Set up branch protection on `main`:

1. **Settings > Branches > Branch protection rules**
2. Create rule for `main`:
   - ✅ Require pull request reviews before merging
   - ✅ Dismiss stale pull request approvals
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging

---

## 🏷️ Labels for Organization

Create these labels:

| Label | Color | Description |
|-------|-------|-------------|
| `milestone` | Purple | Business milestone |
| `business-dev` | Blue | Business development |
| `technical` | Green | Technical work |
| `documentation` | Yellow | Docs/content |
| `client-work` | Red | Client project |
| `q4-2026` | Orange | Q4 2026 |
| `q1-2027` | Orange | Q1 2027 |

---

## 📋 Releases & Versioning

Use semantic versioning:
- **1.0.0** - Initial business launch (Q4 2026)
- **1.1.0** - First client success case study (Q1 2027)
- **1.2.0** - Break-even milestone (Q2 2027)
- **2.0.0** - Year 2 expansion (Q4 2027)

Create releases in GitHub:
```
Title: Ryno-Tec Consulting 1.0.0 - Launch Edition
Tag: v1.0.0
Description: Initial business launch with website and documentation
```

---

## ✅ Implementation Checklist

- [ ] Enable GitHub Pages
- [ ] Configure custom domain (ryno-tec.co.za)
- [ ] Create milestone Issues (Phase 1, 2, 3)
- [ ] Create GitHub Project board
- [ ] Set up branch protection on `main`
- [ ] Create labels
- [ ] Add GitHub Actions workflows
- [ ] Create initial release (v1.0.0)
- [ ] Update repository description
- [ ] Add repository topics: `consulting`, `infrastructure`, `platform-engineering`, `azure`, `south-africa`

---

**Last Updated:** 2026-10-12  
**Maintained by:** Kagiso Tshukudu
