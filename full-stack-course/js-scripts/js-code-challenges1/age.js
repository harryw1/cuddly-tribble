const howOld = (age, year) => {
  const currentYear = 2024;
  const yearDifference = year - currentYear;
  const newAge = age + yearDifference;
  if (newAge < 0) {
    return `The year ${year} was ${-newAge} years before you were born`;
  } else if (newAge > age) {
    return `You will be ${newAge} in the year ${year}`;
  } else {
    return `You were ${newAge} in the year ${year}`;
  }
};

console.log(howOld(25, 2024)); // You will be 25 in the year 2024
console.log(howOld(25, 1999)); // You were 0 in the year 1999
console.log(howOld(25, 2050)); // You will be 51 in the year 2050
console.log(howOld(25, 1980)); // The year 1980 was 5 years before you were born
