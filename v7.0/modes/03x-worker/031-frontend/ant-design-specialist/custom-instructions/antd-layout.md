# Ant Design: Layout Components (Layout, Grid)

Structuring page layouts using Ant Design's `Layout` and `Grid` components.

## 1. `Layout` Component

*   **Purpose:** Provides components for common page structures like headers, footers, sidebars, and main content areas. Typically used for the overall page structure.
*   **Components:**
    *   `<Layout>`: The main container. Can be nested. If it contains a `<Sider>`, it automatically arranges horizontally.
    *   `<Layout.Header>`: Top header section.
    *   `<Layout.Footer>`: Bottom footer section.
    *   `<Layout.Sider>`: Sidebar component. Can be collapsible.
    *   `<Layout.Content>`: Main content area.
*   **Import:** `import { Layout } from 'antd'; const { Header, Footer, Sider, Content } = Layout;`

```jsx
import React, { useState } from 'react';
import { Layout, Menu, Breadcrumb, theme } from 'antd'; // Import Layout and other needed components
import { DesktopOutlined, PieChartOutlined, UserOutlined } from '@ant-design/icons';

const { Header, Content, Footer, Sider } = Layout;

function getItem(label, key, icon, children) { // Helper for Menu items
  return { key, icon, children, label };
}
const items = [ // Example Menu items
  getItem('Option 1', '1', <PieChartOutlined />),
  getItem('Option 2', '2', <DesktopOutlined />),
  getItem('User', 'sub1', <UserOutlined />, [
    getItem('Tom', '3'),
    getItem('Bill', '4'),
  ]),
];

function AppLayout() {
  const [collapsed, setCollapsed] = useState(false);
  const { token: { colorBgContainer, borderRadiusLG } } = theme.useToken(); // Access theme tokens

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* Sidebar */}
      <Sider collapsible collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
        <div className="demo-logo-vertical" /> {/* Placeholder for logo */}
        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} />
      </Sider>

      {/* Main Area */}
      <Layout>
        {/* Header */}
        <Header style={{ padding: '0 16px', background: colorBgContainer }}>
          {/* Header content */}
          My App Header
        </Header>

        {/* Content Area */}
        <Content style={{ margin: '0 16px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>User</Breadcrumb.Item>
            <Breadcrumb.Item>Bill</Breadcrumb.Item>
          </Breadcrumb>
          <div style={{ padding: 24, minHeight: 360, background: colorBgContainer, borderRadius: borderRadiusLG }}>
            Bill is a cat.
            {/* Main page content goes here */}
          </div>
        </Content>

        {/* Footer */}
        <Footer style={{ textAlign: 'center' }}>
          Ant Design ©{new Date().getFullYear()} Created by Ant UED
        </Footer>
      </Layout>
    </Layout>
  );
}

export default AppLayout;

// Add some basic CSS for the logo placeholder if needed
// .demo-logo-vertical { height: 32px; margin: 16px; background: rgba(255, 255, 255, 0.2); border-radius: 6px; }
```

## 2. Grid System (`Row`, `Col`)

*   **Purpose:** A responsive 24-column grid system based on Flexbox, used for arranging content within a horizontal row. Essential for creating responsive layouts that adapt to different screen sizes.
*   **Components:**
    *   `<Row>`: Container for columns. Uses Flexbox.
    *   `<Col>`: Represents a column within a `<Row>`. Spans a certain number of the 24 available columns.
*   **Import:** `import { Row, Col } from 'antd';`
*   **Key Props:**
    *   **`<Row>`:**
        *   `gutter={[horizontalGutter, verticalGutter]}`: Spacing between columns (e.g., `[16, 16]` for 16px horizontal and vertical). Can be a single number for horizontal only. Can also be responsive object `{ xs: 8, sm: 16, md: 24 }`.
        *   `justify`: Flexbox `justify-content` (`start`, `end`, `center`, `space-around`, `space-between`).
        *   `align`: Flexbox `align-items` (`top`, `middle`, `bottom`).
    *   **`<Col>`:**
        *   `span={number}`: Number of columns (out of 24) the column should span by default.
        *   **Responsive Spans:** Use object notation for different screen sizes: `{ xs: 24, sm: 12, md: 8, lg: 6, xl: 4 }`. Breakpoints: `xs` (<576px), `sm` (≥576px), `md` (≥768px), `lg` (≥992px), `xl` (≥1200px), `xxl` (≥1600px).
        *   `offset={number}`: Number of columns to offset (push) the column to the right. Responsive object possible.
        *   `order={number}`: Order of the column within the row. Responsive object possible.
        *   `pull={number}`, `push={number}`: Move column left/right without changing order. Responsive object possible.

```jsx
import React from 'react';
import { Row, Col, Divider } from 'antd';

function GridDemo() {
  const style = { background: '#0092ff', padding: '8px 0', color: 'white', textAlign: 'center' };

  return (
    <div>
      <Divider orientation="left">Basic Grid</Divider>
      <Row gutter={[16, 16]}> {/* 16px horizontal & vertical gutter */}
        <Col span={8}><div style={style}>col-8</div></Col>
        <Col span={8}><div style={style}>col-8</div></Col>
        <Col span={8}><div style={style}>col-8</div></Col>
        <Col span={6}><div style={style}>col-6</div></Col>
        <Col span={6}><div style={style}>col-6</div></Col>
        <Col span={6}><div style={style}>col-6</div></Col>
        <Col span={6}><div style={style}>col-6</div></Col>
      </Row>

      <Divider orientation="left">Responsive Grid</Divider>
      <Row gutter={16}>
        {/* Full width on extra small, half on small, third on medium, quarter on large+ */}
        <Col xs={24} sm={12} md={8} lg={6}><div style={style}>Responsive Col</div></Col>
        <Col xs={24} sm={12} md={8} lg={6}><div style={style}>Responsive Col</div></Col>
        <Col xs={24} sm={12} md={8} lg={6}><div style={style}>Responsive Col</div></Col>
        <Col xs={24} sm={12} md={8} lg={6}><div style={style}>Responsive Col</div></Col>
      </Row>

      <Divider orientation="left">Offset</Divider>
      <Row>
        <Col span={8}><div style={style}>col-8</div></Col>
        <Col span={8} offset={8}><div style={style}>col-8 offset-8</div></Col>
      </Row>
    </div>
  );
}

export default GridDemo;
```

Use `Layout` for the overall page structure and `Row`/`Col` for arranging content within sections, ensuring responsiveness across devices.

*(Refer to the official Ant Design documentation for Layout and Grid.)*