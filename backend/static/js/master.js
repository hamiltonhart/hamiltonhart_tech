// var showHideCompletedTodos = document.getElementById("show-hide-completed-todos");



function showHideCompletedTodos(button) {
    var completedTodos = document.getElementById("completed-todos");
    if (completedTodos.style.display ===  'none' && button.innerHTML === "Show Completed"){
        completedTodos.style.display = 'block';
        button.innerHTML = "Hide Completed";
        localStorage.showcompleted = "block";
        localStorage.showhidebutton = "Hide Completed";
    }
    else{
        completedTodos.style.display = 'none';
        button.innerHTML = "Show Completed";
        localStorage.showcompleted = "none";
        localStorage.showhidebutton = "Show Completed";
    }
}

function getLocalStorageCompletedTodos(){
    var completedTodosDiv = document.getElementById("completed-todos");
    var completedTodosButton = document.getElementById("show-hide-completed-todos");
    if (localStorage.getItem("showcompleted") && localStorage.getItem("showhidebutton")){
        document.getElementById("completed-todos").style.display = localStorage.getItem("showcompleted");
        document.getElementById("show-hide-completed-todos").innerHTML = localStorage.getItem("showhidebutton");
        console.log("Get local storage.")
    }
    else{
        console.log("No local storage")
    }
    
}

getLocalStorageCompletedTodos()
