const findMyKeys = (obj) => {
  if (obj.includes("keys")) {
    return obj.indexOf("keys");
  } else {
    return -1;
  }
};
