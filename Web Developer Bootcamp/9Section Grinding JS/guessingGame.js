function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}
var target = getRandomIntInclusive(1,10);
var guess = prompt("Guess a number!");
while(guess != target)
{
    if (guess > target )
    {
        guess = prompt("Too high. Try again.");
    }
    if (guess < target )
    {
        guess = prompt("Too low. Try again.");
    }
}
alert("You guessed it!!!!!!");
