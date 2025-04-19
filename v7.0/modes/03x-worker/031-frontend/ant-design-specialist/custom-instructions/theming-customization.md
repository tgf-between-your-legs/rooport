# Ant Design Theming & Customization

Methods for customizing the look and feel of Ant Design components.

## 1. `ConfigProvider` (Recommended for Runtime Customization)

*   **Concept:** A React component provided by `antd` that allows you to apply theme configurations to its children. Useful for changing primary colors, component sizes, border radius, etc., dynamically or for specific sections of your app.
*   **Usage:** Wrap your application or specific sections with `<ConfigProvider>`.
    ```jsx
    import { ConfigProvider, Button, Space } from 'antd';
    import { theme } from 'antd'; // Import theme object for algorithms

    const App = () => (
      <ConfigProvider
        theme={{
          // Algorithm for dark/compact mode (optional)
          // algorithm: theme.darkAlgorithm,
          // algorithm: theme.compactAlgorithm,

          token: {
            // Seed Token (influences many components)
            colorPrimary: '#00b96b',
            borderRadius: 2,

            // Alias Tokens (more specific overrides)
            colorBgContainer: '#f6ffed',
            // ... other tokens
          },
          components: {
            // Component-specific overrides
            Button: {
              colorPrimary: '#00b96b',
              algorithm: true, // Enable algorithm for component tokens
            },
            Input: {
              colorPrimary: '#eb2f96',
            },
          },
        }}
      >
        {/* Your application components */}
        <Space>
          <Button type="primary">Primary Button</Button>
          <Input placeholder="Custom Input" />
        </Space>
      </ConfigProvider>
    );
    ```
*   **Tokens:** Refer to the Ant Design documentation for the full list of available design tokens (`token`) and component-specific tokens (`components`).
    *   **Seed Tokens:** Base values like `colorPrimary`, `fontFamily`, `borderRadius`.
    *   **Map Tokens:** Derived values based on seed tokens (e.g., `colorBgLayout`).
    *   **Alias Tokens:** Contextual semantic tokens (e.g., `colorBgContainer`, `colorText`).
*   **Algorithms:** Apply global theme adjustments like `theme.darkAlgorithm` or `theme.compactAlgorithm`. Can be combined in an array.

## 2. Less Variables (Build-time Customization)

*   **Concept:** Ant Design is built with Less. You can override its Less variables during the build process to customize the theme globally. This requires setting up Less compilation in your project build (e.g., via Webpack, Vite with Less plugin, CRACO).
*   **Usage:** Create a Less file (e.g., `src/theme.less`) and override variables *before* importing the main Ant Design Less file.
    ```less
    // src/theme.less
    @import "~antd/lib/style/themes/default.less"; // Import default variables

    // Override variables
    @primary-color: #52c41a; // Green
    @border-radius-base: 4px;
    @link-color: @primary-color;

    // Import Ant Design styles AFTER overriding variables
    @import "~antd/dist/antd.less"; // Or antd.dark.less etc.

    // Your custom application styles...
    ```
*   **Configuration:** Configure your build tool to process this Less file.
*   **Benefit:** Global theme applied at build time.
*   **Drawback:** Requires Less setup, less dynamic than `ConfigProvider`.

## Choosing a Method

*   **`ConfigProvider`:** Best for dynamic theme changes, applying different themes to parts of the app, and easier setup in modern React projects (no Less build config needed). Preferred method generally.
*   **Less Variables:** Suitable for applying a single, static theme globally across the entire application at build time.

*(Refer to the official Ant Design "Customize Theme" documentation for detailed guides: https://ant.design/docs/react/customize-theme)*