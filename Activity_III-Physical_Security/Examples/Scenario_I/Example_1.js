$('#loginForm').submit((event) => {
    event.preventDefault();
    var u = $('#username').val();
    var p = $('input[type=password]').val();
    alert('Username is '+u+' Password is '+p);
});

