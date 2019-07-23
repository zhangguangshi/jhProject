var oScrollList = document.getElementById("scrollList");
var aList = oScrollList.children;
var perHeight = aList[0].offsetHeight;
var i = 0;
var timer = setInterval(function () {
    move();
}, 3000)

function move() {
    i++;
    if (i == aList.length) {
        oScrollList.style.top = 0;
        i = 1;
    }
    if (i == -1) {
        oScrollList.style.top = (-perHeight) * aList.length - 1 + "px";
        i = aList.length - 2
    }
    for (var j = 0; j < aList.length; j++) {
        startMove(oScrollList, {
            top: (-perHeight) * i
        })
    }
    for (let k = 0; k < aNumList.length; k++) {
        aNumList[k].className = ""
    }
    if (i == aList.length - 1) {
        aNumList[0].className = "hover"
    } else {
        aNumList[i].className = "hover"
    }

}
//点击上下滑动
var oBtns = document.getElementById("btns");
var oPrev = oBtns.children[0];
var oNext = oBtns.children[1];
oNext.onclick = function () {
    move();
}
oPrev.onclick = function () {
    i -= 2
    move();
}
oScrollList.onmouseover = function () {
    clearInterval(timer);
}
oScrollList.onmouseout = function () {
    timer = setInterval(function () {
        move()
    }, 3000)
}
//角标变化
var oNums = document.getElementById("nums");
var aNumList = oNums.children;
for (let j = 0; j < aNumList.length; j++) {
    aNumList[j].onmouseover = function () {
        i = j - 1;
        move();
    }
}