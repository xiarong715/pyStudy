function getTime() {
    var httpRequest = new XMLHttpRequest()
    httpRequest.open("GET", "/time", true)
    httpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    httpRequest.send(null)
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
            var json = httpRequest.responseText
            var time = JSON.parse(json).time
            var p = document.getElementById("time")
            p.innerHTML = time
        }
    }
}

getTime()
var alarm = self.setInterval("getTime()",500)

function getBlessing() {
    var httpRequest = new XMLHttpRequest()
    httpRequest.open("GET", "/blessing", true)
    httpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    httpRequest.send(null)
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
            var json = httpRequest.responseText
            var name = JSON.parse(json).name
            var blessing = JSON.parse(json).blessing
            var p = document.getElementById("blessing")
            p.innerHTML = name + " : " + blessing
        }
    }
}

getBlessing()

// jQuery
$(document).ready(function() {

    var html = '';
    for (var i = 1; i <= 50; i ++) {
        html += '<div class="shape-container--'+i+' shape-animation"><div class="random-shape"></div></div>';
    }
      
    document.querySelector('.shape').innerHTML += html;
    
    var $allShapes = $("[class*='shape-container--']");
    $('.button').click(function (event) {
        $allShapes.toggleClass("stop-shape");
        var $this = $(this);
        $this.toggleClass('.button');
        if($this.hasClass('.button')){
            $this.text('开始浮动');         
        } else {
            $this.text('停止浮动');
        }
        event.preventDefault();
    });
    
});

