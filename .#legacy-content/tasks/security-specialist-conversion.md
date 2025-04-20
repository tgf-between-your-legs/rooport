# Task Log: Security Specialist Conversion

**Goal:** Process the `security-specialist.md` file from `v7.0/modes/md/` and migrate it to the appropriate location following the v7.0 mode conventions.

**Subject:** Mode file migration and standardization
**Audience:** Project team
**Purpose:** Document the process of converting the security-specialist mode file to the new format and location
**References:** 
- `v7.0/modes/md/security-specialist.md` (source file)
- `v7.0/templates/mode_template.md` (template)
- `v7.0/templates/mode_hierarchy.md` (hierarchy guide)
- `v7.0/templates/mode_folder_structure.md` (folder structure guide)
- `v7.0/templates/mode_classification_guide.md` (classification guide)
- `project_journal/decisions/20251104-mode_convention_final_refinement.md` (final convention ADR)
- `project_journal/decisions/20251104-mode_file_format_confirmation.md` (format confirmation ADR)
- `project_journal/decisions/20251104-mode_file_conventions_refinement.md` (conventions refinement ADR)

## Process Steps

### 1. Review Source File

Reviewed the source file `v7.0/modes/md/security-specialist.md`. The file contains:
- Mode name: 🛡️ Security Specialist
- Mode slug: security-specialist
- Description, capabilities, and workflow sections
- Role definition
- Custom instructions with detailed workflow steps
- Metadata including tool groups, tags, and API configuration

### 2. Determine Classification and Target Location

Based on the mode classification guide:
- The security-specialist mode is primarily focused on executing security-related tasks (identifying vulnerabilities, implementing security controls, conducting assessments)
- This places it at Level 3: `03x-worker`
- Given its focus on security across applications and infrastructure, it fits best in the cross-functional department: `039-cross-functional`

Therefore, the target folder structure should be:
`v7.0/modes/03x-worker/039-cross-functional/security-specialist/`

And following the latest filename convention from the final refinement ADR, the filename should be:
`039-work-xf-security-specialist.mode.md`

### 3. Create Target Folder and Prepare File

Created the target folder structure:
```
v7.0/modes/03x-worker/039-cross-functional/security-specialist/
```

### 4. Create Updated Mode File

Created the updated mode file at the target location:
`v7.0/modes/03x-worker/039-cross-functional/security-specialist/039-work-xf-security-specialist.mode.md`

The following updates were made to the file:
- Maintained the original content structure
- Updated the metadata section to include:
  - Level: 039-worker-cross-functional
  - Categories: Cross-Functional, Security
  - Stack: Security
  - Delegates To, Escalates To, and Reports To fields
- Formatted the API Configuration according to the latest convention (simple YAML list)
- Ensured all tags and tool groups use standard YAML list format without quotes

### 5. Verification

Verified that the new file follows all the conventions specified in the ADRs:
- Correct folder structure following the hierarchy guide
- Filename using the hyphenated convention: `[level_prefix]-[department_shortcode]-[mode_slug].mode.md`
- Proper metadata formatting
- API Configuration using simple YAML list format

### 6. Delete Original Source File

Deleted the original source file:
```
v7.0/modes/md/security-specialist.md
```

---

**Status:** ✅ Complete
**Outcome:** Success
**Summary:** Successfully migrated the security-specialist mode file to the new location and format. The file is now available at `v7.0/modes/03x-worker/039-cross-functional/security-specialist/039-work-xf-security-specialist.mode.md` and follows all the conventions specified in the ADRs. The original source file has been deleted.
**References:** 
- [`v7.0/modes/03x-worker/039-cross-functional/security-specialist/039-work-xf-security-specialist.mode.md` (created)]