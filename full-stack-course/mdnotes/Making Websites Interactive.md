# Making Websites Interactive

## Scripts Tag

The same way we link to stylesheets externally, we can refer to external JS scripts by defining a `<script>` tag where we then link to our JS file.

## `defer` and `async`

Asynchronous code is the defining feature of modern webpages and the `async` attribute loads and executes the script asynchronously with the rest of the webpage.

We use `async` when we want to run a script independently of the webpage loading and it does not matter if the content from the function is returned immediately. **This significantly improves the client experience of a webpage.**

## What is the DOM?

The DOM, Document Object Model, is a representation of a webpage and defines the layout and interaction of elements on the webpage.
![](Making%20Websites%20Interactive/image.png)
This screenshot from Codeacademy does a great job of explaining the relationship between our HTML and our scripts.
![](Making%20Websites%20Interactive/image%202.png)
This screenshot shows the difference between the HTML we write and the DOM.
#home/fullstack
