# JS Objects

Now we're getting back to what I remember from CSII in college. Let's start by recapping
objects in general.

- Objects are non-primitive data types
- Objects are passed by reference
  - Passing by reference means we're point to
    a location in memory
  - This means that objects are, essentially,
    always mutable
- Objects can store any data, for example:

```javascript
*// Code snippet*
const person = {
    height: "6 feet",
    weight: "160 pounds",
    hairColor: "brown",
    eyeColor: "blue",
    bloodType: "O+",
};
```

This above code example abstracts the 'person' data structure into a set of
key:value pairs and can be accessed with 'dot' notation or 'bracket' notation.

```javascript
console.*log*(person.height);
console.*log*(person.[hairColor]);
```

## 'this' Keyword

To access properties within the scope of an object, we need to use the 'this' keyword
in any function calls or other references to properties within the same object.

```javascript
const person = {
    height: "6 feet",
    weight: "160 pounds",
    hairColor: "brown",
    eyeColor: "blue",
    bloodType: "O+",
    greeting: "hey!",
    *hello*() {
        console.*log*(this.greeting);
    },
};
person.*hello*();
```

Another example:

```javascript
const robot = {
    model: "1E78V2",
    energyLevel: 100,
    *provideInfo*() {
        return `I am ${this.model} and my current energy level is ${this.energyLevel}`;
    },
};

console.*log*(robot.*provideInfo*());
```

## Arrow Function and 'this'

Arrow functions mean that we don't need to reference 'this' in a function call within the scope
of our object. The below is an example of what happens when we try to call this on an arrow function:

```javascript
const goat = {
    dietType: "herbivore",
    *makeSound*() {
        console.*log*("baaa");
    },
    *diet*: () => {
        console.*log*(this.dietType);
    },
};

goat.*diet*(); *// Prints undefined*
```

If we want to fix this code:

```javascript
const goat = {
    dietType: "herbivore",
    *makeSound*() {
        console.*log*("baaa");
    },
    *diet*() {
        console.*log*(this.dietType);
    },
};

goat.*diet*();
```

## Privacy

JS doesn't have any inherent way of creating privacy. JS developers use
the prepending of an underscore, "\_xyz", to indicate to other people
that a variable or some other data structure is not meant to be interacted
with directly.

## Getters and Setters

Getters are functions within an object that can return values and beyond.

```javascript
const person = {
    _firstName: "John",
    _lastName: "Doe",
    get *fullName*() {
        if (this._firstName && this._lastName) {
            return `${this._firstName} ${this._lastName}`;
        } else {
            return "Missing a first name or a last name.";
        }
    },
};

*// To call the getter method:*
person.fullName; *// 'John Doe'*
```

Another example of a 'getter' function:

```javascript
const robot = {
    _model: "1E78V2",
    _energyLevel: 100,
    get *energyLevel*() {
        if (typeof this._energyLevel === "number") {
            return `My current energy level is ${this._energyLevel}`;
        } else {
            return "System malfunction: cannot retrieve energy level";
        }
    },
};

robot.energyLevel;

console.*log*(robot.energyLevel);
```

Setter functions are an appropriate way to handle modifying properties within objects
and handle types so that we don't end up with anything funky.

## Factory Function

Similar to C++, we can create templates for returning different objects with the same structures. Below is an example
of a factory function for making robots that take in two paramters and returns a new object that we can store in
a variable.

```javascript
const *robotFactory* = (*model*, *mobile*) => {
    return {
        model: model, *// or just model,*
        mobile: mobile, *// or just mobile,*
        *beep*() {
            console.*log*("Beep Boop");
        },
    };
};

const tinCan = *robotFactory*("P-500", true);

tinCan.*beep*();
```

## Destructured Assignment

Some shorthand to access properties and store them in variables outside of the object.

```javascript
const robot = {
    model: "1E78V2",
    energyLevel: 100,
    functionality: {
        *beep*() {
            console.*log*("Beep Boop");
        },
        *fireLaser*() {
            console.*log*("Pew Pew");
        },
    },
};

const { functionality } = robot;
functionality.*beep*();
```

## Object Functions

Some built in functions for objects that are nice to know:

```javascript
const robot = {
    model: "SAL-1000",
    mobile: true,
    sentient: false,
    armor: "Steel-plated",
    energyLevel: 75,
};

*// What is missing in the following method call?*
const robotKeys = Object.*keys*(robot);

console.*log*(robotKeys);

*// Declare robotEntries below this line:*
const robotEntries = Object.*entries*(robot);
console.*log*(robotEntries);

*// Declare newRobot below this line:*
const newRobot = Object.*assign*(
    { laserBlaster: true, voiceRecognition: true },
    robot
);

console.*log*(newRobot);
```

## Final Practice

### Example 1

```javascript
const menu = {
  _meal: "",
  _price: 0,
  set meal(mealToCheck) {
    if (typeof mealToCheck === "string") {
      this._meal = mealToCheck;
    }
  },
  set price(priceToCheck) {
    if (typeof priceToCheck === "number") {
      this._price = priceToCheck;
    }
  },
  get todaysSpecial() {
    if (this._meal && this._price) {
      return `Today's special is ${this._meal} for just $${this._price}`;
    } else {
      return "Meal or price was not set correctly!";
    }
  },
};

menu.meal = "Chicken Tikka";
menu.price = 10.99;

console.log(menu.todaysSpecial); // Output: Today's special is Chicken Tikka for just $10.99
```

### Example 2

```javascript
const team = {
  _players: [
    {
      firstName: "Steve",
      lastName: "Martin",
      age: 82,
    },
    {
      firstName: "John",
      lastName: "Wayne",
      age: 72,
    },
    {
      firstName: "Tom",
      lastName: "Hanks",
      age: 62,
    },
  ],
  _games: [
    {
      opponent: "Broncos",
      teamPoints: 42,
      opponentPoints: 27,
    },
    {
      opponent: "Raiders",
      teamPoints: 35,
      opponentPoints: 21,
    },
    {
      opponent: "Chiefs",
      teamPoints: 28,
      opponentPoints: 14,
    },
  ],
  get players() {
    return this._players;
  },
  get games() {
    return this._games;
  },
  addPlayer(newFirstName, newLastName, newAge) {
    const newPlayer = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge,
    };
    this._players.push(newPlayer);
  },
  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    const newGame = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints,
    };
    this._games.push(newGame);
  },
};

team.addPlayer("Bugs", "Bunny", 76);
console.log(team.players);

team.addGame("Titans", 100, 98);
console.log(team.games);
```

#home/fullstack
