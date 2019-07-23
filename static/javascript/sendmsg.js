$(function(){
    //获取发送按钮
    var btn = $('#btn');
    var urls = base_url;
    
    //设定按钮点击事件
    btn.click(function(){


        $.ajax({
           type: "POST",
           url: urls,
           cache:false,
           data: {phone:$('#phone').val(),code:$("#verify").val()},
           success: function(data){
             console.log(data);
           }
        });
         btn.attr('disabled', true);
         start(btn, 60);
    });
   
});

function start(node, count)
{
    if(count > 0 )
    {
        node.html(count--);
        var _this = this;
        setTimeout(function(){
            _this.start(node, count);
        },1000);
    }
    else
    {
        node.prop('disabled', false);
        node.html('再次发送');
        node.css('background','#78b335');
        count = 60;
    }
}