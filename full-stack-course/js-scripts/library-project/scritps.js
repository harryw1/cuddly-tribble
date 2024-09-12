class Media {
  constructor(title) {
    this._title = title;
    this._isCheckedOut = false;
    this._ratings = [];
  }
  get title() {
    return this._title;
  }
  get isCheckedOut() {
    return this._isCheckedOut;
  }
  get ratings() {
    return this._ratings;
  }
  set title(newTitle) {
    this._title = newTitle;
  }
  set isCheckedOut(newIsCheckedOut) {
    this._isCheckedOut = newIsCheckedOut;
  }
  getAverageRating() {
    let ratingsSum = this.ratings.reduce(
      (currentSum, rating) => currentSum + rating,
      0,
    );
    return parseFloat((ratingsSum / this.ratings.length).toFixed(2));
  }
  toggleCheckOutStatus() {
    this._isCheckedOut = !this._isCheckedOut;
  }
  addRating(rating) {
    if (Array.isArray(rating)) {
      rating.forEach((r) => this.ratings.push(this.validateRatings(r)));
    } else {
      this.ratings.push(this.validateRatings(rating));
    }
  }
  validateRatings(rating) {
    return Math.min(Math.max(rating, 1), 5);
  }
}

class Book extends Media {
  constructor(author, title, pages) {
    super(title);
    this._author = author;
    this._pages = pages;
  }
  get author() {
    return this._author;
  }
  get pages() {
    return this._pages;
  }
}

class Movie extends Media {
  constructor(director, title, runTime) {
    super(title);
    this._director = director;
    this._runTime = runTime;
  }
  get director() {
    return this._director;
  }
  get runTime() {
    return this._runTime;
  }
}

class CD extends Media {
  constructor(artist, title, songs, ratings, isCheckedOut) {
    super(title, ratings, isCheckedOut);
    this._artist = artist;
    this._songs = songs;
  }
  get artist() {
    return this._artist;
  }
  get songs() {
    return this._songs;
  }
}

const historyOfEverything = new Book(
  "Bill Bryson",
  "A Short History of Nearly Everything",
  544,
);
historyOfEverything.toggleCheckOutStatus();
console.log(historyOfEverything.isCheckedOut);
historyOfEverything.addRating([4, 5, 5]);
console.log(historyOfEverything.getAverageRating());

const speed = new Movie("Jan de Bont", "Speed", 116);
speed.toggleCheckOutStatus();
console.log(speed.isCheckedOut);
speed.addRating([1, 1, 5]);
console.log(speed.getAverageRating());

const tameImpala = new CD("Tame Impala", "Currents", 13);
tameImpala.toggleCheckOutStatus();
console.log(tameImpala.isCheckedOut);
tameImpala.addRating([5, 5, 5]);
console.log(tameImpala.getAverageRating());
