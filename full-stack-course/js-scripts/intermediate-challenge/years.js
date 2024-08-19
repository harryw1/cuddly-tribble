const sortYears = (years) => {
  const sortedYears = years.sort((a, b) => b - a);
  return sortedYears;
};

// Test case 1: Sorting an array of years in descending order
const years1 = [2000, 1990, 2023, 1985, 2010];
console.log(sortYears(years1)); // Expected output: [2023, 2010, 2000, 1990, 1985]

// Test case 2: Sorting an array with duplicate years
const years2 = [2005, 2010, 2000, 2010, 1995, 2005];
console.log(sortYears(years2)); // Expected output: [2010, 2010, 2005, 2005, 2000, 1995]

// Test case 3: Sorting an empty array
const years3 = [];
console.log(sortYears(years3)); // Expected output: []
