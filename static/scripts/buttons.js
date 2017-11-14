//1.按钮-want_send_bt-弹出确认寄信吗对话框
var user_has_undone_task = false;
//这个var要对接数据库找到user之前有没有在寄状态的信的，这里暂时设一下false***********************************************************

$('#want_send_bt').click(function () {

    //有信件待处理，无法寄信
    if (user_has_undone_task == true) {
        alert('您寄出的信还未被对方收到 + 每次只能寄出一份喔 \n = 您现在不能寄信哦吼吼吼');
    }

    //可以发信，但是看看有没有填完整
    else {
        var tag1 = false;
        var tag2 = false;
        var val_area = '';
        var val_sex = '';
        if ($('#choose_near_rd').prop('checked')) {
            tag1 = true;
            val_area = 'choose_near_rd';//这里要统一一下怎么表示选择寄信地址的远近再修改********************************************
        }
        else if ($('#choose_mid_rd').prop('checked')){
            tag1 = true;
            val_area = 'choose_mid_rd';//这里要统一一下怎么表示选择寄信地址的远近再修改********************************************
        }
        else if ($('#choose_far_rd').prop('checked')){
            tag1 = true;
            val_area = 'choose_far_rd';//这里要统一一下怎么表示选择寄信地址的远近再修改********************************************
        }
        //这个选择地区的状态还要进入地址匹配算法然后布拉布拉*******************************************************************


        if ($('#choose_nan_rd').prop('checked')) {
            tag2 = true;
            val_sex = 'choose_nan_rd';//这里要统一一下怎么表示性别再修改********************************************
        }
        else if ($('#choose_nv_rd').prop('checked')) {
            tag2 = true;
            val_sex = 'choose_nv_rd';//这里要统一一下怎么表示性别再修改********************************************
        }
        else if ($('#choose_non_rd').prop('checked')) {
            tag2 = true;
            val_sex = 'choose_non_rd';//这里要统一一下怎么表示性别再修改********************************************
        }
        //这个选择性别的状态还要进入地址匹配算法然后布拉布拉*******************************************************************


        //填完整的，可以寄信，但是有必要确认一下想清楚了没有
        if (tag1 & tag2) {
            var check = confirm("确定要寄信吗？");
            //是的想清楚了的情况
            if (check == true) {
                //显示分配信息
                $('#match_module').append('\
            <p>\
                <label> 为您配对的对方信息</label>\
            </p >\
            <p>\
                <label>用户名</label>\
            </p>\
            <p>\
                <label>性别</label>\
            </p>\
            <p>\
                <label>地址</label>\
            </p>\
            <button type="button" id="sender_check">马上寄信</button>\
                    ');
                user_has_undone_task = true;
                //这个状态还要存到数据库*******************************************************************
            }
            //只是不小心点到的情况
            else {
                //哼不给他分配地址（啥都不做）
            }
        }

        //没填完整啊啊啊啊啊啊不给他寄
        else {
            alert("请选择完整！");
        }
        
    }
})
