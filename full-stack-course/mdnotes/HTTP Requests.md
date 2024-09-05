# Forms, Requests, and Information

## HTTP Requests

In the most recent module that I started, the focus has been on
users interacting with a webpage to do more than just create requests
from the serve to change information on the screen. Now we're getting
into make requests from the client to the server to change information
on the server. For example, we may have users submit a form to create
a new user account, or to update their profile information.

## Example Form

Here is an example from Codeacademy that shows how we might have a
form element that calls an action and a `POST` method to send the
information to the server.

```html
<form action="/example" method="POST"></form>
```

In this example above, we have a `form` element that has an `action`
attribute that points to the `/example` route or path on the server.

The `method` attribute is set to `POST` which means that the form
will send the information to the server in the body of the request.

## Form Practice

Codeacademy has a practice exercise that has us create a form that
will send information to the server. Here is the code that I wrote:

```html
<form action="/practice.html" method="POST">
  <h1>Burgers!</h1>
  <p>Here's a fun place to put a form about burgers!</p>
</form>
```

## `<input>` Elements

The `input` element is used to create form fields that users can
enter information into. A form is really not a form without the ability for users to enter information.

The `input` element has a `type` attribute that specifies the type of rendering and expected input. In this first example, we have a `text` input type that will render a text field for users to enter information.

```html
<form action="/example.html" method="POST">
  <input type="text" name="first-text-field" />
</form>
```

In this example, we have a `text` input field that will render a text field for users to enter information. The `name` attribute is used to identify the field when the form is submitted. We can decide whether a blank field value to start is appropriate or not and set a default value with the `value` attribute.

```html
<form action="/example.html" method="POST">
  <input
    type="text"
    name="first-text-field"
    value="Enter your name"
  />
</form>
```

## `<label>` Elements

The `label` element is used to create a label for an `input` element. This is useful for accessibility and usability reasons and it will help a user identify what information is expected in the field.

```html

```
