

$(function() {
    // Check if logged in, or do any other GET request similarly to this
    $.ajax({
        url: 'http://127.0.0.1:8000/users',
        dataType: 'application/json',
        contentType: 'application/json',
        beforeSend: function(xhr) {
            xhr.setRequestHeader('Authorization', 'Token: ' + Cookie.get('token'))
        }
    }).done(function(data) {
        console.log(data);
    }).fail(function(xhr, status) {
        // TODO: Handle error by showing the "login" div
        console.log(xhr.status)
        console.log(xhr.responseText);
        console.log(status);
    });

    // Login
    $.ajax({
        url: 'http://127.0.0.1:8000/login',
        method: 'POST',
        dataType: 'application/json',
        contentType: 'application/json'
        data: {username: $('#login-username').val(), password: $('#login-password').val()}
    }).done(function(data) {
        console.log(data);

        // Save token to a cookie so user is logged in for future requests
        Cookie.set('token', data.token);
    }).fail(function(xhr, status) {
        // TODO: Handle error however you want
        console.log(xhr.status)
        console.log(xhr.responseText);
        console.log(status);
    });
});
