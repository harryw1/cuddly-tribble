const getUserChoice = (userInput) => {
    userInput = userInput.toLowerCase();
    if (
        userInput === "rock" ||
        userInput === "paper" ||
        userInput === "scissors" ||
        userInput === "bomb"
    ) {
        return userInput;
    } else {
        console.log("Invalid input");
    }
};

const getComputerChoice = () => {
    const choice = Math.floor(Math.random() * 3);
    if (choice === 0) {
        return "rock";
    } else if (choice === 1) {
        return "paper";
    } else if (choice === 2) {
        return "scissors";
    }
};

const determineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice) {
        return "It's a tie!";
    } else if (userChoice === "bomb") {
        return "Kaboom! User wins!";
    } else if (userChoice === "rock") {
        if (computerChoice === "paper") {
            return "Computer wins!";
        } else {
            return "You win!";
        }
    } else if (userChoice === "paper") {
        if (computerChoice === "scissors") {
            return "Computer wins!";
        } else {
            return "You win!";
        }
    } else if (userChoice === "scissors") {
        if (computerChoice === "rock") {
            return "Computer wins!";
        } else {
            return "You win!";
        }
    } else {
        return "Invalid input";
    }
};

const userChoice = getUserChoice("bomb");
const computerChoice = getComputerChoice();
const winner = determineWinner(userChoice, computerChoice);
console.log(winner);
