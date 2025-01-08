$(document).ready(function(){
var todo_id = $('#todo-id').val();

    $.ajax({
        url : 'https://jsonplaceholder.typicode.com/todos/'+todo_id,
        type : 'GET',
        data : {},
        success : function(todo){
            console.log(todo);
            $('#id').text(todo.id);
            $('#userid').text(todo.userId);
            $('#title').text(todo.title);
            $('#completed').text(todo.completed ? '성공' : '실패');
        },
        error : function(error){
            console.log(error);
        }
    });
});