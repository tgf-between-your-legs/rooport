# Ant Design: Common Components Reference

Examples of using basic and frequently used Ant Design components in React.

## Core Concept

Ant Design (`antd`) provides a rich set of pre-built React components following the Ant Design specification. Import components directly from the `antd` package.

```jsx
import React from 'react';
import { Button, Typography, Space, Divider, Rate, Tag, Spin } from 'antd'; // Import needed components
import { DownloadOutlined, StarFilled } from '@ant-design/icons'; // Import icons

const { Title, Paragraph, Text, Link } = Typography;

function CommonComponentsDemo() {
  return (
    <Space direction="vertical" size="large" style={{ width: '100%' }}>
      {/* Typography */}
      <Divider orientation="left">Typography</Divider>
      <Title level={2}>h2. Ant Design Title</Title>
      <Paragraph>
        Ant Design, a design language for background applications, is refined by Ant UED Team.
        <Text strong> This part is strong.</Text> <Text code>This is code.</Text>
      </Paragraph>
      <Link href="https://ant.design" target="_blank">
        Ant Design (Link)
      </Link>

      {/* Buttons */}
      <Divider orientation="left">Buttons</Divider>
      <Space wrap> {/* Wrap buttons if they overflow */}
        <Button type="primary">Primary Button</Button>
        <Button>Default Button</Button>
        <Button type="dashed">Dashed Button</Button>
        <Button type="text">Text Button</Button>
        <Button type="link">Link Button</Button>
        <Button type="primary" icon={<DownloadOutlined />} shape="circle" />
        <Button type="primary" loading>Loading</Button>
        <Button danger>Danger Default</Button>
      </Space>

      {/* Icons (using @ant-design/icons) */}
      <Divider orientation="left">Icons</Divider>
      <Space>
        <StarFilled style={{ color: 'gold', fontSize: '24px' }} />
        <DownloadOutlined style={{ fontSize: '24px', color: '#1890ff' }} />
      </Space>

      {/* Divider */}
      <Divider>Horizontal Divider</Divider>

      {/* Space */}
      <Divider orientation="left">Space</Divider>
      <Space> {/* Default horizontal */}
        Space Item 1
        <Button type="primary">Button</Button>
        <Text>Space Item 3</Text>
      </Space>

      {/* Rate */}
      <Divider orientation="left">Rate</Divider>
      <Rate allowHalf defaultValue={2.5} />

      {/* Tag */}
      <Divider orientation="left">Tag</Divider>
      <Space>
        <Tag color="magenta">magenta</Tag>
        <Tag color="blue">blue</Tag>
        <Tag color="success">success</Tag>
        <Tag color="warning">warning</Tag>
        <Tag color="error">error</Tag>
        <Tag closable onClose={() => console.log('Tag closed!')}>Closable Tag</Tag>
      </Space>

       {/* Spin */}
       <Divider orientation="left">Spin</Divider>
       <Spin size="large" />
       <Spin tip="Loading...">
         <div style={{ padding: 50, background: 'rgba(0, 0, 0, 0.05)', marginTop: 16 }}>
           Alert message content
         </div>
       </Spin>

    </Space>
  );
}

export default CommonComponentsDemo;
```

## Key Components & Usage

*   **`Typography`**: Includes `Title`, `Text`, `Paragraph`, `Link`. Use `level` prop for `Title` (1-5). Use boolean props like `strong`, `code`, `mark`, `disabled`, `italic` on `Text` and `Paragraph`.
*   **`Button`**:
    *   `type`: `primary`, `default`, `dashed`, `text`, `link`.
    *   `danger`: Boolean for dangerous action styling.
    *   `loading`: Boolean to show loading indicator.
    *   `shape`: `circle`, `round`.
    *   `icon`: React node (often an icon component) to display inside.
    *   Standard HTML button props like `onClick`, `disabled`.
*   **`Icon`**: Import specific icons from `@ant-design/icons`. Use `style` prop for customization.
*   **`Divider`**: Displays a horizontal or vertical line.
    *   `type`: `horizontal` (default), `vertical`.
    *   `orientation`: `left`, `right`, `center` (for text within horizontal divider).
    *   `dashed`: Boolean.
*   **`Space`**: Manages spacing between inline/block elements.
    *   `direction`: `horizontal` (default), `vertical`.
    *   `size`: `small`, `middle` (default), `large`, or a custom number (pixels).
    *   `wrap`: Boolean to allow items to wrap to the next line.
    *   `align`: `start`, `end`, `center`, `baseline`.
*   **`Rate`**: Star rating component. Use `allowHalf`, `defaultValue`, `count`, `tooltips`.
*   **`Tag`**: For displaying tags, categories, labels. Use `color` (predefined or hex), `closable`, `icon`.
*   **`Spin`**: Indicates loading state. Can wrap content. Use `size`, `tip`.

Always import the specific components you need from `antd` to ensure proper tree-shaking and keep bundle sizes manageable. Refer to the official documentation for the full API of each component.

*(Refer to the official Ant Design documentation for each component.)*