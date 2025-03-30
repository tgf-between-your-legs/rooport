<script setup>
import { ref, onMounted, computed } from 'vue';

// Reactive state
const allModes = ref([]); // Holds the data for all fetched modes
const selectedModeSlugs = ref([]); // Holds the slugs of selected modes
const isLoading = ref(true);
const error = ref(null);
const copyButtonText = ref('Copy to Clipboard');

// --- Data Fetching ---
async function fetchModes() {
  isLoading.value = true;
  error.value = null;
  try {
    // Fetch manifest from the public directory (served at root)
    const manifestResponse = await fetch('/roo-commander/mode_templates/manifest.json'); // Path relative to server root
    if (!manifestResponse.ok) {
      throw new Error(`HTTP error fetching manifest! status: ${manifestResponse.status}`);
    }
    const modeFiles = await manifestResponse.json();

    // Fetch individual mode files from the public directory
    const modePromises = modeFiles.map(async (filename) => {
      try {
        const modeResponse = await fetch(`/roo-commander/mode_templates/${filename}`); // Path relative to server root
        if (!modeResponse.ok) {
          console.error(`Failed to fetch ${filename}: ${modeResponse.status}`);
          return null; // Skip this mode
        }
        return await modeResponse.json();
      } catch (fetchError) {
        console.error(`Error fetching or parsing ${filename}:`, fetchError);
        return null; // Skip on error
      }
    });

    // Wait for all fetches and filter out any nulls (failed fetches)
    const modesData = (await Promise.all(modePromises)).filter(mode => mode !== null);

    // Sort modes alphabetically by name for consistent display
    modesData.sort((a, b) => a.name.localeCompare(b.name));

    allModes.value = modesData;

  } catch (err) {
    console.error('Error loading modes:', err);
    error.value = 'Failed to load mode data. Please check the console and ensure manifest.json and mode files are accessible in the public/mode_templates directory.';
  } finally {
    isLoading.value = false;
  }
}

// Fetch modes when the component is mounted
onMounted(fetchModes);

// --- Computed Properties ---

// Group modes for display
const groupedModes = computed(() => {
  const categories = {
    management: [],
    specialist: [],
    other: []
  };
  allModes.value.forEach(mode => {
    // Basic categorization logic (can be refined)
    if (mode.slug?.includes('manager') || mode.slug?.includes('architect') || mode.slug?.includes('executive')) {
        categories.management.push(mode);
    } else if (mode.slug?.includes('specialist') || mode.slug?.includes('developer') || mode.slug?.includes('tester') || mode.slug?.includes('reviewer') || mode.slug?.includes('fixer') || mode.slug?.includes('writer') || mode.slug?.includes('designer') || mode.slug?.includes('creator') || mode.slug?.includes('installer')) {
         categories.specialist.push(mode);
    } else {
        categories.other.push(mode);
    }
  });
   // Ensure categories are sorted internally by name
   for (const category in categories) {
       categories[category].sort((a, b) => a.name.localeCompare(b.name));
   }
  return categories;
});

// Generate JSON output based on selected slugs
const outputJson = computed(() => {
  const selectedModesData = allModes.value.filter(mode => selectedModeSlugs.value.includes(mode.slug));
  // Sort final output array by slug for consistency
  selectedModesData.sort((a, b) => a.slug.localeCompare(b.slug));
  return JSON.stringify(selectedModesData, null, 2); // Pretty print
});

// --- Methods ---

function selectAll() {
  selectedModeSlugs.value = allModes.value.map(mode => mode.slug);
}

function deselectAll() {
  selectedModeSlugs.value = [];
}

async function copyToClipboard() {
  try {
    await navigator.clipboard.writeText(outputJson.value);
    copyButtonText.value = 'Copied!';
    setTimeout(() => {
      copyButtonText.value = 'Copy to Clipboard';
    }, 1500);
  } catch (err) {
    console.error('Failed to copy text: ', err);
    alert('Failed to copy JSON. Please copy manually.');
  }
}

</script>

<template>
  <div class="container">
    <h1>Roo Commander Mode Configurator</h1>
    <p>
      Welcome to the Roo Commander Mode Configurator! This tool allows you to select which predefined 'modes' (specialised AI roles) you want to include in your Roo Commander setup.
      Choose the modes relevant to your workflow, and the tool will generate the necessary JSON configuration array below. You can then copy this JSON and use it to customise your Roo Commander experience.
    </p>

    <div class="controls">
      <button @click="selectAll">Select All</button>
      <button @click="deselectAll">Deselect All</button>
    </div>

    <div id="mode-selection-area">
      <div v-if="isLoading">Loading modes...</div>
      <div v-if="error" class="error-message">{{ error }}</div>
      <div v-if="!isLoading && !error">
        <div v-for="(modesInCategory, categoryName) in groupedModes" :key="categoryName" class="category">
          <h2 v-if="modesInCategory.length > 0">{{ categoryName.charAt(0).toUpperCase() + categoryName.slice(1) }}</h2>
          <label v-for="mode in modesInCategory" :key="mode.slug">
            <input type="checkbox" :value="mode.slug" v-model="selectedModeSlugs">
            {{ mode.name }} ({{ mode.slug }})
          </label>
        </div>
      </div>
    </div>

    <h2>Generated JSON Output:</h2>
    <textarea id="output-json" readonly :value="outputJson" placeholder="JSON output will appear here..."></textarea>
    <div class="output-controls">
      <button id="copy-button" @click="copyToClipboard">{{ copyButtonText }}</button>
    </div>

    <footer>
      <p>
        Part of the <a href="https://github.com/jezweb/roo-commander" target="_blank" rel="noopener noreferrer">Roo Commander</a> project.
      </p>
    </footer>
  </div>
</template>

<style scoped>
/* General Styles */
body { /* Apply to body if this style isn't overridden by Vite's base styles */
  background-color: #f8f9fa; /* Light grey background */
  margin: 0; /* Remove default body margin */
}

.container {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  padding: 30px;
  max-width: 960px; /* Slightly wider */
  margin: 20px auto; /* Add top/bottom margin */
  background-color: #ffffff; /* White background for the container */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 10px rgba(0,0,0,0.1); /* Subtle shadow */
}

h1 {
  color: #343a40; /* Darker heading */
  text-align: center; /* Center heading */
  margin-bottom: 10px;
}
h2 {
    color: #495057; /* Slightly lighter heading */
    margin-top: 25px; /* More space above h2 */
    margin-bottom: 10px;
    border-bottom: 1px solid #dee2e6; /* Separator line */
    padding-bottom: 5px;
}
p {
  margin-bottom: 20px;
  line-height: 1.6;
  color: #6c757d; /* Grey text */
  text-align: center; /* Center paragraph */
}

/* Controls */
.controls {
  margin-bottom: 20px;
  text-align: center; /* Center buttons */
}

button {
  margin: 0 5px; /* Adjust margin */
  padding: 10px 18px; /* Slightly larger buttons */
  cursor: pointer;
  border: 1px solid #ced4da;
  background-color: #e9ecef; /* Lighter button background */
  color: #495057;
  border-radius: 4px;
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}
button:hover {
    background-color: #dee2e6; /* Darker hover */
    border-color: #adb5bd;
}
button:active {
    background-color: #ced4da;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
}

/* Mode Selection Area */
#mode-selection-area {
  border: 1px solid #dee2e6; /* Lighter border */
  padding: 20px;
  margin-bottom: 25px;
  min-height: 150px; /* Increased min-height */
  max-height: 500px; /* Increased max-height */
  overflow-y: auto;
  background-color: #fff; /* Ensure white background */
  border-radius: 4px; /* Match button radius */
}

.category {
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #e9ecef; /* Lighter separator */
  text-align: left; /* Explicitly left-align content within category */
}
.category:last-child {
    border-bottom: none;
}

.category h2 {
  font-size: 1.2em; /* Slightly larger category titles */
  margin-bottom: 12px;
  font-weight: 600; /* Semi-bold */
  color: #007bff; /* Use a primary color */
  border-bottom: none; /* Remove border from h2 */
  margin-top: 0; /* Remove extra top margin */
  padding-left: 5px; /* Align heading with labels */
}

label {
  display: block; /* Ensures labels are on new lines */
  margin-bottom: 8px; /* More space between labels */
  cursor: pointer;
  padding-left: 5px; /* Indent labels slightly */
  color: #495057;
}
label:hover {
    background-color: #f8f9fa; /* Subtle hover for labels */
}
label input {
    margin-right: 10px; /* More space after checkbox */
    vertical-align: middle; /* Align checkbox nicely */
}

/* Output Area */
textarea {
  width: 100%;
  min-height: 300px; /* Taller textarea */
  margin-bottom: 15px;
  box-sizing: border-box;
  font-family: 'Courier New', Courier, monospace; /* Monospace font */
  font-size: 0.9em;
  border: 1px solid #ced4da;
  padding: 15px;
  border-radius: 4px;
  background-color: #e9ecef; /* Light background for contrast */
  color: #343a40;
}

.output-controls {
  margin-bottom: 15px;
  text-align: right; /* Align copy button to the right */
}

.error-message {
    color: #dc3545; /* Bootstrap danger color */
    font-weight: bold;
    background-color: #f8d7da; /* Light red background */
    border: 1px solid #f5c6cb; /* Red border */
    padding: 10px 15px;
    border-radius: 4px;
    margin-bottom: 15px;
}

/* Footer */
footer {
    margin-top: 30px;
    padding-top: 15px;
    border-top: 1px solid #dee2e6;
    text-align: center;
    font-size: 0.9em;
    color: #6c757d;
}
footer a {
    color: #007bff;
    text-decoration: none;
}
footer a:hover {
    text-decoration: underline;
}
</style>
