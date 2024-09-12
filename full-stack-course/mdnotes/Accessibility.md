# Digital Accessibility

## Introduction

Digital accessibility is the practice of making digital content accessible to people with disabilities. This includes websites, software, and other digital tools. Accessibility is important because it ensures that everyone can access and use digital content, regardless of their abilities.

## Guidelines

The current guidelines can be found at the [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) website. These guidelines provide a framework for making digital content accessible to people with disabilities. The guidelines are organized into four principles: perceivable, operable, understandable, and robust.

## Tools

There are many ways to make digital content more accessible. For exmaple, we can use contrast, alt text, and keyboard navigation.

### Contrast

Contrast is an important aspect of accessibility. It ensures that text is readable and distinguishable from the background. To improve contrast, use dark text on a light background or vice versa. Having dark text on a dark background or light text on a light background can make it difficult for people with visual impairments, or even those without vision impairements, to read the content.

### Headings and Structure

Headings and structure are important for making content more accessible. Use headings to organize content and make it easier to navigate. This helps people with screen readers or other assistive technologies to understand the structure of the content.

Each webpage should only have one `<h1>` tag, which is the main heading of the page. Use `<h2>` tags for subheadings, `<h3>` tags for sub-subheadings, and so on. This helps to create a logical structure for the content.

### Text Accessibility

Good practice is to use real text rather than images of text, use high contrast text and backgrounds, and ensure that text is readable and understandable. Screen readers can have difficulty reading text that is part of an image, so it is important to use real text whenever possible. It's also easier for a client browser to load text than an image, which can help improve page load times.

#### Contrasting Colors

According to the WCAG guidelines, the contrast ratio between text and its background should be at least 4.5:1 for normal text and 3:1 for large text. This ensures that text is readable and distinguishable from the background. Here's a great tool to check the contrast ratio of text: [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

#### Font Sizes

The standard font size for most modern web browsers is 16px. This is a good starting point for most websites, but it's important to consider the needs of your users. Some users may need larger text to read comfortably, so it's a good idea to provide options for increasing the font size.

### Colors

Color is an important aspect of accessibility. Some people have color blindness or low vision, so it's important to use color wisely. Avoid using color as the only way to convey information, and ensure that text is readable and distinguishable from the background.

From Codeacademy:

> For instance, using the combination of black (`#000000`) as a foreground color and white (`#ffffff`) as a background color provides maximum contrast. While this is a fairly common color combination for text on a page, the high contrast can also cause glare that will increase strain on the user’s eyes over time.

### Color Blindness

Color blindness is a common condition that affects how people perceive colors. There are different types of color blindness, but the most common type is red-green color blindness. This means that people with this condition have difficulty distinguishing between red and green colors. Approximately 8% of men and 0.5% of women have a color vision deficiency.

## Best Practices

Here are some best practices for making digital content accessible:

1. Use alt text for images: Alt text provides a textual description of an image, which is important for people who are visually impaired or using screen readers.
2. Text overlaid on images: Avoid placing text directly on top of images, as this can make it difficult to read.
3. Use descriptive link text: Link text should be descriptive and provide context about where the link will take the user.
4. Buttons and links: Make sure that buttons and links are easily clickable and distinguishable from other content.

## Accessible Elements

Digital accessibility is an important aspect of web development. By following best practices and guidelines, we can ensure that digital content is accessible to everyone, regardless of their abilities. This helps to create a more inclusive and equitable online experience for all users.

## Accessible Rich Internet Applications (ARIA)

Accessible Rich Internet Applications (ARIA) is a set of attributes that can be added to HTML elements to improve accessibility. ARIA provides additional information to assistive technologies, such as screen readers, to help users navigate and interact with web content.

This lesson covers:
1. Semantic Elements
2. ARIA Roles
3. ARIA Properties
4. `alt` Attributes

### Semantic Elements

Semantic elements are HTML elements that provide meaning to the content they contain. For example, the `<header>` element is used to define the header of a webpage, while the `<nav>` element is used to define a navigation menu. By using semantic elements, we can create a more accessible and understandable structure for our content.

### ARIA Role

ARIA roles are attributes that can be added to HTML elements to define their purpose or function. For example, the `role="button"` attribute can be added to a `<div>` element to make it behave like a button. ARIA roles help assistive technologies, such as screen readers, to understand the purpose of an element and how it should be interacted with. [Aria in HTML](https://www.w3.org/TR/html-aria/#allowed-aria-roles-states-and-properties) provides a list of allowed ARIA roles, states, and properties.

#### ARIA Role: Presentation

The `role="presentation"` attribute can be used to indicate that an element should be treated as a presentational element and not be announced by assistive technologies. This can be useful for decorative elements that do not convey any meaningful information to the user.

### `alt` Attributes

The `alt` attribute is used to provide a textual description of an image. This is important for people who are visually impaired or using screen readers, as it allows them to understand the content of the image. The `alt` will be loaded in place of the image if the image file is not found, the user's connection is slow, or if the user is using a screen reader.
