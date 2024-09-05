# Form Validation

This is where things become interesting in terms of complexity. Now we have to start to thing about websites that aren’t just displaying information, but are accepting, validating, checking and storing data. So now, we have a back-end serving data to the front-end, which can also receive data from users and clients to send back to the back-end. This module is all about forms and form validation.

## Why Validate?

I really like the way Codeacademy breaks this down, so I am going to quote them below:

> Most data, once submitted, is stored by a website or web application. It’s stored in a ~[database](https://www.codecademy.com/resources/docs/general/database)~ on the ~[server](https://www.codecademy.com/resources/docs/general/server)~ side. There are important reasons for us to make sure the information that will be stored in the database is accurate.
>
> We want operations that depend on the data to work: Allowing a user to enter an incorrectly formatted email address, either on purpose or by accident, means that we won’t be able to contact that user later. Allowing a user to sign up for an account with a username that is already in use could cause numerous errors down the line. Making sure we collect all the data we need and checking that the data are formatted correctly can save a web application and its users a lot of trouble.
>
> We want to keep our site secure: Unprotected data leaves entry points for malicious actors to hurt our application or our users. Allowing a user to submit a non-secure password means that their account will not be protected. Unprotected forms can also allow bits of code to be injected into our servers. This can potentially leave our users’ sensitive information exposed. The malicious actor could even gain control of our site or corrupt our existing data!

## Regular Expressions

We’re going to be using `regex` to be performing a lot of this validation because we can use to to ensure valid expressions without having to do a bunch of `if` statements and whatnot.
#home/fullstack
