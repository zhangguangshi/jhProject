// JavaScript Document

function inputTipText(){      
$("input[class*=grayTips]") //所有样式名中含有grayTips的input     
.each(function(){     
   var oldVal=$(this).val();   //默认的提示性文本     
   $(this)     
   .css({"color":"#999"})  //灰色     
   .focus(function(){     
    if($(this).val()!=oldVal){$(this).css({"color":"#1c1714"})}else{$(this).val("").css({"color":"#999"})}     
   })     
   .blur(function(){     
    if($(this).val()==""){$(this).val(oldVal).css({"color":"#999"})}     
   })     
   .keydown(function(){$(this).css({"color":"#1c1714"})})     
       
})     
}     
    
$(function(){     
inputTipText();  //直接调用就OK了     
}) 


function bf(e,f){
	$(".sec-p").removeClass();
	$(e).addClass(f);
	}