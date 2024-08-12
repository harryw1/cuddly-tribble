const finalGrade = (a, b, c) => {
  if (a < 0 || a > 100 || b < 0 || b > 100 || c < 0 || c > 100) {
    return "You have entered an invalid grade.";
  }
  let avg = Math.average(a, b, c); // Codeacademy doesn't have Math.average
  if (avg < 60) {
    return "F";
  } else if (avg < 70) {
    return "D";
  } else if (avg < 80) {
    return "C";
  } else if (avg < 90) {
    return "B";
  } else {
    return "A";
  }
};
