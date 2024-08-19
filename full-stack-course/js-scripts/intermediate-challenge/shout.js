const shoutGreetings = (arr) => {
  const shoutArray = [];
  arr.forEach((greeting) => {
    shoutArray.push(greeting.toUpperCase() + "!");
  });
  return shoutArray;
};

// Test case 1: Basic test with an array of lowercase greetings
const testCase1 = ["hello", "hi", "hey"];
console.log(shoutGreetings(testCase1));
// Expected output: ['HELLO', 'HI', 'HEY']

// Test case 2: Test with an array of mixed case greetings
const testCase2 = ["Hello", "GOOD MORNING", "welcome"];
console.log(shoutGreetings(testCase2));
// Expected output: ['HELLO', 'GOOD MORNING', 'WELCOME']

// Test case 3: Test with an empty array
const testCase3 = [];
console.log(shoutGreetings(testCase3));
// Expected output: []
