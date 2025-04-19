# Task Log: database-specialist-conversion - Technical Writing: Mode File Migration

**Goal:** Process and migrate the database-specialist mode file to the new convention format
**Subject:** Database Specialist mode file migration
**Audience:** Mode system maintainers and developers
**Purpose:** Document the migration process and ensure proper conversion to the new format
**References:** 
- `v7.0/modes/md/database-specialist.md` (source file - now deleted)
- `v7.0/templates/mode_template.md` (template)
- `v7.0/templates/mode_hierarchy.md` (hierarchy guide)
- `v7.0/templates/mode_folder_structure.md` (folder structure guide)
- `v7.0/templates/mode_classification_guide.md` (classification guide)
- `project_journal/decisions/20251104-mode_convention_final_refinement.md` (convention ADR)

## Process Steps

1. ✅ Review the source mode file
2. ✅ Determine the correct target folder and filename
   - Based on the classification guide, database-specialist is a worker-level mode (03x-worker) in the database department (033-worker-database)
   - Target folder: `v7.0/modes/03x-worker/033-database/database-specialist/`
   - Target filename: `033-work-db-database-specialist.mode.md` (based on the ADR refinement)
3. ✅ Create the target folder if needed
   - Created `v7.0/modes/03x-worker/033-database/database-specialist/` directory
4. ✅ Copy and rename the mode file to the target location
   - Created `v7.0/modes/03x-worker/033-database/database-specialist/033-work-db-database-specialist.mode.md`
5. ✅ Update the new file's metadata according to the template and final conventions
   - Added Level: 033-worker-database
   - Updated Tool Groups to use standard YAML list format
   - Updated Tags to use standard YAML list format
   - Added Categories: Database
   - Added Stack: SQL, NoSQL, ORM, Database Migration Tools
   - Added Reports To: technical-architect, commander
   - Updated API Configuration to use standard YAML format
6. ✅ Flag any ambiguous or missing critical information
   - No ambiguous or missing critical information found
7. ✅ Update this task log with the process and outcome
8. ✅ (Optional) Delete the source file
   - Deleted `v7.0/modes/md/database-specialist.md`

## Summary

The database-specialist mode file has been successfully migrated to the new convention format. The mode is now properly classified as a worker-level mode in the database department (033-worker-database) and follows the updated file naming and metadata conventions.

Key changes made:
- Created proper directory structure following the hierarchy guide
- Renamed file using the convention `033-work-db-database-specialist.mode.md`
- Updated metadata section with proper Level, Categories, Stack, and Reports To fields
- Reformatted YAML lists according to the convention refinement ADR
- Deleted the original source file after successful migration

The new file is located at: `v7.0/modes/03x-worker/033-database/database-specialist/033-work-db-database-specialist.mode.md`

---
**Status:** ✅ Complete
**Outcome:** Success
**Summary:** Successfully migrated the database-specialist mode file to the new convention format, creating the proper directory structure and updating the metadata according to the final conventions. The filename has been corrected to use the department shortcode "work-db" and follow the fully hyphenated format.
**References:** [`v7.0/modes/03x-worker/033-database/database-specialist/033-work-db-database-specialist.mode.md` (created)]