const justCoolStuff = (arr1, arr2) => {
  return arr1.filter((item) => arr2.includes(item));
};

// Test case 1: Basic functionality
const coolStuff = [
  "gameboys",
  "skateboards",
  "backwards hats",
  "fruit-by-the-foot",
  "pogs",
  "my room",
  "temporary tattoos",
];
const myStuff = [
  "rules",
  "fruit-by-the-foot",
  "wedgies",
  "sweaters",
  "skateboards",
  "family-night",
  "my room",
  "braces",
  "the information superhighway",
];
console.log(justCoolStuff(myStuff, coolStuff));
// Expected output: ['fruit-by-the-foot', 'skateboards', 'my room']

// Test case 2: Empty arrays
console.log(justCoolStuff([], []));
// Expected output: []

// Test case 3: No common elements
const arr1 = ["a", "b", "c"];
const arr2 = ["d", "e", "f"];
console.log(justCoolStuff(arr1, arr2));
// Expected output: []

// Test case 4: All elements in common
const arr3 = [1, 2, 3];
const arr4 = [1, 2, 3];
console.log(justCoolStuff(arr3, arr4));
// Expected output: [1, 2, 3]

// Test case 5: Mixed data types
const arr5 = [1, "two", true, null, { key: "value" }];
const arr6 = ["one", true, null, { key: "value" }, 5];
console.log(justCoolStuff(arr5, arr6));
// Expected output: [true, null, { key: 'value' }]
