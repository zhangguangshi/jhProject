		var stat1 = false;
		var stat2 = false;
		var stat3 = false;
$(function(){
	$('#phone').blur(function(){
		if($.trim($('#phone').val()).length === 0) 
		{
			$('.msgl1').html("&nbsp;&nbsp;<font color='red'>手机号码不能为空</font>");
			stat1 =false;
		}else{
			var tel = $("#phone").val(); //获取手机号
            var telReg = !!tel.match(/^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/);
            //如果手机号码不能通过验证
            if(telReg == false){
                $('.msgl1').html('&nbsp;&nbsp;<font color=red style="width:20px;">手机格式有误!</font>');
                stat1 = false;
            }else{
            	$.post(forget_ck_phone,{phone:$("#phone").val()},function(data){
            		if(data.status){
  $('.msgl1').html("&nbsp;&nbsp;<font color='red'>该手机尚未注册</font>");
            			stat1 =false;
            		}else{
            			$('.msgl1').html("&nbsp;&nbsp;<font color='green'>√</font>");
						stat1 =true;
            		}
            	});
				
            }
        }
			
	});

	$("input[name='verify']").blur(function(){
		var verify = $("input[name='verify']").val();
		var web_url = code_url;
		$.post(web_url,{verify:verify},function(data){
			if(data.status)
			{
				$('.msgl3').html("&nbsp;&nbsp;<font color='green'>√</font>");
				$("#btn").attr('disabled',false);
				$("#btn").css('background','#78b335');
				stat3 =true;
			}else{
				if(verify.length == 0){
					$('.msgl3').html("&nbsp;&nbsp;<font color='red'>请填写验证码</font>");
					$("#btn").attr('disabled',true);
					stat3 =false;
						
				}else{
					$('.msgl3').html("&nbsp;&nbsp;<font color='red'>验证码错误</font>");
						$("#btn").attr('disabled',true);
						stat3 =false;

				}
				
				
				
			}
		});
	});

	$("#reg_code").focus(function(){
		var myphone = $("#phone").val();
		var verify = $("#verify").val();
		if(myphone =='' && verify == ''){
			$("#btn").attr('disabled',true);
		}
	})
    $('#reg_code').blur(function(){
        if($.trim($('#reg_code').val()).length === 0)
        {
            $('.msg4').html("&nbsp;&nbsp;<font color='red'>请填写短信验证码</font>");
            stat2 = false;
        }else{
             $.post(forget_check_code,{code:$('#reg_code').val()},function(data){
            if(data.status)
            {
              $('.msg4').html("&nbsp;&nbsp;<font color='green'>√</font>");
              stat2 =true;
            }else{
               $('.msg4').html("&nbsp;&nbsp;<font color='red'>验证码错误</font>");
                stat2 =false;
            }
          });
        }
    });
		
		
	$('#submit').click(function(){
		if(stat1 ==true && stat2 ==true && stat3 ==true)
		{
			var login = login_url;
			$('#submit').html('登录中..');
			$.post(login,{phone:$('#phone').val(),password:$('#password').val(),verify:$('#verify').val(),icode:$("#reg_code").val()},function(data){
				if(data.status)
				{
					
					window.location.href= user_url;
				}else{
					alert(data.info);
					$('#submit').html('登录');
				}
			});
		}else{
			$('#submit').html('登录');
		}
				//$("input[name='phone'],.msg").html("&nbsp;&nbsp;<font color='red'>X</font>");
				
				//$('.msg').html("&nbsp;&nbsp;<font color='green'>√</font>");
				//$('#submit').html('登录中..');
		
	});

	$("input[name='verify']").blur(function(){
		var verify = $("input[name='verify']").val();
		var web_url = code_url;
		$.post(web_url,{verify:verify},function(data){
			if(data.status)
			{
				$('.msg3').html("&nbsp;&nbsp;<font color='green'>√</font>");
				window.stat3 = true;
				
			}else{
				$('.msg3').html("&nbsp;&nbsp;<font color='red'>X</font>");
			}
		});
	});

	$(".layer1").keydown(function() {
		if(window.event.keyCode == 13)
		{

			var login = login_url;
			$('#submit').html('登录中..');
			$.post(login,{phone:$('#phone').val(),password:$('#password').val(),verify:$('#verify').val(),icode:$("#reg_code").val()},function(data){
				if(data.status)
				{
					
					window.location.href= user_url;
				}else{
					alert(data.info);
					$('#submit').html('登录');
				}
			});
		
		}
	});
});