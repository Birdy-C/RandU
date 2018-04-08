window.onload = function () {
    var h1 = 110 * $('#letters-part').find("li").length;
    var sh1 = (h1 + 40).toString() + 'px';
    $('#letters-part')[0].style.height = sh1;

    for (var i = 0; i < ($('#letters-part').find("li").length); i++) {
        console.log($('#letters-part').find("li").find(".letter-state")[0].innerHTML);
        if ($('#letters-part').find("li").find(".letter-state")[0].innerHTML == '已寄到') {

            $('#letters-part').find("li")[i].style.backgroundColor = '0x000000';
        }
    }
}