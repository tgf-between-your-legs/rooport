import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  // Define the base path for deployment (e.g., GitHub Pages)
  // Assumes the repo name is 'roo-commander' and this tool is in 'tools/mode_configurator/'
  base: '/roo-commander/tools/mode_configurator/',
})
