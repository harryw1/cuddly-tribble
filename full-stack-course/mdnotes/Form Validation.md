# Form Validation

## Introduction

Some forms on webpages are not optional, and the user must fill them out. In this case, it is important to validate the form before submitting it. This is to ensure that the user has entered the correct information and that the form can be processed correctly.

For example:

```html
<form action="/example.html" method="POST">
  <label for="allergies">Do you have any dietary restrictions?</label>
  <br>
  <input id="allergies" name="allergies" type="text" required>
  <br>
  <input type="submit" value="Submit">
</form>
```

In this example, the user must enter their dietary restrictions before submitting the form. If they do not, the form will not be submitted.

## Required Attribute

The `required` attribute can be added to form elements to indicate that the user must fill out the field before submitting the form. If the user tries to submit the form without filling out the required field, they will receive an error message. The kind of error message depends on the browser.

### Number Input Example

```html
<form action="/example.html" method="POST">
  <label for="guests">Enter # of guests:</label>
  <input id="guests" name="guests" type="number" min="1" max="4">
  <input type="submit" value="Submit">
</form>
```

In this form, the user must enter a number between 1 and 4. We have both the `required` attribute and a `min` and `max`.

### Text Input Example

```html
<form action="/example.html" method="POST">
  <label for="summary">Summarize your feelings in less than 250 characters</label>
  <input id="summary" name="summary" type="text" minlength="5" maxlength="250" required>
  <input type="submit" value="Submit">
</form>
```

In this form, the user must enter a text that is at least 5 characters long and at most 250 characters long.

## Custom Validation and Pattern Matching

In some cases, the `required` attribute is not enough to validate the form. For example, if you want to validate an email address, you can use the `pattern` attribute.

### Credit Card Example

```html
<form action="/example.html" method="POST">
  <label for="payment">Credit Card Number (no spaces):</label>
  <br>
  <input id="payment" name="payment" type="text" required pattern="[0-9]{14,16}">
  <input type="submit" value="Submit">
</form>
```

The `pattern` attribute uses a regular expression to validate the input. We're asking the form to match any number between 0 and 9, and the length should be between 14 and 16 characters.
