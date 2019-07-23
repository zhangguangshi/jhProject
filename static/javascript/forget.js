$(function(){
    $('#btn_f').attr('disabled', true);
    $('#phone2').mouseout(function(){
        if($.trim($('#phone2').val()).length !==0 )
        {
            $.post(forget_ck_phone,{phone:$('#phone2').val()},function(data){
                if(data.status){
                    $('.msgf1').html('&nbsp;&nbsp;<font color=red>手机号码不存在</font>');
                }else{
                     $('.msgf1').html("&nbsp;&nbsp;<font color='green'>√</font>");
                }
            });
        }
    });

    //获取发送按钮
    var btn = $('#btn_f');
    var urlf = forget_sendmsg_url;
    
    //设定按钮点击事件
    btn.click(function(){


        $.ajax({
           type: "POST",
           url: urlf,
           cache:false,
           data: {phone:$('#phone2').val(),code:$('#forget_verify').val()},
           success: function(data){
             console.log(data);
           }
        });
         btn.attr('disabled', true);
         start_f(btn, 60);
    });
   
});

function start_f(node, count)
{
    if(count > 0 )
    {
        node.html(count--);
        var _this = this;
        setTimeout(function(){
            _this.start_f(node, count);
        },1000);
    }
    else
    {
        node.prop('disabled', false);
        node.html('再次发送');
        count = 60;
    }
}