
function getRandomColor() {

    return '#' +

        (function (color) {

            return (color += '0123456789abcdef'[Math.floor(Math.random() * 5)])

                && (color.length == 6) ? color : arguments.callee(color);

        })('');

}

window.onload = function () {
   
    //随机字体颜色
    for (var i = 0; i < 10; i++) {
        $('div.post-date')[i].style.color = getRandomColor();
    }
    /*这段代码试过了不能用
    $("#new-show-file").on("input", function () {

        //var imgFile = this.files[0];
        //var fr = new FileReader();
        //fr.onload = function () {
        //document.getElementById('new-show-img')[0].src = document.getElementById('new-show-file')[0].text.val();//= fr.result;
        //};
        //fr.readAsDataURL(imgFile);
    })*/



    //user-posts的高度变化
    var h = 110 * $('#user-posts').find("li").length;
    var sh = (h + 70).toString() + 'px';
    $('#user-posts')[0].style.height = sh;



}

//function e(){
//    document.write("<img src='../static/output.png?v=" + new Date().getTime() + "'>");
//}