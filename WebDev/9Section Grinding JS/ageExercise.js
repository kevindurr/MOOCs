var age = prompt("What is your age?");

if (age < 0){    
    alert("ERROR");
}
else if (age == 21){
    alert("Happy 21st birthday!!");
}
else if (age % Math.sqrt(age) === 0){
    alert("Perfect Square!");
}
else if (age % 2 == 1){
    alert("your age is odd!");
}
else{
    alert("You're nothing special...");
}