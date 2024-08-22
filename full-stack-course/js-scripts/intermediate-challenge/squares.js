const squareNums = (arr) => {
  const squaredNumbers = arr.map((num) => num * num);
  return squaredNumbers;
};

// Test case 1: Squaring positive numbers
console.log(squareNums([1, 2, 3])); // Expected output: [1, 4, 9]

// Test case 2: Squaring negative numbers
console.log(squareNums([-1, -2, -3])); // Expected output: [1, 4, 9]

// Test case 3: Squaring zero
console.log(squareNums([0])); // Expected output: [0]

// Test case 4: Squaring mixed numbers
console.log(squareNums([-2, 0, 2])); // Expected output: [4, 0, 4]

// Test case 5: Empty array
console.log(squareNums([])); // Expected output: []

// Test case 6: Squaring decimal numbers
console.log(squareNums([0.5, 1.5, 2.5])); // Expected output: [0.25, 2.25, 6.25]
