/*
  Portfolio project in JS that will create a mad-libs
  style story based on a random selection of words.
*/
const adjs = [
  "cool",
  "awesome",
  "funny",
  "crazy",
  "weird",
  "strange",
  "boring",
  "lame",
  "dumb",
  "smart",
];

const nouns = [
  "dog",
  "cat",
  "bird",
  "fish",
  "snake",
  "lizard",
  "hamster",
  "gerbil",
  "rat",
  "mouse",
];

const verbs = [
  "shopping",
  "laundry",
  "cleaning",
  "cooking",
  "paying bills",
  "mowing the lawn",
  "walking the dog",
  "picking up dry cleaning",
  "washing the car",
  "taking out the trash",
];

const message = (adjs, nouns, verbs) => {
  const adj = adjs[Math.floor(Math.random() * adjs.length)];
  const noun = nouns[Math.floor(Math.random() * nouns.length)];
  const verb = verbs[Math.floor(Math.random() * verbs.length)];

  return `Help! My ${adj} ${noun} is ${verb} and I don't know what to do!`;
};

console.log(message(adjs, nouns, verbs));
