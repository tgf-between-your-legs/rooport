const fs = require('fs');
const path = require('path');

// Define the standard order of properties
const standardOrder = [
  'slug',
  'name',
  'roleDefinition',
  'customInstructions',
  'groups',
  'tags',
  // Include other possible properties to ensure they're not lost
  'description',
  'icon',
  'version',
  'author',
  'website',
  'license',
  // Add any other properties that might exist in the mode files
];

// Directory containing the mode files
const modesDir = path.join(__dirname, '..', 'v6.3', 'modes');

// Function to reorder properties in an object according to standardOrder
function reorderProperties(obj) {
  const reordered = {};
  
  // First add properties in the standard order
  standardOrder.forEach(prop => {
    if (obj.hasOwnProperty(prop)) {
      reordered[prop] = obj[prop];
    }
  });
  
  // Then add any remaining properties not in the standard order
  Object.keys(obj).forEach(prop => {
    if (!standardOrder.includes(prop)) {
      reordered[prop] = obj[prop];
    }
  });
  
  return reordered;
}

// Process all JSON files in the modes directory
fs.readdir(modesDir, (err, files) => {
  if (err) {
    console.error('Error reading directory:', err);
    return;
  }
  
  // Filter for JSON files
  const jsonFiles = files.filter(file => file.endsWith('.json'));
  console.log(`Found ${jsonFiles.length} JSON files in ${modesDir}`);
  
  // Process each JSON file
  jsonFiles.forEach(file => {
    const filePath = path.join(modesDir, file);
    
    try {
      // Read the file
      const content = fs.readFileSync(filePath, 'utf8');
      const modeObj = JSON.parse(content);
      
      // Reorder properties
      const reorderedObj = reorderProperties(modeObj);
      
      // Write back to file with pretty formatting
      fs.writeFileSync(filePath, JSON.stringify(reorderedObj, null, 2), 'utf8');
      console.log(`Standardized properties in ${file}`);
    } catch (fileErr) {
      console.error(`Error processing ${file}:`, fileErr);
    }
  });
  
  console.log('Finished standardizing mode properties');
});