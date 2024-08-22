const speciesArray = [
  { speciesName: "shark", numTeeth: 50 },
  { speciesName: "dog", numTeeth: 42 },
  { speciesName: "alligator", numTeeth: 80 },
  { speciesName: "human", numTeeth: 32 },
];

const sortSpeciesByTeeth = (speciesArray) => {
  return speciesArray.sort((a, b) => a.numTeeth - b.numTeeth);
};

console.log(sortSpeciesByTeeth(speciesArray));
