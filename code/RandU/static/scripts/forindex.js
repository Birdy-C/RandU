//：Only For Random You

$('#shift-pic1').click(function () {
    $('#our-jumb-lead')[0].innerHTML = "随机撒点式寄信|收信|交友|相亲平台";
    $('#our-jumb')[0].style.backgroundImage = "url('../static/image/SendBack.jpg')";

});

$('#shift-pic2').click(function () {
    $('#our-jumb-lead')[0].innerHTML = "Only For Random You";
    $('#our-jumb')[0].style.backgroundImage = "url('../static/image/ReceiveBack.jpg')";

});

/*$('#login-button').click(function (event) {
    event.preventDefault();
    //$('form').fadeOut(500);
    $('.wrapper').addClass('form-success');
});*/

$('#sign-button').click(function () {
    window.location.href = '/register';
});