const fs = require('fs');
const path = require('path');

// Directory containing the mode collections
const collectionsDir = path.join(__dirname, '..', 'v6.4', 'modes');

// Function to fix the groups structure in a mode
function fixGroupsStructure(mode) {
  if (!mode.groups) return mode;
  
  // Check if any group is an object (complex structure)
  const hasComplexGroups = mode.groups.some(group => typeof group === 'object');
  
  if (hasComplexGroups) {
    console.log(`Fixing complex groups structure in mode: ${mode.slug}`);
    
    // Convert complex groups to simple strings
    // For any object with a "group" property, just use that value
    const simplifiedGroups = mode.groups.map(group => {
      if (typeof group === 'object' && group.group) {
        return group.group;
      }
      return group;
    });
    
    mode.groups = simplifiedGroups;
  }
  
  return mode;
}

// Process all collection directories
fs.readdir(collectionsDir, (err, collections) => {
  if (err) {
    console.error('Error reading collections directory:', err);
    return;
  }
  
  // Filter for directories
  collections.forEach(collection => {
    const collectionPath = path.join(collectionsDir, collection);
    
    // Check if it's a directory
    if (fs.statSync(collectionPath).isDirectory()) {
      // Find the modes JSON file in this collection
      const modesFiles = fs.readdirSync(collectionPath).filter(file => file.endsWith('_modes.json'));
      
      modesFiles.forEach(modesFile => {
        const modesFilePath = path.join(collectionPath, modesFile);
        
        try {
          // Read the file
          const content = fs.readFileSync(modesFilePath, 'utf8');
          const modesObj = JSON.parse(content);
          
          if (modesObj.customModes && Array.isArray(modesObj.customModes)) {
            // Fix groups structure for each mode
            let modified = false;
            modesObj.customModes = modesObj.customModes.map(mode => {
              const originalMode = JSON.stringify(mode);
              const fixedMode = fixGroupsStructure(mode);
              if (JSON.stringify(fixedMode) !== originalMode) {
                modified = true;
              }
              return fixedMode;
            });
            
            if (modified) {
              // Write back to file with pretty formatting
              fs.writeFileSync(modesFilePath, JSON.stringify(modesObj, null, 2), 'utf8');
              console.log(`Updated groups structure in ${modesFilePath}`);
            }
          }
        } catch (fileErr) {
          console.error(`Error processing ${modesFilePath}:`, fileErr);
        }
      });
    }
  });
  
  console.log('Finished fixing groups structure in all collections');
});