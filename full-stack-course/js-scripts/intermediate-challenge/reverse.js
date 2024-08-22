const reverseArray = (array) => {
  let reversedArray = [];
  for (let i = array.length - 1; i >= 0; i--) {
    reversedArray.push(array[i]);
  }
  return reversedArray;
};

const sentence = ["sense.", "make", "all", "will", "This"];
console.log(reverseArray(sentence));
