# Ant Design: Data Display Components (Table, List, Card)

Using Ant Design components for displaying collections of data.

## 1. `Table`

*   **Purpose:** A powerful component for displaying tabular data with features like sorting, filtering, pagination, selection, and expandable rows.
*   **Import:** `import { Table } from 'antd';`
*   **Key Props:**
    *   `columns`: Array of column configuration objects. Each object defines:
        *   `title`: Header text for the column.
        *   `dataIndex`: Key in the data source object corresponding to this column's data. Can be a string or an array for nested data (e.g., `['address', 'city']`).
        *   `key`: Unique key for the column (often same as `dataIndex`).
        *   `render?: (text, record, index) => ReactNode`: Custom render function for cell content. `text` is the value from `dataIndex`, `record` is the entire row data object.
        *   `sorter?: (a, b) => number` or `boolean`: Enable sorting. If boolean, uses default sort. Provide function for custom sort logic.
        *   `filters?: { text: string, value: string | number }[]`: Array of filter options for the column header dropdown.
        *   `onFilter?: (value, record) => boolean`: Function to apply filtering logic.
        *   `width?: number | string`: Fixed width for the column.
        *   `fixed?: 'left' | 'right'`: Fix column position during horizontal scroll.
    *   `dataSource`: Array of data objects. Each object represents a row. **Must have a unique `key` property** for each object (React requirement).
    *   `pagination`: `false` to disable, or an object to configure pagination options (e.g., `{ pageSize: 10, showSizeChanger: true }`). Defaults to true.
    *   `loading`: Boolean to show loading indicator over the table.
    *   `rowSelection`: Object to configure row selection (checkboxes). See docs for details (`type: 'checkbox' | 'radio'`, `onChange`, `selectedRowKeys`).
    *   `expandable`: Object to configure expandable rows. See docs for details (`expandedRowRender`, `rowExpandable`).
    *   `onChange?: (pagination, filters, sorter, extra) => void`: Callback function triggered when pagination, filters, or sorter changes. Used for server-side data fetching/sorting/filtering.

```jsx
import React, { useState } from 'react';
import { Table, Tag, Space } from 'antd';
import type { TableProps } from 'antd'; // Import TableProps type

interface DataType {
  key: React.Key; // Required unique key
  name: string;
  age: number;
  address: string;
  tags: string[];
}

const columns: TableProps<DataType>['columns'] = [ // Define columns with type
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
    render: (text) => <a>{text}</a>, // Example custom render
    sorter: (a, b) => a.name.localeCompare(b.name),
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
    sorter: (a, b) => a.age - b.age,
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: 'Tags',
    key: 'tags',
    dataIndex: 'tags',
    render: (_, { tags }) => ( // Access tags from the record
      <>
        {tags.map((tag) => {
          let color = tag.length > 5 ? 'geekblue' : 'green';
          if (tag === 'loser') { color = 'volcano'; }
          return <Tag color={color} key={tag}>{tag.toUpperCase()}</Tag>;
        })}
      </>
    ),
    filters: [ // Example filters
      { text: 'Developer', value: 'developer' },
      { text: 'Designer', value: 'designer' },
    ],
    onFilter: (value, record) => record.tags.includes(value as string),
  },
  {
    title: 'Action',
    key: 'action',
    render: (_, record) => ( // Access record for actions
      <Space size="middle">
        <a>Invite {record.name}</a>
        <a>Delete</a>
      </Space>
    ),
  },
];

const data: DataType[] = [ // Example data source
  { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park', tags: ['nice', 'developer'] },
  { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park', tags: ['loser'] },
  { key: '3', name: 'Joe Black', age: 32, address: 'Sydney No. 1 Lake Park', tags: ['cool', 'teacher'] },
];

function TableDemo() {
  // Handle server-side changes if needed
  const handleTableChange: TableProps<DataType>['onChange'] = (pagination, filters, sorter) => {
    console.log('Table Changed:', pagination, filters, sorter);
    // Fetch new data based on changes
  };

  return <Table columns={columns} dataSource={data} onChange={handleTableChange} />;
}

export default TableDemo;
```

## 2. `List`

*   **Purpose:** A flexible component for displaying list data in various styles (vertical, grid). Simpler than `Table` for less structured data.
*   **Import:** `import { List, Avatar } from 'antd';`
*   **Key Props:**
    *   `dataSource`: Array of data items.
    *   `renderItem: (item, index) => ReactNode`: Function to render each item in the list.
    *   `grid`: Object to configure grid layout (e.g., `{ gutter: 16, column: 4 }` or responsive `{ xs: 1, sm: 2, md: 4 }`).
    *   `loading`: Boolean.
    *   `pagination`: `false` or pagination configuration object.
    *   `header`, `footer`: React nodes for header/footer sections.
    *   `itemLayout`: `'horizontal'` (default) or `'vertical'`.

```jsx
import React from 'react';
import { List, Avatar, Space } from 'antd';
import { MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons';

const data = Array.from({ length: 3 }).map((_, i) => ({ // Example data
  href: 'https://ant.design',
  title: `Ant Design Title ${i + 1}`,
  avatar: `https://api.dicebear.com/7.x/miniavs/svg?seed=${i}`,
  description: 'Ant Design, a design language for background applications.',
  content: 'We supply a series of design principles, practical patterns...',
}));

const IconText = ({ icon, text }: { icon: React.FC; text: string }) => (
  <Space>
    {React.createElement(icon)}
    {text}
  </Space>
);

function ListDemo() {
  return (
    <List
      itemLayout="vertical" // Vertical layout for blog-style posts
      size="large"
      pagination={{ pageSize: 3 }} // Example pagination
      dataSource={data}
      footer={<div><b>Ant Design</b> footer part</div>}
      renderItem={(item) => (
        <List.Item
          key={item.title}
          actions={[ // Actions at the bottom of each item
            <IconText icon={StarOutlined} text="156" key="list-vertical-star-o" />,
            <IconText icon={LikeOutlined} text="156" key="list-vertical-like-o" />,
            <IconText icon={MessageOutlined} text="2" key="list-vertical-message" />,
          ]}
          extra={ // Content floated to the right
            <img width={272} alt="logo" src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png" />
          }
        >
          <List.Item.Meta
            avatar={<Avatar src={item.avatar} />}
            title={<a href={item.href}>{item.title}</a>}
            description={item.description}
          />
          {item.content}
        </List.Item>
      )}
    />
  );
}
export default ListDemo;
```

## 3. `Card`

*   **Purpose:** A simple container for content, often used to group related information. Can be used within `List` or `Grid`.
*   **Import:** `import { Card } from 'antd';`
*   **Key Props:**
    *   `title`: Card title (React node).
    *   `extra`: Content floated to the top-right corner (React node).
    *   `cover`: Image or media displayed at the top (React node).
    *   `actions`: Array of React nodes displayed at the bottom.
    *   `loading`: Boolean.
    *   `bordered`: Boolean (default `true`).
    *   `hoverable`: Boolean to add lift-up effect on hover.
    *   `size`: `'default'` or `'small'`.

```jsx
import React from 'react';
import { Card, Avatar } from 'antd';
import { EditOutlined, EllipsisOutlined, SettingOutlined } from '@ant-design/icons';

const { Meta } = Card; // Sub-component for metadata (avatar, title, description)

function CardDemo() {
  return (
    <Card
      style={{ width: 300 }}
      cover={
        <img alt="example" src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png" />
      }
      actions={[ // Actions at the bottom
        <SettingOutlined key="setting" />,
        <EditOutlined key="edit" />,
        <EllipsisOutlined key="ellipsis" />,
      ]}
      hoverable
    >
      <Meta
        avatar={<Avatar src="https://api.dicebear.com/7.x/miniavs/svg?seed=1" />}
        title="Card title"
        description="This is the description"
      />
    </Card>
  );
}
export default CardDemo;
```

Choose the appropriate data display component based on the structure and complexity of your data. `Table` is for structured tabular data, `List` is for simpler lists or feeds, and `Card` is for self-contained blocks of information.

*(Refer to the official Ant Design documentation for Table, List, and Card.)*