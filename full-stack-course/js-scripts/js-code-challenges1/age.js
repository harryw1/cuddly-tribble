/**
 * Calculates a person's age in a given year and provides a descriptive message.
 *
 * @param {number} age - The current age of the person.
 * @param {number} year - The year for which to calculate the age.
 * @returns {string} A message describing the person's age situation for the given year.
 *
 * @description
 * This function takes a person's current age and a target year, then calculates
 * and describes the person's age situation for that year. It handles three scenarios:
 * 1. If the calculated age is negative (i.e., before the person was born)
 * 2. If the year is in the future
 * 3. If the year is in the past but after the person was born
 *
 * The function assumes the current year is 2024.
 *
 * @example
 * howOld(25, 2024) // Returns: "You will be 25 in the year 2024"
 * howOld(25, 1999) // Returns: "You were 0 in the year 1999"
 * howOld(25, 2050) // Returns: "You will be 51 in the year 2050"
 * howOld(25, 1980) // Returns: "The year 1980 was 5 years before you were born"
 */

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
