const toEmoticon = (string) => {
  switch (string.toLowerCase()) {
    case "shrug":
      return '|_{"}_|';
    case "smiley face":
      return ":)";
    case "frowny face":
      return ":(";
    case "winky face":
      return ";)";
    case "heart":
      return "<3";
    case "kiss":
      return ":*";
    default:
      return "|_(* ~ *)_|";
  }
};

console.log(toEmoticon("shrug")); // Should print '|_{"}_|'
console.log(toEmoticon("smiley face")); // Should print ':)'
console.log(toEmoticon("frowny face")); // Should print ':('
console.log(toEmoticon("winky face")); // Should print ';)'
console.log(toEmoticon("unknown")); // Should print '|_(* ~ *)_|'
