var input = prompt("What would you like to do?");
var todos = [];
while (input !== "quit"){

    if (input === "list"){
        todos.forEach(function(todo, i){
            console.log(i + ": " + todo);
        });
    }
    else if(input === "new"){
        var newTodo = prompt("Enter new todo");
        todos.push(newTodo);
    }
    else if(input === "delete"){
        var index = prompt("Enter an index to delete");
        todos.splice(index, 1);
    }
    input = prompt("What would you like to do?");
}
console.log("OK, YOU QUIT THE APP");