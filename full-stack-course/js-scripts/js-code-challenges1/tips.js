const tipCalculator = (quality, total) => {
  switch (quality) {
    case "bad":
      return total * 0.05;
    case "ok":
      return total * 0.15;
    case "good":
      return total * 0.2;
    case "excellent":
      return total * 0.3;
    default:
      return total * 0.18;
  }
};

// Test cases
console.log(tipCalculator("bad", 100)); // Expected output: 5
console.log(tipCalculator("ok", 100)); // Expected output: 15
console.log(tipCalculator("good", 100)); // Expected output: 20
console.log(tipCalculator("excellent", 100)); // Expected output: 30
console.log(tipCalculator("average", 100)); // Expected output: 18
