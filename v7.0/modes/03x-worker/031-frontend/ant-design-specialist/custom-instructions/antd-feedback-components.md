# Ant Design: Feedback Components (Modal, Message, Notification, Popconfirm)

Using Ant Design components to provide feedback and confirmation to users.

## 1. `Modal`

*   **Purpose:** Displays content in a layer above the main page, requiring user interaction to dismiss. Used for important confirmations, forms, or detailed information.
*   **Import:** `import { Modal, Button } from 'antd';`
*   **Usage:** Typically controlled using `useState` for visibility.
*   **Key Props:**
    *   `open`: Boolean state controlling visibility.
    *   `title`: Title of the modal (React node).
    *   `onOk`: Callback function when the user clicks the OK button.
    *   `onCancel`: Callback function when the user clicks the cancel button, close icon, or presses Esc.
    *   `confirmLoading`: Boolean to show loading state on the OK button.
    *   `footer`: Custom footer content (React node), or `null` to hide the default footer.
    *   `width`, `centered`, `maskClosable`, etc.
*   **Static Methods:** `Modal.info()`, `Modal.success()`, `Modal.error()`, `Modal.warning()`, `Modal.confirm()` provide convenient ways to show simple feedback dialogs without managing `open` state manually.

```jsx
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

function ModalDemo() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [confirmLoading, setConfirmLoading] = useState(false);

  const showModal = () => setIsModalOpen(true);

  const handleOk = () => {
    setConfirmLoading(true);
    console.log('OK clicked');
    // Simulate async action
    setTimeout(() => {
      setIsModalOpen(false);
      setConfirmLoading(false);
    }, 1500);
  };

  const handleCancel = () => {
    console.log('Cancel clicked');
    setIsModalOpen(false);
  };

  // Static confirmation method
  const showConfirm = () => {
    Modal.confirm({
      title: 'Do you want to delete these items?',
      content: 'Some descriptions',
      okText: 'Yes',
      okType: 'danger',
      cancelText: 'No',
      onOk() {
        console.log('Confirm OK');
      },
      onCancel() {
        console.log('Confirm Cancel');
      },
    });
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>Open Modal</Button>
      <Button onClick={showConfirm} style={{ marginLeft: 8 }}>Show Confirm</Button>

      <Modal
        title="Basic Modal"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
        confirmLoading={confirmLoading}
        okText="Submit"
        cancelText="Close"
      >
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Modal>
    </>
  );
}

export default ModalDemo;
```

## 2. `message`

*   **Purpose:** Displays global messages at the top center of the screen, usually for brief feedback on operations (e.g., "Save successful"). Automatically dismisses.
*   **Import:** `import { message, Button } from 'antd';`
*   **Usage:** Call static methods directly: `message.success()`, `message.error()`, `message.warning()`, `message.info()`, `message.loading()`.
*   **Configuration:** Can configure duration, max count, etc. globally using `message.config()`. Returns a function to destroy the message if needed.

```jsx
import React from 'react';
import { message, Button, Space } from 'antd';

function MessageDemo() {
  const [messageApi, contextHolder] = message.useMessage(); // Hook for context access (recommended)

  const showSuccess = () => messageApi.success('Operation successful!');
  const showError = () => messageApi.error('Operation failed!');
  const showLoading = () => {
    const key = 'loadingMsg'; // Unique key to update/destroy later
    messageApi.loading({ content: 'Action in progress...', key });
    setTimeout(() => {
      messageApi.success({ content: 'Loaded!', key, duration: 2 });
    }, 2000);
  };

  return (
    <>
      {contextHolder} {/* Render context holder */}
      <Space>
        <Button onClick={showSuccess}>Success Message</Button>
        <Button onClick={showError} danger>Error Message</Button>
        <Button onClick={showLoading}>Loading Message</Button>
      </Space>
    </>
  );
}
export default MessageDemo;
```

## 3. `notification`

*   **Purpose:** Displays global notification boxes in a corner of the screen (default top-right). Suitable for more detailed information or messages that shouldn't interrupt the user flow as much as a `Modal`.
*   **Import:** `import { notification, Button } from 'antd';`
*   **Usage:** Call static methods: `notification.success()`, `notification.error()`, `notification.warning()`, `notification.info()`, or `notification.open()`. Takes an object with `message`, `description`, `placement`, `duration`, `icon`, etc.
*   **Configuration:** Global config via `notification.config()`. Use `notification.useNotification()` hook for context access.

```jsx
import React from 'react';
import { notification, Button, Space } from 'antd';
import { SmileOutlined } from '@ant-design/icons';

function NotificationDemo() {
  const [api, contextHolder] = notification.useNotification();

  const openNotification = (type) => {
    api[type]({ // Use dynamic type: success, info, warning, error
      message: `Notification Title (${type})`,
      description: 'This is the content of the notification. This is the content.',
      placement: 'topRight', // bottomRight, bottomLeft, topLeft
      duration: 4.5, // seconds, 0 for persistent
      icon: type === 'success' ? <SmileOutlined style={{ color: '#108ee9' }} /> : null,
    });
  };

  return (
    <>
      {contextHolder}
      <Space>
        <Button onClick={() => openNotification('success')}>Success</Button>
        <Button onClick={() => openNotification('info')}>Info</Button>
        <Button onClick={() => openNotification('warning')}>Warning</Button>
        <Button onClick={() => openNotification('error')} danger>Error</Button>
      </Space>
    </>
  );
}
export default NotificationDemo;
```

## 4. `Popconfirm`

*   **Purpose:** A small popover confirmation dialog attached to an element, typically used for confirming actions like deletion.
*   **Import:** `import { Popconfirm, Button, message } from 'antd';`
*   **Usage:** Wrap the trigger element (e.g., a Button) with `<Popconfirm>`.
*   **Key Props:**
    *   `title`: The confirmation question text.
    *   `onConfirm`: Callback function executed when the user clicks "Yes".
    *   `onCancel`: Callback function executed when the user clicks "No".
    *   `okText`, `cancelText`: Customize button labels.
    *   `disabled`: Boolean to disable the popconfirm.

```jsx
import React from 'react';
import { Popconfirm, Button, message } from 'antd';

function PopconfirmDemo() {
  const confirm = (e) => {
    console.log(e);
    message.success('Delete confirmed');
    // Perform delete action here
  };

  const cancel = (e) => {
    console.log(e);
    message.error('Delete cancelled');
  };

  return (
    <Popconfirm
      title="Delete the task"
      description="Are you sure you want to delete this task?"
      onConfirm={confirm}
      onCancel={cancel}
      okText="Yes"
      cancelText="No"
    >
      <Button danger>Delete</Button>
    </Popconfirm>
  );
}
export default PopconfirmDemo;
```

Choose the appropriate feedback component based on the importance and intrusiveness required for the user interaction. Use `message` for brief status updates, `notification` for more detailed but non-blocking info, `Popconfirm` for simple confirmations, and `Modal` for critical confirmations or complex interactions.

*(Refer to the official Ant Design documentation for Modal, Message, Notification, and Popconfirm.)*