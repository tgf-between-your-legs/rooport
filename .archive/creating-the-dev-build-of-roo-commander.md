lets discuss and decide how we do a 'dev' and a 'build' using a assume some kind of js files for each task
im trying to think about how i go between my local usage of roo commander in the root of the workspace and the source material for each new version of roo commander

lets think about the 'dev' process

we would already have need all the default project folders in the workspace which i will already be using, which we explain here
/home/jeremy/vscode/roo-commander/.docs/standards/project_structure_inventory.md


custom mode folders
the custom modes have a preferred method to follow as sub folders of .roo/

explained in this copy of the documentation
/home/jeremy/vscode/roo-commander/v7.0/context/custom-modes.md

so the script would need me the user to define the source directory where all the modes are in their various sub folder structure
eg if we are making the custom modes for v7.1
then all the modes can be found in various depths of folders in 
/home/jeremy/vscode/roo-commander/v7.1/modes
and a specific mode would be like
/home/jeremy/vscode/roo-commander/v7.1/modes/worker/database/database-specialist
so then we would make a folder (if it doesnt exist) called
.roo/rules-database-specialist/
and then delete the contents of that folder if it has any
and then we would copy the folders 
context
custom-instructions
examples
without the README.md files
(i dont think they are needed because the modes dont have to read the files as i understand it, the contents are just placed into their context as part of their prompt)
into
.roo/rules-database-specialist/
(note: ive been advised that sub folders in there should get read into the context window for the mode when it is active, we dont need to merge the files into the /rules- folder, we will test this shortly and find out)

.roomodes json file
we also have to make (or more likely replace the contents of) the file /home/jeremy/vscode/roo-commander/.roomodes
you can see the format
/home/jeremy/vscode/roo-commander/v7.0/context/custom-modes.md
## Custom Mode Configuration (JSON Format)
and we are going to give all our modes all the groups and no file restrictions, eg
"groups": [
        "read",
        "edit",
        "browser",
        "command",
        "mcp"
      ]

the roleDefinition seems like that is what we have in our mode md files as
# --- Base Prompting (Required) ---

the customInstructions in the roomodes seems like it would be what we have for
# --- Description (Required) ---



what am i missing, what havent i thought of?
