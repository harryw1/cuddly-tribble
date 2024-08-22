const dogFactory = (name, breed, weight) => {
  if (
    typeof name === "string" &&
    typeof breed === "string" &&
    typeof weight === "number"
  ) {
    return {
      _name: name,
      _breed: breed,
      _weight: weight,
      get name() {
        return this._name;
      },
      set name(newName) {
        if (typeof newName === "string") {
          this._name = newName;
        } else {
          console.log("Invalid input. Name must be a string.");
        }
      },
      get breed() {
        return this._breed;
      },
      set breed(newBreed) {
        if (typeof newBreed === "string") {
          this._breed = newBreed;
        } else {
          console.log("Invalid input. Breed must be a string.");
        }
      },
      get weight() {
        return this._weight;
      },
      set weight(newWeight) {
        if (typeof newWeight === "number") {
          this._weight = newWeight;
        } else {
          console.log("Invalid input. Weight must be a number.");
        }
      },
      bark() {
        return "ruff! ruff!";
      },
      eatTooManyTreats() {
        this._weight++;
      },
    };
  }
};

const dog1 = dogFactory("Joe", "Pug", 27);

console.log(dog1.name); // Expected output: "Joe"
console.log(dog1.breed); // Expected output: "Pug"
console.log(dog1.weight); // Expected output: 27

dog1.name = "Charlie";
console.log(dog1.name); // Expected output: "Charlie"

dog1.breed = "Bulldog";
console.log(dog1.breed); // Expected output: "Bulldog"

dog1.weight = 30;
console.log(dog1.weight); // Expected output: 30

console.log(dog1.bark()); // Expected output: "ruff! ruff!"

dog1.eatTooManyTreats();
console.log(dog1.weight); // Expected output: 31

dog1.name = 123; // Expected output: "Invalid input. Name must be a string."
dog1.breed = true; // Expected output: "Invalid input. Breed must be a string."
dog1.weight = "heavy"; // Expected output: "Invalid input. Weight must be a number."
