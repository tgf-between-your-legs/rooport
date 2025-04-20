# Discovery Agent Question Bank

A collection of questions to guide requirements elicitation. Use these to formulate `ask_followup_question` prompts during the discovery phase.

## I. Project Goals & Overview

*   What is the primary problem this project aims to solve?
*   What are the main goals or objectives? How will success be measured?
*   Who are the target users or user personas?
*   What is the overall scope? What is explicitly *out* of scope?
*   Are there any existing systems or processes this project replaces or integrates with?
*   What is the desired timeline or key milestones?

## II. Core Functionality

*(Ask for each major feature identified)*
*   Can you describe the desired functionality for [Feature X]?
*   What are the key steps a user would take to use [Feature X]? (User Flow)
*   What specific data needs to be displayed or managed for [Feature X]?
*   Are there different user roles with different permissions related to [Feature X]?
*   What are the essential acceptance criteria for [Feature X] to be considered complete?
*   How would you prioritize this feature (Must-have, Should-have, Could-have)?

## III. Design & Aesthetics

*   What is the desired look and feel for the application (e.g., modern, corporate, playful)?
*   Are there any existing brand guidelines, logos, or color palettes to follow?
*   Can you provide links to any inspirational websites, apps, or designs?
*   Are there existing wireframes, mockups, or Figma designs available? If so, where?
*   Based on the detected stack ([mention detected UI tech]), do you have preferences for specific UI component libraries (e.g., Material UI, Ant Design, Bootstrap, Shadcn UI)?
*   Is responsiveness (working on different screen sizes like mobile, tablet, desktop) a requirement?

## IV. Technical Aspects

*   **Non-Functional Requirements (NFRs):**
    *   Are there specific performance requirements (e.g., page load times, transaction speed)?
    *   What are the security expectations (e.g., user authentication method, data encryption, compliance needs)?
    *   What is the expected user load (average, peak)? Are there scalability requirements?
    *   Are there specific reliability or uptime requirements?
*   **Constraints:**
    *   Are there any budget limitations?
    *   Are there technology constraints (e.g., must use specific cloud provider, database, programming language)? (Cross-reference with detected stack: "I see X, is that a hard constraint?")
    *   Are there integration requirements with other specific systems or APIs?
*   **Data:**
    *   Where will the data come from? Is there an existing database or API?
    *   What are the key data entities and their relationships?
    *   Are there any data privacy or compliance considerations (e.g., GDPR)?

## V. Stack Confirmation

*(Use after automated analysis)*
*   Our analysis suggests the project uses [Language/Framework X, Library Y]. Is this correct?
*   Are there any other key technologies or dependencies we should be aware of?
*   Is there a preferred build tool or CI/CD process?

*(Tailor questions based on the project type and initial context. Start broad, then get specific.)*