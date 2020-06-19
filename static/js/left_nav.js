$(".mainpage").click(function () {
    location.reload();
})
let a=[]
let y = $(".left_nav").data("loginuser")//得到登录用户
let is_click=false;
$(".mylike").click(function () {
    a=[];
    is_click=true;
    $(".post").html("");
    if (y == "") {
        alert("先登录")
        return
    }
    $.ajax({
        async: false,
        url: '/getlikes/' + y,
        type: "POST",
        success: function (data) {
            if (data != "None") {
                a = data;
            }
        },
        error: function (data) {
            alert("error");
        }
    })
    for (let j = 0; j < 4&&j<a.length; j++) {
        let str = '/small_post/' + a[j] + '/' + y

            let newdiv = "div" + j;
            let div1 = window.document.createElement("div");
            div1.className = newdiv;
            div1.style.position = "relative";
            document.getElementById("s").appendChild(div1);
            $("." + newdiv).load(str, function () {
                init(a[j]);
            })
    }
    let j=4;
    $(window).scroll(function () {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(document).height();
        var windowHeight = $(this).height();
        if (scrollTop + windowHeight == scrollHeight&&j<a.length) {
            loadsmallpost(j)
            j++;
        }
    })
})


$(".mycollect").click(function () {
    a=[];
    is_click=true;
    if (y == "") {
        alert("先登录")
        return
    }
    $.ajax({
        async: false,
        url: '/getcollect/' + y,
        type: "POST",
        success: function (data) {
            if (data != "None")
                a = data
        },
        error: function (data) {
        }
    })

    $(".post").html("")
    for (let j = 0; j<4&&j < a.length; j++) {
        let str = '/small_post/' + a[j] + '/' + y
            let newdiv = "div" + j
            let div1 = window.document.createElement("div")
            div1.className = newdiv
            div1.style.position = "relative";
            document.getElementById("s").appendChild(div1)
            $("." + newdiv).load(str, function () {
                init(a[j]);
            })

    }
    let j=4;
    $(window).scroll(function () {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(document).height();
        var windowHeight = $(this).height();
        if (scrollTop + windowHeight == scrollHeight&&j<a.length) {
            loadsmallpost(j)
            j++;
        }
    })
})

$(".block0").click(function () {
    if (this.style.color != "dimgray") {
        $(".child_block").html("");
        this.style.color = "dimgray";
        $(".block1").css("color", "whitesmoke");
        $(".block2").css("color", "whitesmoke");
        $(".block3").css("color", "whitesmoke");
        a = $(".block0").data("block0");
        if (a == "None")
            return
        a = a.split(',');
        for (let j = 0; j < a.length; j++) {

            let newa = "childblock" + j;
            let a1 = window.document.createElement("a");
            a1.className = newa;
            a1.id = newa;
            a1.style.position = "absolute";
            a1.style.left = "0px";
            a1.style.top = (j * 50) + "px";
            a1.style.width = "200px";
            a1.style.height = "50px"
            a1.style.padding = "10px 10px";
            a1.style.backgroundColor = "#898585";
            a1.style.color = "whitesmoke";
            a1.style.cursor = "pointer";
            a1.style.textAlign = "center";
            a1.style.textDecoration = "none";
            a[j] = a[j].replace("[", '');
            a[j] = a[j].replace("]", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace(" ", "");
            a1.innerHTML = a[j];
            a1.href = "/index/0/" + a[j];//第0大板块的a[j]小板块
            document.getElementById("child_block").appendChild(a1);
        }
    } else {
        this.style.color = "whitesmoke";
        $(".child_block").html("");
    }
})


$(".block1").click(function () {
    if (this.style.color != "dimgray") {
        $(".child_block").html("");
        this.style.color = "dimgray";
        $(".block0").css("color", "whitesmoke");
        $(".block2").css("color", "whitesmoke");
        $(".block3").css("color", "whitesmoke");
        a = $(".block1").data("block1");
        if (a == "None")
            return
        a = a.split(',');
        $(".child_block").html("");
        for (let j = 0; j < a.length; j++) {

            let newa = "childblock" + j;
            let a1 = window.document.createElement("a");
            a1.className = newa;
            a1.id = newa;
            a1.style.position = "absolute";
            a1.style.left = "0px";
            a1.style.top = (j * 50 + 50) + "px";
            a1.style.width = "200px";
            a1.style.height = "50px"
            a1.style.padding = "10px 10px";
            a1.style.backgroundColor = "#898585";
            a1.style.color = "whitesmoke";
            a1.style.cursor = "pointer";
            a1.style.textAlign = "center";
            a1.style.textDecoration = "none";
            a[j] = a[j].replace("[", '');
            a[j] = a[j].replace("]", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace(" ", "");
            a1.innerHTML = a[j];
            a1.href = "/index/1/" + a[j];//第1大板块的a[j]小板块
            document.getElementById("child_block").appendChild(a1);
        }
    } else {
        this.style.color = "whitesmoke";
        $(".child_block").html("");
    }
})

$(".block2").click(function () {
    if (this.style.color != "dimgray") {
        $(".child_block").html("");
        this.style.color = "dimgray";
        $(".block1").css("color", "whitesmoke");
        $(".block0").css("color", "whitesmoke");
        $(".block3").css("color", "whitesmoke");
        a = $(".block2").data("block2");
        if (a == "None")
            return
        a = a.split(',');
        $(".child_block").html("");
        for (let j = 0; j < a.length; j++) {

            let newa = "childblock" + j;
            let a1 = window.document.createElement("a");
            a1.className = newa;
            a1.id = newa;
            a1.style.position = "absolute";
            a1.style.left = "0px";
            a1.style.top = (j * 50 + 100) + "px";
            a1.style.width = "200px";
            a1.style.height = "50px"
            a1.style.padding = "10px 10px";
            a1.style.backgroundColor = "#898585";
            a1.style.color = "whitesmoke";
            a1.style.cursor = "pointer";
            a1.style.textAlign = "center";
            a1.style.textDecoration = "none";
            a[j] = a[j].replace("[", '');
            a[j] = a[j].replace("]", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace(" ", "");
            a1.innerHTML = a[j];
            a1.href = "/index/2/" + a[j];//第0大板块的a[j]小板块
            document.getElementById("child_block").appendChild(a1);
        }
    } else {
        this.style.color = "whitesmoke";
        $(".child_block").html("");
    }
})

$(".block3").click(function () {
    if (this.style.color != "dimgray") {
        $(".child_block").html("");
        this.style.color = "dimgray";
        $(".block1").css("color", "whitesmoke");
        $(".block2").css("color", "whitesmoke");
        $(".block0").css("color", "whitesmoke");
        a = $(".block3").data("block3");
        if (a == "None")
            return
        a = a.split(',');
        $(".child_block").html("");
        for (let j = 0; j < a.length; j++) {

            let newa = "childblock" + j;
            let a1 = window.document.createElement("a");
            a1.className = newa;
            a1.id = newa;
            a1.style.position = "absolute";
            a1.style.left = "0px";
            a1.style.top = (j * 50 + 150) + "px";
            a1.style.width = "200px";
            a1.style.height = "50px"
            a1.style.padding = "10px 10px";
            a1.style.backgroundColor = "#898585";
            a1.style.color = "whitesmoke";
            a1.style.cursor = "pointer";
            a1.style.textAlign = "center";
            a1.style.textDecoration = "none";
            a[j] = a[j].replace("[", '');
            a[j] = a[j].replace("]", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace("'", '');
            a[j] = a[j].replace(" ", "");
            a1.innerHTML = a[j];
            a1.href = "/index/3/" + a[j];//第0大板块的a[j]小板块
            document.getElementById("child_block").appendChild(a1);
        }
    } else {
        this.style.color = "whitesmoke";
        $(".child_block").html("");
    }
})








