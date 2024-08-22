const team = {
  _players: [
    {
      firstName: "Steve",
      lastName: "Martin",
      age: 82,
    },
    {
      firstName: "John",
      lastName: "Wayne",
      age: 72,
    },
    {
      firstName: "Tom",
      lastName: "Hanks",
      age: 62,
    },
  ],
  _games: [
    {
      opponent: "Broncos",
      teamPoints: 42,
      opponentPoints: 27,
    },
    {
      opponent: "Raiders",
      teamPoints: 35,
      opponentPoints: 21,
    },
    {
      opponent: "Chiefs",
      teamPoints: 28,
      opponentPoints: 14,
    },
  ],
  get players() {
    return this._players;
  },
  get games() {
    return this._games;
  },
  addPlayer(newFirstName, newLastName, newAge) {
    const newPlayer = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge,
    };
    this._players.push(newPlayer);
  },
  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    const newGame = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints,
    };
    this._games.push(newGame);
  },
};

team.addPlayer("Bugs", "Bunny", 76);
console.log(team.players);

team.addGame("Titans", 100, 98);
console.log(team.games);
