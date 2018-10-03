var todos = [];
window.setTimeout(function() {
    // put all of your JS code from the lecture here
    var select;
    while (select != "quit")
    {
        select = prompt("What would you like to do?");
        if (select == "new")
        {
            var input = prompt("Enter a new todo");
            todos.push(input);
        }
        else if (select == "list")
        {
            console.log(todos);
        }
    }
    

}, 500);