const isTheDinnerVegan = (arr) => {
  let isVegan = true;
  arr.forEach((food) => {
    if (food.source !== "plant") {
      isVegan = false;
    }
  });
  return isVegan;
};

// Test cases
const dinner = [
  { name: "hamburger", source: "meat" },
  { name: "cheese", source: "dairy" },
  { name: "ketchup", source: "plant" },
  { name: "bun", source: "plant" },
  { name: "dessert twinkies", source: "unknown" },
];

console.log(isTheDinnerVegan(dinner)); // Should return false

const veggieDinner = [
  { name: "salad", source: "plant" },
  { name: "tofu", source: "plant" },
  { name: "quinoa", source: "plant" },
  { name: "fruit", source: "plant" },
];

console.log(isTheDinnerVegan(veggieDinner)); // Should return true

const emptyDinner = [];

console.log(isTheDinnerVegan(emptyDinner)); // Should return true

const unknownDinner = [
  { name: "mystery meat", source: "unknown" },
  { name: "suspicious sauce", source: "unknown" },
];

console.log(isTheDinnerVegan(unknownDinner)); // Should return true (because it's not explicitly non-vegan)
