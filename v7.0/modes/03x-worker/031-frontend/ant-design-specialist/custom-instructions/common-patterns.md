# Common Ant Design Patterns

Examples of implementing common UI patterns using Ant Design components.

## 1. Data Table with Sorting and Filtering

```jsx
import React, { useState, useEffect } from 'react';
import { Table, Input } from 'antd';
import type { TableProps } from 'antd';

interface DataType {
  key: React.Key;
  name: string;
  age: number;
  address: string;
}

// Assume fetchUsers is a function that fetches data
// const fetchUsers = async (): Promise<DataType[]> => { ... };

const UserTable: React.FC = () => {
  const [data, setData] = useState<DataType[]>([]);
  const [loading, setLoading] = useState(false);
  const [searchText, setSearchText] = useState('');

  useEffect(() => {
    setLoading(true);
    // Replace with actual data fetching
    Promise.resolve([
      { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
      { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
    ]).then(fetchedData => {
      setData(fetchedData);
      setLoading(false);
    });
  }, []);

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchText(e.target.value.toLowerCase());
  };

  const filteredData = data.filter(item =>
    item.name.toLowerCase().includes(searchText) ||
    item.address.toLowerCase().includes(searchText)
  );

  const columns: TableProps<DataType>['columns'] = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
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
  ];

  return (
    <div>
      <Input
        placeholder="Search Name or Address"
        onChange={handleSearch}
        style={{ marginBottom: 16, width: 300 }}
      />
      <Table
        columns={columns}
        dataSource={filteredData}
        loading={loading}
        rowKey="key"
      />
    </div>
  );
};

export default UserTable;
```

## 2. Modal Dialog Confirmation

```jsx
import React, { useState } from 'react';
import { Button, Modal } from 'antd';

const DeleteConfirmation: React.FC<{ onConfirm: () => void }> = ({ onConfirm }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    onConfirm(); // Call the passed-in confirm function
    setIsModalOpen(false);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <Button type="primary" danger onClick={showModal}>
        Delete Item
      </Button>
      <Modal
        title="Confirm Deletion"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Confirm Delete"
        cancelText="Cancel"
        okButtonProps={{ danger: true }}
      >
        <p>Are you sure you want to delete this item? This action cannot be undone.</p>
      </Modal>
    </>
  );
};

export default DeleteConfirmation;
```

## 3. Using `message` for Feedback

```jsx
import React from 'react';
import { Button, message, Space } from 'antd';

const FeedbackDemo: React.FC = () => {
  const [messageApi, contextHolder] = message.useMessage();

  const showSuccess = () => {
    messageApi.open({
      type: 'success',
      content: 'Operation successful!',
    });
  };

  const showError = () => {
    messageApi.open({
      type: 'error',
      content: 'Operation failed. Please try again.',
    });
  };

   const showLoading = () => {
    messageApi.open({
      type: 'loading',
      content: 'Processing...',
      duration: 0, // Keep open until manually closed
    });
    // Simulate closing after delay
    setTimeout(() => messageApi.destroy(), 2500);
  };


  return (
    <>
      {contextHolder} {/* Important: Renders the message container */}
      <Space>
        <Button onClick={showSuccess}>Show Success</Button>
        <Button onClick={showError}>Show Error</Button>
         <Button onClick={showLoading}>Show Loading</Button>
      </Space>
    </>
  );
};

export default FeedbackDemo;
```

*(These examples show basic implementations. Adapt them based on specific application logic, state management, and styling needs.)*