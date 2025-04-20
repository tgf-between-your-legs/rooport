# Ant Design Form Handling

Best practices and examples for using `antd` Form components in React.

## Core Components

*   **`<Form>`:** Wrapper component for the form. Handles submission (`onFinish`, `onFinishFailed`) and provides form instance via `Form.useForm()`.
*   **`<Form.Item>`:** Wrapper for individual form controls. Connects the control to the form state and handles layout, labels, validation messages.
    *   `name`: String identifying the field in the form data object.
    *   `label`: Text label for the field.
    *   `rules`: Array of validation rule objects.
    *   `dependencies`: Array of other field names; triggers re-validation when dependencies change.
    *   `shouldUpdate`: Function to control when the `Form.Item` re-renders based on form state changes.
*   **Input Controls:** Standard `antd` input components (`<Input>`, `<Select>`, `<Checkbox>`, `<Radio.Group>`, `<DatePicker>`, etc.) placed *inside* `<Form.Item>`.

## Getting Form Instance

Use the `Form.useForm()` hook to get access to the form instance API.

```jsx
import { Form, Input, Button } from 'antd';

const MyForm = () => {
  const [form] = Form.useForm(); // Get form instance

  const onFinish = (values) => {
    console.log('Success:', values);
    // Call API, etc.
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  const resetForm = () => {
    form.resetFields();
  };

  return (
    <Form
      form={form} // Pass instance to Form
      name="basic"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      {/* Form Items go here */}
      <Button type="primary" htmlType="submit">Submit</Button>
      <Button htmlType="button" onClick={resetForm}>Reset</Button>
    </Form>
  );
};
```

## Validation (`rules`)

Define validation rules as an array of objects on `<Form.Item>`.

```jsx
<Form.Item
  label="Username"
  name="username"
  rules={[
    { required: true, message: 'Please input your username!' },
    { min: 3, message: 'Username must be at least 3 characters!' },
    { pattern: /^[a-zA-Z0-9_]+$/, message: 'Username can only include letters, numbers, and underscores!' }
  ]}
>
  <Input />
</Form.Item>

<Form.Item
  label="Password"
  name="password"
  rules={[{ required: true, message: 'Please input your password!' }]}
>
  <Input.Password />
</Form.Item>

// Custom Validator
<Form.Item
  label="Confirm Password"
  name="confirm"
  dependencies={['password']} // Re-validate when 'password' changes
  rules={[
    { required: true, message: 'Please confirm your password!' },
    ({ getFieldValue }) => ({
      validator(_, value) {
        if (!value || getFieldValue('password') === value) {
          return Promise.resolve();
        }
        return Promise.reject(new Error('The two passwords do not match!'));
      },
    }),
  ]}
>
  <Input.Password />
</Form.Item>
```

## Common Form Instance Methods (`form.*`)

*   `form.getFieldValue('fieldName')`: Get value of a single field.
*   `form.getFieldsValue()`: Get values of all fields (or specified fields).
*   `form.setFieldsValue({ fieldName: value, ... })`: Set values for one or more fields.
*   `form.resetFields()`: Reset fields to initial values.
*   `form.validateFields()`: Programmatically trigger validation.
*   `form.submit()`: Programmatically submit the form.

## Dynamic Form Items (`Form.List`)

Use `Form.List` for managing dynamic arrays of form fields (e.g., adding multiple phone numbers).

```jsx
<Form.List name="users">
  {(fields, { add, remove }) => (
    <>
      {fields.map(({ key, name, ...restField }) => (
        <Space key={key} style={{ display: 'flex', marginBottom: 8 }} align="baseline">
          <Form.Item
            {...restField}
            name={[name, 'first']}
            rules={[{ required: true, message: 'Missing first name' }]}
          >
            <Input placeholder="First Name" />
          </Form.Item>
          <Form.Item
            {...restField}
            name={[name, 'last']}
            rules={[{ required: true, message: 'Missing last name' }]}
          >
            <Input placeholder="Last Name" />
          </Form.Item>
          <MinusCircleOutlined onClick={() => remove(name)} />
        </Space>
      ))}
      <Form.Item>
        <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined />}>
          Add field
        </Button>
      </Form.Item>
    </>
  )}
</Form.List>
```

*(Refer to the official Ant Design Form documentation for more complex scenarios and component-specific props: https://ant.design/components/form)*