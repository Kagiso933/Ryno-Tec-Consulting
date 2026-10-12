# Git Workflow

This document outlines the Git workflow for Ryno-Tec Consulting repository.

## Branch Strategy

### Main Branches

- **`main`** - Production-ready code and documents
  - Stable, tested, release-ready
  - Protected: requires pull request review
  - Tagged with semantic versions

- **`develop`** - Development branch
  - Integration branch for features
  - Staging for next release
  - Can be unstable

### Supporting Branches

- **`feature/*`** - New features or documentation
  - Created from: `develop`
  - Merged back into: `develop`
  - Naming: `feature/add-market-analysis`, `feature/update-website`

- **`bugfix/*`** - Bug fixes
  - Created from: `develop`
  - Merged back into: `develop`
  - Naming: `bugfix/fix-revenue-projections`

- **`release/*`** - Release preparation
  - Created from: `develop`
  - Merged into: `main` and back to `develop`
  - Naming: `release/1.1.0`

- **`hotfix/*`** - Critical production fixes
  - Created from: `main`
  - Merged into: `main` and `develop`
  - Naming: `hotfix/critical-document-error`

## Workflow Steps

### Creating a Feature Branch

```bash
# Update develop
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Commit changes
git add .
git commit -m "docs: Add feature description

Detailed explanation of changes.

- Bullet point 1
- Bullet point 2"

# Push to remote
git push origin feature/your-feature-name
```

### Creating a Pull Request

1. Push your branch to GitHub
2. Open Pull Request on GitHub
3. Provide clear title and description
4. Request review from maintainers
5. Address feedback
6. Merge when approved

### Merging to Main

```bash
# Create release branch
git checkout -b release/1.1.0 develop

# Update version number, docs
# Commit changes
git commit -m "release: Prepare version 1.1.0"

# Merge to main
git checkout main
git pull origin main
git merge --no-ff release/1.1.0
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main --tags

# Merge back to develop
git checkout develop
git merge --no-ff release/1.1.0
git push origin develop

# Delete release branch
git branch -d release/1.1.0
git push origin --delete release/1.1.0
```

## Commit Message Format

### Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation changes
- **style:** Code style (formatting, missing semicolons, etc)
- **refactor:** Code refactoring
- **test:** Adding or updating tests
- **chore:** Build process, dependencies, version numbers

### Subject
- Use imperative mood ("add" not "added")
- Start with lowercase
- Do not end with period
- Limit to 50 characters

### Body (Optional)
- Explain what and why, not how
- Wrap at 72 characters
- Separated from subject by blank line

### Footer (Optional)
- Reference issues: `Fixes #123`
- Breaking changes: `BREAKING CHANGE: description`

### Examples

Good:
```
docs: Add market analysis section

Add comprehensive market analysis covering:
- Market size and TAM
- Competitive landscape
- Target customer segments
- Growth projections

Fixes #42
```

Good:
```
feat: Implement new service offerings

Expand service portfolio with professional services
including solution architecture, training, and advisory.

- Add professional services documentation
- Update service matrix
- Revise revenue model
```

Avoid:
```
Updated stuff
Fixed bugs
Changed docs
```

## Best Practices

1. **Commit Early & Often**
   - Logical, atomic commits
   - Each commit should be independently valid
   - Easy to review and revert if needed

2. **Write Clear Messages**
   - Future you will thank present you
   - Helps with Git history archaeology
   - Important for team collaboration

3. **Pull Before Pushing**
   ```bash
   git pull origin feature-branch
   git push origin feature-branch
   ```

4. **Never Force Push to Shared Branches**
   - `main` and `develop` should never be force-pushed
   - Only force push to your own feature branches if absolutely necessary

5. **Keep Branches Up to Date**
   ```bash
   git fetch origin
   git rebase origin/develop
   ```

6. **Delete Merged Branches**
   ```bash
   git branch -d feature-branch
   git push origin --delete feature-branch
   ```

## Review Process

### As Author
- Keep PRs focused and reasonably sized
- Respond to review comments promptly
- Push changes for review as new commits
- Thank reviewers for feedback

### As Reviewer
- Review for clarity and correctness
- Ask questions if unclear
- Suggest improvements constructively
- Approve when satisfied
- Use GitHub's review features

## Troubleshooting

### Accidentally committed to wrong branch?
```bash
git reset HEAD~1
git checkout -b correct-branch
git commit -m "your message"
```

### Need to undo last commit?
```bash
# Keep changes
git reset --soft HEAD~1

# Discard changes
git reset --hard HEAD~1
```

### Merge conflicts?
```bash
# See conflicts
git status

# Edit files to resolve
# Then
git add .
git commit -m "Resolve merge conflicts"
```

## Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Semantic Commit Messages](https://www.conventionalcommits.org/)
- [Git Documentation](https://git-scm.com/doc)

---

**Last Updated:** October 2026
