const menu = {
  _meal: "",
  _price: 0,
  set meal(mealToCheck) {
    if (typeof mealToCheck === "string") {
      this._meal = mealToCheck;
    }
  },
  set price(priceToCheck) {
    if (typeof priceToCheck === "number") {
      this._price = priceToCheck;
    }
  },
  get todaysSpecial() {
    if (this._meal && this._price) {
      return `Today's special is ${this._meal} for just $${this._price}`;
    } else {
      return "Meal or price was not set correctly!";
    }
  },
};

menu.meal = "Chicken Tikka";
menu.price = 10.99;

console.log(menu.todaysSpecial); // Output: Today's special is Chicken Tikka for just $10.99
