
var answer = prompt("factorial");
answer = Number(answer);
var sum = 1;
while(answer > 1)
{
    sum *= answer;
    answer--;
}
alert("Factorial is: " + sum);
