//鼠标单击文本框时
function formTip(obj, tipcolor) {
    var tipcolor = arguments[1] ? tipcolor : '#ACA899';//默认提示文字颜色
    var tipVal = obj.defaultValue;//提示文字就是默认的value值

    obj.style.color = tipcolor;
    obj.onfocus = function () {
        if (obj.value == tipVal) {
            obj.value = '';
            obj.style.color = '';//添加的提示颜色
        }
    }

    obj.onblur = function () {
        if (obj.value == '') {
            obj.value = tipVal;
            obj.style.color = tipcolor;
        }
    }

}

window.onload = function () {
    formTip(document.getElementById("user-state-text"));

    //限制文本框字数
    $("#user-state-text").on("input propertychange", function () {
        var $this = $(this),
            _val = $this.val(),
            count = "";
        if (_val.length > 100) {
            $this.val(_val.substring(0, 100));
        }
        count = 100 - $this.val().length;
        $("#text-count").text(count);
    });
}