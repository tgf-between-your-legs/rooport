# 4. Key Considerations / Safety Protocols

*   **Component API:** Use the documented API for Ant Design components. Avoid accessing internal DOM structures directly, as these can change between versions.
*   **Form Validation:** Implement thorough validation using Ant Design's `rules` prop on `Form.Item`. Handle both client-side and server-side validation feedback if applicable.
*   **Responsiveness:** Utilize Ant Design's Grid system (`Row`, `Col`) and responsive props (like `xs`, `sm`, `md`, `lg`, `xl`, `xxl` on `Col`) on components where available. Test layouts on different screen sizes.
*   **Accessibility:** Use semantic HTML where possible. Ensure Ant Design components are used accessibly (e.g., associating labels with form inputs via `Form.Item`, providing `alt` text for images in `Card` or `Avatar`). Request review from `accessibility-specialist` for critical components or complex interactions.
*   **Bundle Size:** Be mindful that Ant Design can increase bundle size. Ensure tree-shaking is configured correctly in the build process (usually handled by `frontend-lead` or `devops-lead`). Import only the necessary components.