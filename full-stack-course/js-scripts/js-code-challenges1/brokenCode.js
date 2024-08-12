const whatRelation = (percentSharedDNA) => {
  if (percentSharedDNA === 100) {
    return "You are likely identical twins.";
  }
  if (percentSharedDNA > 34 && percentSharedDNA <= 99) {
    return "You are likely parent and child or full siblings.";
  }
  if (percentSharedDNA >= 14 && percentSharedDNA <= 34) {
    return "You are likely grandparent and grandchild, aunt/uncle and niece/nephew, or half siblings.";
  }
  if (percentSharedDNA > 5 && percentSharedDNA <= 13) {
    return "You are likely 1st cousins.";
  }
  if (percentSharedDNA > 2 && percentSharedDNA <= 5) {
    return "You are likely 2nd cousins.";
  }
  if (percentSharedDNA > 0 && percentSharedDNA <= 2) {
    return "You are likely 3rd cousins";
  } else {
    return "You are likely not related.";
  }
};

console.log(whatRelation(34));
// Should print 'You are likely grandparent and grandchild, aunt/uncle and niece/nephew, or half siblings.'

console.log(whatRelation(3));
// Should print 'You are likely 2nd cousins.'
