function startMove(obj,json,fn){
    clearInterval(obj.timer);
    obj.timer = setInterval(function(){
        var flag = true;//假设所有属性都达到目标值
        for(var attr in json){
            var iTarget = json[attr];
            if(attr=="opacity"){
                var iCur = parseInt(getStyle(obj,attr)*100);   
            }else{
                var iCur = parseInt(getStyle(obj,attr));
            }
            
            var iSpeed = (iTarget-iCur)/7;
            iSpeed = iSpeed>0 ? Math.ceil(iSpeed) : Math.floor(iSpeed);
            if(attr=="opacity"){
                oBox.style.opacity = (iCur + iSpeed)/100;
                oBox.style.filter="alpha(opacity="+(iCur + iSpeed)+")";       
            }else{
                obj.style[attr] = iCur + iSpeed +"px";
            }
            //必须所有属性都达到目标值才清除定时器
            if(iCur!=iTarget){
                flag = false;
                }
            }
            if(flag){
                clearInterval(obj.timer);
                if(fn){
                    fn()
                }
            }
        
    },20) 
}
function getStyle(obj,attr){
        if(obj.currentStyle){
            return obj.currentStyle[atter];
        }
        return getComputedStyle(obj,null)[attr];
    }

function startMove (obj,json,fn){
	clearInterval(obj.timer);
	obj.timer=setInterval(function(){
		var flag=true;
		for(var attr in json){
			var iTarget = json[attr];
			if(attr == "opacity"){
				var iCur = parseInt(getStyle(obj,attr)*100);
			}else{
				var iCur = parseInt(getStyle(obj,attr));
			}
			
			var iSpeed = (iTarget - iCur) / 7;
            iSpeed = iSpeed>0 ? Math.ceil(iSpeed) : Math.floor(iSpeed);
            
			if(attr == "opacity"){
				obj.style.opacity=(iCur + iSpeed)/100;
                obj.style.filter="alpha(opacity="+(iCur + iSpeed)+")";
                
			}else{
				obj.style[attr]=iCur+iSpeed+"px";
			}
			if(iCur != iTarget){
				flag=false;
			}
		}
			if(flag){
				clearInterval(obj.timer);
				if(fn){
					fn();
				}
			}
		
	},20)
}

function getStyle (obj,attr){
	if(obj.currentStyle){
		return obj.currentStyle[attr];
	}
	return getComputedStyle(obj,null)[attr];
}
