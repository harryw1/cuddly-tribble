function getSleepHours(day) {
    day = day.toLowerCase();
    switch (day) {
        case "monday":
            return 9;
        case "tuesday":
            return 7;
        case "wednesday":
            return 8;
        case "thursday":
            return 5;
        case "friday":
        case "saturday":
            return 10;
        case "sunday":
            return 7;
        default:
            return `I don't know how long you slept.`;
    }
}

const getActualSleepHours = () => {
    let sleepHours = 0;
    sleepHours += getSleepHours('monday');
    sleepHours += getSleepHours('tuesday');
    sleepHours += getSleepHours('wednesday');
    sleepHours += getSleepHours('thursday');
    sleepHours += getSleepHours('friday');
    sleepHours += getSleepHours('saturday');
    sleepHours += getSleepHours('sunday');
    return sleepHours;
}

const getIdealSleepHours = () => {
    const idealHours = 8;
    return idealHours * 7;
}

const calculateSleepDebt = () => {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours();
    const sleepDebt = Math.abs(actualSleepHours - idealSleepHours);
    if (actualSleepHours === idealSleepHours) {
        console.log(`You got the perfect amount of sleep!`);
    } else if (actualSleepHours > idealSleepHours) {
        console.log(`You got more sleep than needed!`);
    } else {
        console.log(`You need to get ${sleepDebt} hours of sleep.`);
    }
}

calculateSleepDebt();
