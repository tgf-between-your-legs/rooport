# Requirements Document Templates

Use these templates as a starting point for structuring the requirements section of the Discovery Report. Adapt based on project type and complexity.

## Template 1: General Web Application

```markdown
## Project Requirements

### 1. Overview & Goals
*   **Problem:** [Briefly describe the problem this project solves]
*   **Goal(s):** [List the primary objectives, e.g., Increase user engagement, Streamline process X]
*   **Target Users:** [Describe the primary user personas]
*   **Success Criteria:** [How will success be measured? e.g., Achieve Y signups, Reduce process time by Z%]

### 2. Core Functionality
*   **Feature 1: [Name, e.g., User Authentication]**
    *   User Story/Description: As a user, I want to register and log in, so that I can access my account.
    *   Acceptance Criteria:
        *   [ ] Users can register with email/password.
        *   [ ] Users receive a confirmation email.
        *   [ ] Users can log in with registered credentials.
        *   [ ] Users can log out.
        *   [ ] Password reset functionality exists.
    *   Priority: Must-have
*   **Feature 2: [Name, e.g., Dashboard Display]**
    *   User Story/Description: As a logged-in user, I want to see a dashboard summarizing my key data.
    *   Acceptance Criteria:
        *   [ ] Dashboard displays widget A.
        *   [ ] Widget B shows data from the last 7 days.
        *   [ ] Users can customize widget layout (Optional).
    *   Priority: Must-have (core widgets), Could-have (customization)
*   ... *(Add more features)*

### 3. Design & Aesthetics
*   **Look & Feel:** [Describe desired style, e.g., Modern, clean, professional, playful]
*   **Branding:** [Reference brand guidelines, logos, color palettes if available]
*   **Inspiration:** [Links to inspirational websites or apps]
*   **Existing Assets:** [Links to Figma designs, wireframes, mockups]
*   **UI Framework Preference:** [e.g., Tailwind CSS preferred, Use existing Material UI components]

### 4. Technical Aspects
*   **Non-Functional Requirements (NFRs):**
    *   Performance: [e.g., Page loads under 2 seconds]
    *   Security: [e.g., Standard web security practices (OWASP Top 10), HTTPS required]
    *   Scalability: [e.g., Expected initial load: 100 concurrent users]
    *   ... *(Add others as needed)*
*   **Constraints:** [e.g., Must integrate with existing API X, Must run on AWS, Budget limit]
*   **Data:** [Describe key data entities and relationships, data sources]

```

## Template 2: API Development

```markdown
## Project Requirements

### 1. Overview & Goals
*   **Problem:** [e.g., Need a programmatic way to access user profile data]
*   **Goal(s):** [e.g., Provide RESTful API for CRUD operations on user profiles]
*   **Target Consumers:** [e.g., Internal web frontend, Mobile application]

### 2. Core Functionality / Endpoints
*   **Resource: User Profile**
    *   `GET /users/{userId}/profile`: Retrieve user profile.
        *   Auth: Required (User scope)
        *   Response: User profile object (fields: name, email, bio, avatarUrl)
    *   `PUT /users/{userId}/profile`: Update user profile.
        *   Auth: Required (User scope, self only)
        *   Request Body: Fields to update (name, bio, avatarUrl)
        *   Response: Updated user profile object
*   **Resource: Authentication**
    *   `POST /auth/login`: User login.
        *   Request Body: email, password
        *   Response: Access token, Refresh token
*   ... *(Add more resources and endpoints)*

### 3. Technical Aspects
*   **API Style:** RESTful
*   **Data Format:** JSON
*   **Authentication:** JWT Bearer Tokens
*   **NFRs:**
    *   Performance: Average response time < 150ms
    *   Security: Input validation, rate limiting, HTTPS
    *   Scalability: Handle 500 requests per second
*   **Constraints:** Must use existing PostgreSQL database.

```

*(Adapt and combine elements from these templates as needed for the specific project.)*