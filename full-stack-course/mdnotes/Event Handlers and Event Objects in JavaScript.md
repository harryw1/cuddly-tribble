# Event Handlers and Event Objects in JavaScript

## Event Handlers

Event handlers are functions that get executed when a specific event occurs. They allow you to respond to user interactions or other changes in the webpage.

### Ways to Add Event Handlers

1. **HTML attribute**:
   ```html
   <button onclick="handleClick()">Click me</button>
   ```
2. **DOM property**:
   ```javascript
   document.getElementById("myButton").onclick = handleClick;
   ```
3. **addEventListener method** (recommended):
   ```javascript
   document
     .getElementById("myButton")
     .addEventListener("click", handleClick);
   ```

## Event Objects

When an event occurs, the browser creates an event object containing details about the event. This object is automatically passed to the event handler function.

### Common Properties of Event Objects

- `type`: The type of event (e.g., 'click', 'keydown')
- `target`: The element that triggered the event
- `currentTarget`: The element that the event handler is attached to
- `timeStamp`: The time when the event occurred

## Examples

Examples demonstrating event handlers and event objects:

### Example 1: Click Event

```javascript
function handleClick(event) {
  console.log("Button clicked!");
  console.log("Event type:", event.type);
  console.log("Target element:", event.target);
}

document
  .getElementById("myButton")
  .addEventListener("click", handleClick);
```

### Example 2: Keydown Event

```javascript
function handleKeydown(event) {
  console.log("Key pressed:", event.key);
  if (event.key === "Enter") {
    console.log("Enter key was pressed!");
  }
}

document.addEventListener("keydown", handleKeydown);
```

### Example 3: Form Submit Event

```javascript
function handleSubmit(event) {
  event.preventDefault(); // Prevent form from submitting
  console.log("Form submitted!");
  // Perform form validation or data processing here
}

document
  .getElementById("myForm")
  .addEventListener("submit", handleSubmit);
```

### Example 4: Mouse Events

```javascript
function handleMouseMove(event) {
  console.log("Mouse position:", event.clientX, event.clientY);
}

document.addEventListener("mousemove", handleMouseMove);
```

#home/fullstack
