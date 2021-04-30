$(document).ready(function() {

    $('.updateButton').on('click', function() {

        req = $.ajax({
            url : '/update',
            type : 'POST',
        });
        req.done(function(data) {
            $('#table').html(aj.responseText);
        });
    });
});
