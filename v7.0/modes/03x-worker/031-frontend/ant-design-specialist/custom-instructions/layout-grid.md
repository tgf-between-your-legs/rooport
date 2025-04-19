# Ant Design Grid System (`Row`, `Col`)

Guide to using Ant Design's responsive grid system for layout. Based on a 24-column grid.

## Core Components

*   **`<Row>`:** Container for columns. Can control alignment and spacing.
*   **`<Col>`:** Represents a column within a row. Spans a certain number of the 24 available columns.

## Basic Usage

```jsx
import { Row, Col } from 'antd';

const MyLayout = () => (
  <>
    {/* Two equal columns */}
    <Row>
      <Col span={12}>Column 1 (12/24)</Col>
      <Col span={12}>Column 2 (12/24)</Col>
    </Row>

    {/* Three equal columns */}
    <Row>
      <Col span={8}>Column A (8/24)</Col>
      <Col span={8}>Column B (8/24)</Col>
      <Col span={8}>Column C (8/24)</Col>
    </Row>

    {/* Unequal columns */}
    <Row>
      <Col span={6}>Sidebar (6/24)</Col>
      <Col span={18}>Main Content (18/24)</Col>
    </Row>
  </>
);
```

## Responsive Design

Use breakpoint props (`xs`, `sm`, `md`, `lg`, `xl`, `xxl`) on `<Col>` to define different spans, offsets, or orders for different screen sizes. Follows a mobile-first approach if only larger breakpoints are specified.

*   `xs`: <576px (Mobile)
*   `sm`: ≥576px (Tablet)
*   `md`: ≥768px (Small Desktop / Large Tablet)
*   `lg`: ≥992px (Desktop)
*   `xl`: ≥1200px (Large Desktop)
*   `xxl`: ≥1600px (X-Large Desktop)

```jsx
<Row>
  {/* On mobile (xs), takes full width (24). On tablet (sm) and up, takes half width (12). */}
  <Col xs={24} sm={12}>
    Content A
  </Col>
  {/* On mobile (xs), takes full width (24). On tablet (sm) and up, takes half width (12). */}
  <Col xs={24} sm={12}>
    Content B
  </Col>
</Row>

<Row>
  {/* Complex example: Mobile: Full width. Tablet: Half width. Desktop: One-third width. */}
  <Col xs={24} sm={12} md={8}>Item 1</Col>
  <Col xs={24} sm={12} md={8}>Item 2</Col>
  <Col xs={24} sm={12} md={8}>Item 3</Col>
</Row>
```

## Gutters

Add spacing between columns using the `gutter` prop on `<Row>`. Can be a single number (horizontal gutter) or an array `[horizontal, vertical]`. Can also be responsive.

```jsx
{/* Horizontal and vertical gutters */}
<Row gutter={[16, 24]}>
  <Col span={8}>Col</Col>
  <Col span={8}>Col</Col>
  <Col span={8}>Col</Col>
  <Col span={8}>Col</Col>
  {/* ... more cols */}
</Row>

{/* Responsive gutters */}
<Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
  <Col span={6}>Col</Col>
  {/* ... */}
</Row>
```

## Alignment & Justification (on `<Row>`)

*   **`justify`**: Horizontal alignment of columns within the row (`start`, `end`, `center`, `space-around`, `space-between`, `space-evenly`).
*   **`align`**: Vertical alignment of columns within the row (`top`, `middle`, `bottom`, `stretch`).

```jsx
<Row justify="center" align="middle" style={{ height: '200px', background: '#eee' }}>
  <Col span={4}>Centered Col</Col>
  <Col span={4}>Centered Col</Col>
</Row>
```

## Offset & Order (on `<Col>`)

*   **`offset`**: Push a column to the right by a number of grid columns.
*   **`order`**: Change the visual order of columns. Can be responsive.

```jsx
<Row>
  <Col span={8}>Col 1</Col>
  <Col span={8} offset={8}>Col 2 (Pushed right)</Col>
</Row>

<Row>
  <Col span={12} xs={{ order: 2 }} sm={{ order: 1 }}>Content A (Second on mobile)</Col>
  <Col span={12} xs={{ order: 1 }} sm={{ order: 2 }}>Content B (First on mobile)</Col>
</Row>
```

*(Refer to the official Ant Design Grid documentation for all props and advanced usage: https://ant.design/components/grid)*