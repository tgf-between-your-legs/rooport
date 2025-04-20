# Git Commands Reference

This reference document provides a comprehensive guide to Git commands commonly used by the Git Manager mode. Each command includes basic syntax, important options, practical examples, and safety considerations where applicable.

## Table of Contents

1. [Repository Information](#repository-information)
   - [git status](#git-status)
   - [git log](#git-log)
   - [git diff](#git-diff)
   - [git show](#git-show)

2. [Basic Operations](#basic-operations)
   - [git init](#git-init)
   - [git add](#git-add)
   - [git commit](#git-commit)
   - [git rm](#git-rm)

3. [Branch Management](#branch-management)
   - [git branch](#git-branch)
   - [git checkout](#git-checkout)
   - [git switch](#git-switch)

4. [Integration](#integration)
   - [git merge](#git-merge)
   - [git rebase](#git-rebase)
   - [git cherry-pick](#git-cherry-pick)

5. [Remote Operations](#remote-operations)
   - [git remote](#git-remote)
   - [git fetch](#git-fetch)
   - [git pull](#git-pull)
   - [git push](#git-push)
   - [git clone](#git-clone)

6. [Advanced Operations](#advanced-operations)
   - [git stash](#git-stash)
   - [git tag](#git-tag)
   - [git reset](#git-reset)
   - [git revert](#git-revert)

7. [Conflict Resolution](#conflict-resolution)
   - [Identifying Conflicts](#identifying-conflicts)
   - [Resolving Conflicts](#resolving-conflicts)
   - [Aborting Operations](#aborting-operations)

---

## Repository Information

### git status

Shows the working tree status, including staged changes, untracked files, and branch information.

**Basic Syntax:**
```bash
git status [options]
```

**Important Options:**
- `-s, --short`: Gives output in short format
- `-b, --branch`: Shows branch information
- `-u, --untracked-files[=mode]`: Shows untracked files (mode: no, normal, all)

**Examples:**
```bash
# Standard status check
git status

# Concise status output
git status -sb
```

**Git Manager Usage:**
Always use this command before performing operations to verify the repository state and ensure you're working in the expected context.

### git log

Shows commit logs with various formatting options.

**Basic Syntax:**
```bash
git log [options]
```

**Important Options:**
- `--oneline`: Compact single-line format
- `-n <number>`: Limits output to last n commits
- `--graph`: Displays ASCII graph of branch and merge history
- `--pretty=format:"<format>"`: Custom formatting
- `--author=<pattern>`: Filter by author
- `--since=<date>`, `--until=<date>`: Filter by date
- `--grep=<pattern>`: Filter by commit message pattern
- `--follow <file>`: Follow file history through renames

**Examples:**
```bash
# View recent commits in compact format
git log --oneline -n 10

# View branch history with graph
git log --graph --oneline --all --decorate

# View commits affecting a specific file
git log --follow -- path/to/file.js
```

**Git Manager Usage:**
Use to verify commit history before operations like rebase or merge, or to find specific commits for cherry-picking.

### git diff

Shows changes between commits, commit and working tree, etc.

**Basic Syntax:**
```bash
git diff [options] [<commit>] [--] [<path>...]
```

**Important Options:**
- `--staged` or `--cached`: Shows changes staged for commit
- `--name-only`: Shows only names of changed files
- `--name-status`: Shows names and status of changed files
- `<commit1>..<commit2>`: Shows changes between two commits

**Examples:**
```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged

# View changes between two commits
git diff HEAD~3..HEAD

# View changes to specific file
git diff -- path/to/file.js
```

**Git Manager Usage:**
Use to inspect changes before committing or to understand differences between branches before merging.

### git show

Shows various types of objects (commits, tags, etc.).

**Basic Syntax:**
```bash
git show [options] <object>...
```

**Important Options:**
- `--name-only`: Shows only names of changed files
- `--name-status`: Shows names and status of changed files

**Examples:**
```bash
# Show the latest commit
git show

# Show a specific commit
git show abc123

# Show a specific file from a commit
git show abc123:path/to/file.js
```

**Git Manager Usage:**
Use to examine specific commits or to view file contents at a particular commit.

---

## Basic Operations

### git init

Creates an empty Git repository or reinitializes an existing one.

**Basic Syntax:**
```bash
git init [options] [directory]
```

**Important Options:**
- `--bare`: Creates a bare repository (no working directory)
- `--template=<template_directory>`: Uses custom template directory

**Examples:**
```bash
# Initialize repository in current directory
git init

# Initialize repository in specified directory
git init path/to/repo
```

**Git Manager Usage:**
Typically used only when setting up new projects. Use with caution as it creates a new repository.

### git add

Adds file contents to the index (staging area).

**Basic Syntax:**
```bash
git add [options] [--] <pathspec>...
```

**Important Options:**
- `-A, --all`: Adds all changes (new, modified, deleted)
- `-u, --update`: Updates only tracked files (no new files)
- `-p, --patch`: Interactively choose hunks to stage
- `-i, --interactive`: Interactive mode

**Examples:**
```bash
# Add specific file
git add path/to/file.js

# Add all files in directory
git add src/

# Add all changed files
git add .

# Add all tracked files with changes
git add -u

# Interactively add parts of files
git add -p
```

**Git Manager Usage:**
Use to stage changes before committing. The `-p` option is useful for creating clean, focused commits.

### git commit

Records changes to the repository.

**Basic Syntax:**
```bash
git commit [options]
```

**Important Options:**
- `-m <message>`: Commit message
- `-a, --all`: Automatically stage modified and deleted files
- `--amend`: Amend previous commit
- `--no-edit`: Use previous commit message when amending
- `--date=<date>`: Override author date

**Examples:**
```bash
# Commit with message
git commit -m "Add feature X"

# Stage all tracked files and commit
git commit -am "Fix bug in feature X"

# Amend previous commit
git commit --amend -m "Updated message"

# Amend previous commit without changing message
git commit --amend --no-edit
```

**Git Manager Usage:**
Use to create commits after staging changes. Be cautious with `--amend` as it rewrites history.

### git rm

Removes files from the working tree and the index.

**Basic Syntax:**
```bash
git rm [options] [--] <file>...
```

**Important Options:**
- `-r`: Recursive removal (for directories)
- `--cached`: Remove only from the index (keep in working directory)
- `-f, --force`: Override safety checks

**Examples:**
```bash
# Remove file from index and working directory
git rm file.txt

# Remove directory recursively
git rm -r directory/

# Remove from index only (keep file in working directory)
git rm --cached file.txt
```

**Git Manager Usage:**
Use to remove files that should no longer be tracked. The `--cached` option is useful when you want to stop tracking a file but keep it locally.

---

## Branch Management

### git branch

Lists, creates, or deletes branches.

**Basic Syntax:**
```bash
git branch [options] [branch-name]
```

**Important Options:**
- `-a, --all`: Lists all branches (local and remote)
- `-r, --remotes`: Lists remote-tracking branches
- `-v, --verbose`: Shows hash and commit subject
- `-d, --delete`: Deletes a branch
- `-D`: Forces branch deletion
- `-m, --move`: Renames a branch
- `--merged`: Lists branches merged into current branch
- `--no-merged`: Lists branches not merged into current branch

**Examples:**
```bash
# List all local branches
git branch

# List all branches (local and remote)
git branch -a

# Create a new branch (without switching to it)
git branch feature/login

# Delete a branch
git branch -d feature/login

# Force delete a branch
git branch -D feature/login

# Rename current branch
git branch -m new-name
```

**Git Manager Usage:**
Use to manage branches. Always verify branch existence and state before operations. Be cautious with `-D` as it forces deletion even if changes aren't merged.

### git checkout

Switches branches or restores working tree files.

**Basic Syntax:**
```bash
git checkout [options] <branch>
git checkout [options] -- <file>...
```

**Important Options:**
- `-b <new-branch>`: Creates and switches to a new branch
- `-B <new-branch>`: Creates/resets and switches to a branch
- `-t, --track`: Sets up tracking mode
- `--orphan <new-branch>`: Creates a new orphan branch
- `-f, --force`: Forces checkout (discards local changes)

**Examples:**
```bash
# Switch to existing branch
git checkout develop

# Create and switch to new branch
git checkout -b feature/login

# Create branch tracking remote branch
git checkout -t origin/feature/login

# Discard changes to a file
git checkout -- file.js

# Create orphan branch (no parent commit)
git checkout --orphan new-branch
```

**Git Manager Usage:**
Use to switch between branches or restore files. Be cautious with `-f` as it discards local changes. Note that `git switch` is now preferred for branch operations.

### git switch

Switches branches (modern alternative to git checkout for branch operations).

**Basic Syntax:**
```bash
git switch [options] <branch>
```

**Important Options:**
- `-c, --create <new-branch>`: Creates and switches to a new branch
- `-C, --force-create <new-branch>`: Forces creation/reset of branch
- `--detach [<start-point>]`: Switches to detached HEAD state
- `--track, --no-track`: Controls branch tracking behavior

**Examples:**
```bash
# Switch to existing branch
git switch main

# Create and switch to new branch
git switch -c feature/login

# Force create/reset branch
git switch -C feature/login

# Switch to detached HEAD
git switch --detach HEAD~3
```

**Git Manager Usage:**
Preferred over `git checkout` for branch operations as it's more focused and has clearer semantics.

---

## Integration

### git merge

Joins two or more development histories together.

**Basic Syntax:**
```bash
git merge [options] [<commit>...]
```

**Important Options:**
- `--no-ff`: Creates a merge commit even if fast-forward is possible
- `--ff-only`: Refuses to merge unless fast-forward is possible
- `--squash`: Squashes all commits into a single commit
- `--abort`: Aborts the current merge
- `--continue`: Continues after resolving conflicts
- `-m <message>`: Sets the commit message
- `-s <strategy>`: Chooses merge strategy

**Examples:**
```bash
# Merge branch into current branch
git merge feature/login

# Merge with commit even if fast-forward possible
git merge --no-ff feature/login

# Merge only if fast-forward possible
git merge --ff-only feature/login

# Squash merge (combine all commits)
git merge --squash feature/login

# Abort a merge with conflicts
git merge --abort
```

**Git Manager Usage:**
Use to integrate changes from one branch into another. Be prepared to handle conflicts. For complex merges, consider using `--no-ff` for clearer history.

### git rebase

Reapplies commits on top of another base.

**Basic Syntax:**
```bash
git rebase [options] [<upstream> [<branch>]]
```

**Important Options:**
- `-i, --interactive`: Interactive mode for editing commits
- `--onto <newbase>`: Rebases onto a new base
- `--continue`: Continues after resolving conflicts
- `--abort`: Aborts the rebase
- `--skip`: Skips current patch
- `--exec <cmd>`: Executes command after each commit

**Examples:**
```bash
# Rebase current branch onto main
git rebase main

# Interactive rebase for editing commits
git rebase -i HEAD~5

# Rebase feature branch onto specific commit
git rebase --onto commit123 old-base feature-branch

# Continue rebase after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort
```

**⚠️ Safety Considerations:**
- Rebasing rewrites commit history, which can cause issues for collaborators
- Never rebase commits that have been pushed to a public repository
- Always confirm with the user before rebasing
- Be prepared to handle conflicts

**Git Manager Usage:**
Use with caution as it rewrites history. Always confirm with the user before rebasing public branches. Useful for cleaning up commit history before merging.

### git cherry-pick

Applies changes from specific commits to the current branch.

**Basic Syntax:**
```bash
git cherry-pick [options] <commit>...
```

**Important Options:**
- `-e, --edit`: Edits commit message before committing
- `-n, --no-commit`: Applies changes without committing
- `-x`: Appends cherry-pick source to commit message
- `--continue`: Continues after resolving conflicts
- `--abort`: Aborts the cherry-pick
- `--skip`: Skips current commit

**Examples:**
```bash
# Apply a single commit to current branch
git cherry-pick abc123

# Apply multiple commits
git cherry-pick abc123 def456

# Apply changes without committing
git cherry-pick -n abc123

# Continue cherry-pick after resolving conflicts
git cherry-pick --continue
```

**Git Manager Usage:**
Use to apply specific commits from one branch to another. Useful for backporting fixes or features.

---

## Remote Operations

### git remote

Manages set of tracked repositories.

**Basic Syntax:**
```bash
git remote [options] <subcommand>
```

**Important Options:**
- `-v, --verbose`: Shows URLs for remotes

**Subcommands:**
- `add <name> <url>`: Adds a remote
- `remove <name>`: Removes a remote
- `rename <old> <new>`: Renames a remote
- `set-url <name> <url>`: Changes remote URL
- `show <name>`: Shows information about a remote

**Examples:**
```bash
# List all remotes
git remote -v

# Add a remote
git remote add origin https://github.com/user/repo.git

# Change remote URL
git remote set-url origin https://github.com/user/new-repo.git

# Remove a remote
git remote remove upstream
```

**Git Manager Usage:**
Use to manage connections to remote repositories. Always verify remote URLs before operations.

### git fetch

Downloads objects and refs from another repository.

**Basic Syntax:**
```bash
git fetch [options] [<repository> [<refspec>...]]
```

**Important Options:**
- `-a, --all`: Fetches from all remotes
- `-p, --prune`: Removes remote-tracking branches that no longer exist
- `--tags`: Fetches all tags
- `--depth=<depth>`: Limits history depth

**Examples:**
```bash
# Fetch from default remote (origin)
git fetch

# Fetch from specific remote
git fetch upstream

# Fetch all remotes
git fetch --all

# Fetch and prune deleted branches
git fetch -p

# Fetch specific branch
git fetch origin feature/login
```

**Git Manager Usage:**
Use to update local references to remote branches without merging. Safe operation that doesn't modify working directory.

### git pull

Fetches from and integrates with another repository or branch.

**Basic Syntax:**
```bash
git pull [options] [<repository> [<refspec>...]]
```

**Important Options:**
- `--ff-only`: Only fast-forward
- `--no-ff`: Always create merge commit
- `--rebase[=preserve]`: Rebase instead of merge
- `--autostash`: Automatically stash/unstash
- `-p, --prune`: Prunes remote-tracking branches

**Examples:**
```bash
# Pull from default remote/branch
git pull

# Pull from specific remote/branch
git pull origin develop

# Pull with rebase instead of merge
git pull --rebase

# Pull only if fast-forward possible
git pull --ff-only
```

**Git Manager Usage:**
Use to fetch and integrate remote changes. Consider using `--ff-only` for safety or `--rebase` for cleaner history.

### git push

Updates remote refs along with associated objects.

**Basic Syntax:**
```bash
git push [options] [<repository> [<refspec>...]]
```

**Important Options:**
- `-u, --set-upstream`: Sets upstream for branch
- `--force`: Forces update (⚠️ destructive)
- `--force-with-lease`: Forces update if remote ref hasn't changed
- `--tags`: Pushes all tags
- `--delete`: Deletes remote branch or tag
- `--all`: Pushes all branches

**Examples:**
```bash
# Push current branch to default remote
git push

# Push and set upstream
git push -u origin feature/login

# Push all branches
git push --all

# Push tags
git push --tags

# Delete remote branch
git push origin --delete feature/old
```

**⚠️ Safety Considerations:**
- `--force` overwrites remote history and can cause problems for collaborators
- Always confirm with the user before using `--force`
- Consider `--force-with-lease` as a safer alternative to `--force`

**Git Manager Usage:**
Use to publish local changes to remote repositories. Always confirm before using force options.

### git clone

Clones a repository into a new directory.

**Basic Syntax:**
```bash
git clone [options] <repository> [<directory>]
```

**Important Options:**
- `--branch, -b <name>`: Checks out specific branch
- `--depth <depth>`: Creates shallow clone with specified depth
- `--single-branch`: Clones only one branch
- `--recurse-submodules`: Initializes submodules

**Examples:**
```bash
# Clone repository
git clone https://github.com/user/repo.git

# Clone to specific directory
git clone https://github.com/user/repo.git my-project

# Clone specific branch
git clone -b develop https://github.com/user/repo.git

# Shallow clone (faster for large repos)
git clone --depth=1 https://github.com/user/repo.git
```

**Git Manager Usage:**
Use to create a local copy of a remote repository. Typically used only when setting up new projects.

---

## Advanced Operations

### git stash

Stashes changes in a dirty working directory.

**Basic Syntax:**
```bash
git stash [<subcommand>]
```

**Subcommands:**
- `save [<message>]`: Saves changes to stash (default if no subcommand)
- `list`: Lists stashes
- `show [<stash>]`: Shows stash contents
- `pop [<stash>]`: Applies and removes stash
- `apply [<stash>]`: Applies stash without removing
- `drop [<stash>]`: Removes stash
- `clear`: Removes all stashes
- `branch <branchname> [<stash>]`: Creates branch from stash

**Examples:**
```bash
# Stash current changes
git stash

# Stash with message
git stash save "WIP: feature implementation"

# List stashes
git stash list

# Apply and remove most recent stash
git stash pop

# Apply specific stash without removing
git stash apply stash@{2}

# Create branch from stash
git stash branch feature/from-stash
```

**Git Manager Usage:**
Use to temporarily save changes when switching contexts. Useful before pulling or checking out branches.

### git tag

Creates, lists, deletes, or verifies tags.

**Basic Syntax:**
```bash
git tag [options] <tagname> [<commit>]
```

**Important Options:**
- `-a, --annotated`: Creates annotated tag
- `-m <message>`: Tag message
- `-d, --delete`: Deletes tag
- `-l, --list [<pattern>]`: Lists tags
- `--contains <commit>`: Lists tags containing commit
- `-f, --force`: Forces tag creation

**Examples:**
```bash
# List all tags
git tag

# Create lightweight tag
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# Tag specific commit
git tag -a v1.0.0 -m "Version 1.0.0" abc123

# Delete tag
git tag -d v1.0.0

# Push tags to remote
git push origin --tags
```

**Git Manager Usage:**
Use to mark specific points in history, typically for releases. Annotated tags are preferred for releases as they contain more metadata.

### git reset

Resets current HEAD to specified state.

**Basic Syntax:**
```bash
git reset [options] [<commit>] [--] [<paths>...]
```

**Important Options:**
- `--soft`: Keeps changes staged
- `--mixed`: Unstages changes (default)
- `--hard`: Discards changes (⚠️ destructive)
- `--merge`: Resets while keeping local changes
- `--keep`: Like --hard but keeps uncommitted local changes

**Examples:**
```bash
# Unstage all changes
git reset

# Unstage specific file
git reset -- file.js

# Move HEAD to previous commit, keep changes staged
git reset --soft HEAD~1

# Move HEAD to previous commit, unstage changes
git reset --mixed HEAD~1

# Move HEAD to previous commit, discard changes
git reset --hard HEAD~1
```

**⚠️ Safety Considerations:**
- `--hard` discards all uncommitted changes and can cause data loss
- Always confirm with the user before using `--hard`
- Consider creating a backup branch before destructive operations

**Git Manager Usage:**
Use with caution, especially with `--hard`. Useful for undoing commits or unstaging changes.

### git revert

Creates new commit that undoes changes from a previous commit.

**Basic Syntax:**
```bash
git revert [options] <commit>...
```

**Important Options:**
- `-e, --edit`: Edits commit message
- `-n, --no-commit`: Reverts but doesn't commit
- `--no-edit`: Uses default message
- `--continue`: Continues after resolving conflicts
- `--abort`: Aborts the revert

**Examples:**
```bash
# Revert most recent commit
git revert HEAD

# Revert specific commit
git revert abc123

# Revert multiple commits
git revert abc123 def456

# Revert without committing
git revert -n HEAD
```

**Git Manager Usage:**
Safer alternative to `reset` when changes have been pushed, as it preserves history. Creates a new commit that undoes changes rather than rewriting history.

---

## Conflict Resolution

### Identifying Conflicts

Git marks conflicts in files with conflict markers:

```
<<<<<<< HEAD
Current branch content
=======
Incoming branch content
>>>>>>> branch-name
```

**Commands to identify conflicts:**
```bash
# Show conflicted files
git status

# Show conflict details
git diff
```

### Resolving Conflicts

1. **Manual Resolution:**
   - Edit files to remove conflict markers and choose desired content
   - Use visual tools if available (`git mergetool`)

2. **Mark as Resolved:**
```bash
# After editing, stage resolved file
git add <file>

# Continue the operation
git merge --continue
# or
git rebase --continue
# or
git cherry-pick --continue
```

3. **Using Merge Strategies:**
```bash
# Choose specific version (ours/theirs)
git checkout --ours <file>   # Keep current branch version
git checkout --theirs <file> # Keep incoming branch version
git add <file>
```

### Aborting Operations

If conflicts are too complex to resolve:

```bash
# Abort merge
git merge --abort

# Abort rebase
git rebase --abort

# Abort cherry-pick
git cherry-pick --abort
```

**Git Manager Usage:**
For simple conflicts, attempt resolution using the strategies above. For complex conflicts, abort the operation and escalate to the user or appropriate specialist.

---

## Best Practices for Git Manager

1. **Always verify context before operations:**
   ```bash
   git status
   git branch -v
   git remote -v
   ```

2. **Confirm before destructive operations:**
   - Force push: `git push --force`
   - Hard reset: `git reset --hard`
   - Rebase: `git rebase`

3. **Create backup branches before risky operations:**
   ```bash
   git branch backup/feature-name
   ```

4. **Use safer alternatives when possible:**
   - `--force-with-lease` instead of `--force`
   - `revert` instead of `reset` for public branches
   - `merge` instead of `rebase` for public branches

5. **Keep commit messages clear and descriptive:**
   ```bash
   git commit -m "feat: Add user authentication system"
   ```

6. **Log all operations and their outcomes in the task journal.**

7. **Escalate complex conflicts or authentication issues to the appropriate specialist or user.**