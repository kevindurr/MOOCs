var answer = prompt("Are we there yet?");
while(answer !== "yes" && answer !== "yeah")
{
    if (answer.includes('yes'))
    {
        break;
    }
    answer = prompt("Are we there yet?");
}
alert("Yay, we finally made it");
