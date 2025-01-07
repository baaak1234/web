// $(document).ready(function(){
//     $('#my-btn').on('click', function(){
//         if ($('#txt').html() == "hello"){
//             $('#txt').html('안녕');
//         } else {
//             $('#txt').html('hello');
//         }
//     });
// });





$(document).ready(function(){
    $('#my-btn').on('click', function(){
        var $txt = $('#txt');
        
        if ($txt.css('color') === 'rgb(0, 0, 255)' || $txt.css('color') === 'blue'){
            $txt.css('color', 'black');
        } else {
            $txt.css('color', 'blue');
        }
    });
});


$(document).ready(function(){
    $('#my-btn').on('click', function(){
        var inputValue = $('#inp').val();
        $('#txt').html(inputValue);
    });
});