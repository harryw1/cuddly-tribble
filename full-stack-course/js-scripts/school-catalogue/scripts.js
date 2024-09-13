class School {
  constructor(name, level, numberOfStudents) {
    this._name = name;
    if (level === "primary" || level === "middle" || level === "high") {
      this._level = level;
    } else {
      console.log("Invalid input: level must be primary, middle, or high.");
    }
    this._numberOfStudents = numberOfStudents;
  }
  get name() {
    return this._name;
  }
  get level() {
    return this._level;
  }
  get numberOfStudents() {
    return this._numberOfStudents;
  }
  set numberOfStudents(newNumberOfStudents) {
    if (typeof newNumberOfStudents === "number") {
      this._numberOfStudents = newNumberOfStudents;
    } else {
      console.log("Invalid input: numberOfStudents must be set to a Number.");
    }
  }
  quickFacts() {
    return `${this.name} educates ${this.numberOfStudents} students at the ${this.level} school level.`;
  }
  static pickSubstituteTeacher(substituteTeachers) {
    const randomIndex = Math.floor(Math.random() * substituteTeachers.length);
    return substituteTeachers[randomIndex];
  }
}

class PrimarySchool extends School {
  constructor(name, numberOfStudents, pickupPolicy, level = "primary") {
    super(name, level, numberOfStudents);
    this._pickupPolicy = pickupPolicy;
  }
  get pickupPolicy() {
    return this._pickupPolicy;
  }
}

class MiddleSchool extends School {
  constructor(name, numberOfStudents, level = "middle") {
    super(name, level, numberOfStudents);
  }
}

class HighSchool extends School {
  constructor(name, numberOfStudents, sportsTeams, level = "high") {
    super(name, level, numberOfStudents);
    this._sportsTeams = sportsTeams;
  }
  get sportsTeams() {
    return this._sportsTeams;
  }
}

const lorraineHansbury = new PrimarySchool(
  "Lorraine Hansbury",
  514,
  "Students must be picked up by a parent, guardian, or a family member over the age of 13.",
);
console.log(lorraineHansbury.quickFacts());
const substituteTeachers = [
  "Jamal Crawford",
  "Lou Williams",
  "J. R. Smith",
  "James Harden",
  "Jason Terry",
  "Manu Ginobli",
];
console.log(School.pickSubstituteTeacher(substituteTeachers));

const alSmith = new HighSchool("Al E. Smith", 415, [
  "Baseball",
  "Basketball",
  "Volleyball",
  "Track and Field",
]);

for (let r in alSmith.sportsTeams) {
  console.log(alSmith.sportsTeams[r]);
}
