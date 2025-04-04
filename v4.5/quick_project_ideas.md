# Quick Project Ideas for Roo Commander v4.5

This file provides ideas for simple web projects that you can try building with Roo Commander. These projects focus on core web technologies (HTML, CSS, JavaScript) and optionally use popular CSS frameworks via CDN links, meaning they require **no complex build setup** and can be run by simply opening the `index.html` file in your browser.

These are great for getting familiar with the Roo Commander workflow and building confidence! For each idea, a suggested starting prompt for the `👑 Roo Commander` is provided.

---

## 1. Vanilla JavaScript Projects (No Frameworks)

These rely purely on HTML for structure, CSS for styling, and JavaScript for interactivity.

*   **🎯 Simple To-Do List:**
    *   **Goal:** Create a list where users can add tasks, mark them as complete (e.g., strikethrough), and optionally remove them. Persist tasks using local storage.
    *   **Core Tech:** HTML, CSS, JS (DOM manipulation, event listeners, local storage).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'simple-todo'. Create a web-based to-do list application using HTML, CSS, and vanilla JavaScript. Users should be able to add tasks, mark tasks as complete (visually indicating completion), remove tasks, and have their tasks persist between browser sessions using local storage."`

*   **🎯 Basic Calculator:**
    *   **Goal:** Implement a calculator that can perform addition, subtraction, multiplication, and division.
    *   **Core Tech:** HTML, CSS (grid layout), JS (event listeners, calculation logic, display update).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'basic-calculator'. Create a web-based calculator using HTML, CSS, and vanilla JavaScript. It should have buttons for digits 0-9, operators +, -, *, /, an equals sign, and a clear button. It needs a display area to show input and results."`

*   **🎯 Pomodoro Timer:**
    *   **Goal:** Create a timer that cycles through work sessions (e.g., 25 minutes) and short breaks (e.g., 5 minutes). Include start, pause, and reset buttons. Optionally add an audible alert.
    *   **Core Tech:** HTML, CSS, JS (`setInterval`/`setTimeout`, state management, DOM update, optional Audio API).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'pomodoro-timer'. Create a web-based Pomodoro timer using HTML, CSS, and vanilla JavaScript. It should display the time remaining, have start, pause, and reset buttons, and cycle between a 25-minute work session and a 5-minute break session. Add a simple sound alert when a session ends."`

*   **🎯 Random Quote Generator:**
    *   **Goal:** Display a random quote from a predefined list when a button is clicked.
    *   **Core Tech:** HTML, CSS, JS (array of quotes, event listener, random selection, DOM update).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'quote-generator'. Create a simple web page using HTML, CSS, and vanilla JavaScript that displays a random quote from a predefined list when the user clicks a 'New Quote' button. Include at least 10 quotes in the list."`

*   **🎯 Simple Image Carousel:**
    *   **Goal:** Create a basic image carousel/slider with "Previous" and "Next" buttons to cycle through a small set of images.
    *   **Core Tech:** HTML (image tag, buttons), CSS (styling, potentially transitions/hiding inactive images), JS (array of image URLs, event listeners, logic to change the displayed image `src`).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'image-carousel'. Create a simple image carousel using HTML, CSS, and vanilla JavaScript. It should display one image at a time from a list of 3-5 images (use placeholder image URLs if needed). Include 'Previous' and 'Next' buttons to cycle through the images."`

*   **🎯 Basic Quiz App:**
    *   **Goal:** Create a simple multiple-choice quiz. Display one question at a time, track the score, and show the final score at the end.
    *   **Core Tech:** HTML (display question/options, score), CSS (styling), JS (array of question objects, logic for displaying questions/options, checking answers, tracking score, moving to next question).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'simple-quiz'. Create a basic multiple-choice quiz web application using HTML, CSS, and vanilla JavaScript. Define 3-5 questions with 3-4 answer options each (only one correct). Display one question at a time, allow the user to select an answer, show if it was correct, track the score, and display the final score after the last question."`

---

## 2. Bootstrap Project (via CDN)

Leverage Bootstrap's pre-built components and grid system for faster layout and styling. Link Bootstrap via CDN in your HTML.

*   **🎯 Simple Landing Page:**
    *   **Goal:** Create a single-page landing page for a fictional product or service with a responsive navigation bar, hero section, features section (using grid/cards), and footer.
    *   **Core Tech:** HTML, Bootstrap CSS/JS (via CDN), Custom CSS (for minor tweaks).
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'bootstrap-landing'. Create a single-page landing page using HTML and Bootstrap 5 (via CDN). Include a responsive navbar, a hero section with a call-to-action button, a section listing 3 key features using Bootstrap cards within a grid layout, and a simple footer."`

---

## 3. Material Web Components Project (via CDN)

Use Google's Material Web Components (MWC) for Material Design elements without needing a full framework like React/Vue/Angular. Link MWC via CDN/module script tags.

*   **🎯 Basic Contact Form:**
    *   **Goal:** Create a simple contact form with Material Design text fields (Name, Email, Message) and a button. (Focus on layout and component usage, not backend submission).
    *   **Core Tech:** HTML, MWC components (via module script tags), CSS.
    *   **Roo Modes:** `👑 Roo Commander`, `🚦 Project Onboarding`, `🔍 Discovery Agent`, `✨ Project Initializer`, `🖥️ Frontend Developer`.
    *   **Suggested Prompt:** `"Start a new project called 'mwc-contact-form'. Create a simple contact form page using HTML and Material Web Components (via module script imports from a CDN like unpkg). Include MWC text fields for Name and Email, an MWC text area for Message, and an MWC button for Submit. Use basic CSS for layout."`

---

**Tips for Success:**

*   **Start Small:** Choose one simple feature first.
*   **Be Specific:** Clearly define the goal for the `👑 Roo Commander`.
*   **Review Requirements:** Ensure the `🔍 Discovery Agent` captures what you want before implementation starts.
*   **Check the Task Logs:** Follow progress in `project_journal/tasks/`.
*   **Iterate:** Don't expect perfection on the first try. Provide feedback to the Commander to refine the results.