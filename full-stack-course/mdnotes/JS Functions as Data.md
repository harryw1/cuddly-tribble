# JS Functions as Data

From Codeacademy:

> We’re also going to learn about a way to add another level of abstraction to our programming: _higher-order functions_. _Higher-order functions_ are functions that accept other functions as arguments and/or return functions as output. This enables us to build abstractions on other abstractions, just like “We hosted a birthday party” is an abstraction that may build on the abstraction “We made a cake.”

## Functions as Data

We’re coming back to the idea of functions being passed by reference. The example they make here is about a really long function name and then storing that function in a much smaller constant’s name.

```javascript
const announceThatIAmDoingImportantWork = () => {
    console.log("I'm doing very important work!");
};

const busy = announceThatIAmDoingImportantWork;

busy(); // A much more convenient function call
```

Again, we’re passing by reference so `busy` and `announceThatIAmDoingImportantWork` point to the same address in memory.

## Functions as Parameters

We can also pass functions as parameters to other high-order functions:

#home/fullstack
