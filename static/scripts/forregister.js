//显示上传的图片
$('#put-on-head-button').change(function () {

    var f = document.getElementById('put-on-head-label').files[0];

    var src = window.URL.createObjectURL(f);

    //document.getElementById('.put-on-head').src = src;
    document.getElementById('uhead').src = src;

});

$('.blades').hover(function () {
    this.style.rotate++;
});

$('#aplyer_nan_input').click(function () {
    if ($('#aplyer_nan_input').prop('checked')) {

        if (document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHead.jpg' || document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHeadnv.jpg') {/////////////////////aaaaaaaaaaaaaaaaaaaaa改成服务器地址吧
            document.getElementById('uhead').src = 'http://localhost:5000/static/image/defaultHeadnan.jpg';
        }
        else {
            console.log(document.getElementById('uhead').src);
        }

    }
});

$('#aplyer_nv_input').click(function () {
    if ($('#aplyer_nv_input').prop('checked')) {

        if (document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHead.jpg' || document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHeadnan.jpg') {/////////////////////aaaaaaaaaaaaaaaaaaaaa改成服务器地址吧
            document.getElementById('uhead').src = 'http://localhost:5000/static/image/defaultHeadnv.jpg';
        }
        else {
            console.log(document.getElementById('uhead').src);
        }

    }
});

$('#aplyer_non_input').click(function () {
    if ($('#aplyer_non_input').prop('checked')) {

        if (document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHeadnv.jpg' || document.getElementById('uhead').src == 'http://localhost:5000/static/image/defaultHeadnan.jpg') {/////////////////////aaaaaaaaaaaaaaaaaaaaa改成服务器地址吧
            document.getElementById('uhead').src = 'http://localhost:5000/static/image/defaultHead.jpg';
        }
        else {
            console.log(document.getElementById('uhead').src);
        }

    }
});
