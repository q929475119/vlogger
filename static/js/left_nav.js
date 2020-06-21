$(".mainpage").click(function () {
    location.reload();
})
let a = []
let y = $(".left_nav").data("loginuser")//得到登录用户
let is_click = false;
$(".mylike").click(function () {
    a = [];
    is_click = true;
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
    for (let j = 0; j < 4 && j < a.length; j++) {
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
    let j = 4;
    $(window).scroll(function () {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(document).height();
        var windowHeight = $(this).height();
        if (scrollTop + windowHeight == scrollHeight && j < a.length) {
            loadsmallpost(j)
            j++;
        }
    })
})


$(".mycollect").click(function () {
    a = [];
    is_click = true;
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
    for (let j = 0; j < 4 && j < a.length; j++) {
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
    let j = 4;
    $(window).scroll(function () {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(document).height();
        var windowHeight = $(this).height();
        if (scrollTop + windowHeight == scrollHeight && j < a.length) {
            loadsmallpost(j)
            j++;
        }
    })
})

function loadchildblock0() {
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
        a1.style.padding = "14px 10px 6px 10px";
        a1.style.backgroundColor = "#66B1D9";
        a1.style.color = "whitesmoke";
        a1.style.cursor = "pointer";
        a1.style.textAlign = "center";
        a1.style.textDecoration = "none";
        a1.style.borderBottomWidth="1px";
        a1.style.borderBottomStyle="solid";
        a1.style.borderBottomColor="#d9d9d9 ";
        a[j] = a[j].replace("[", '');
        a[j] = a[j].replace("]", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace(" ", "");
        a1.innerHTML = a[j];
        a1.href = "/index/0/" + a[j];//第0大板块的a[j]小板块
        document.getElementById("child_block").appendChild(a1);
    }
}

function loadchildblock1() {
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
        a1.style.top = (j * 50 + 34) + "px";
        a1.style.width = "200px";
        a1.style.height = "50px"
        a1.style.padding = "14px 10px 6px 10px";
        a1.style.backgroundColor = "#66B1D9";
        a1.style.color = "whitesmoke";
        a1.style.cursor = "pointer";
        a1.style.textAlign = "center";
        a1.style.textDecoration = "none";
        a1.style.borderBottomWidth="1px";
        a1.style.borderBottomStyle="solid";
        a1.style.borderBottomColor="#d9d9d9 ";
        a[j] = a[j].replace("[", '');
        a[j] = a[j].replace("]", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace(" ", "");
        a1.innerHTML = a[j];
        a1.href = "/index/1/" + a[j];//第1大板块的a[j]小板块
        document.getElementById("child_block").appendChild(a1);
    }
}

function loadchildblock2() {
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
        a1.style.top = (j * 50 + 68) + "px";
        a1.style.width = "200px";
        a1.style.height = "50px"
        a1.style.padding = "14px 10px 6px 10px";
        a1.style.backgroundColor = "#66B1D9";
        a1.style.color = "whitesmoke";
        a1.style.cursor = "pointer";
        a1.style.textAlign = "center";
        a1.style.textDecoration = "none";
        a1.style.borderBottomWidth="1px";
        a1.style.borderBottomStyle="solid";
        a1.style.borderBottomColor="#d9d9d9 ";
        a[j] = a[j].replace("[", '');
        a[j] = a[j].replace("]", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace(" ", "");
        a1.innerHTML = a[j];
        a1.href = "/index/2/" + a[j];//第0大板块的a[j]小板块
        document.getElementById("child_block").appendChild(a1);
    }
}

function loadchildblock3() {
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
        a1.style.top = (j * 50 + 102) + "px";
        a1.style.width = "200px";
        a1.style.height = "50px"
        a1.style.padding = "14px 10px 6px 10px";
        a1.style.backgroundColor = "#66B1D9";
        a1.style.color = "whitesmoke";
        a1.style.cursor = "pointer";
        a1.style.textAlign = "center";
        a1.style.textDecoration = "none";
        a1.style.borderBottomWidth="1px";
        a1.style.borderBottomStyle="solid";
        a1.style.borderBottomColor="#d9d9d9 ";
        a[j] = a[j].replace("[", '');
        a[j] = a[j].replace("]", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace("'", '');
        a[j] = a[j].replace(" ", "");
        a1.innerHTML = a[j];
        a1.href = "/index/3/" + a[j];//第0大板块的a[j]小板块
        document.getElementById("child_block").appendChild(a1);
    }
}

let tag = -1;
$('.block0').on('mouseenter', function () {
    $('.block0').css({'background-color': '#66B1D9', 'color': 'dimgray'});
    $(".child_block").html("");
    $(".child_block").css({'display':'block'})
    loadchildblock0();
    tag = 0;
})
$('.block0').on('mouseleave', function () {
    $('.block0').css({'background-color': 'transparent', 'color': 'whitesmoke'});
    // $(".child_block").html("");
    $(".child_block").css({'display':'none'})
})
$('.block1').on('mouseenter', function () {
    $('.block1').css({'background-color': '#66B1D9', 'color': 'dimgray'});
    $(".child_block").html("");
    $(".child_block").css({'display':'block'})
    loadchildblock1();
    tag = 1;
})
$('.block1').on('mouseleave', function () {
    $('.block1').css({'background-color': 'transparent', 'color': 'whitesmoke'});
    // $(".child_block").html("");
    $(".child_block").css({'display':'none'})
})
$('.block2').on('mouseenter', function () {
    $('.block2').css({'background-color': '#66B1D9', 'color': 'dimgray'});
    $(".child_block").html("");
    $(".child_block").css({'display':'block'})
    loadchildblock2();
    tag = 2;
})
$('.block2').on('mouseleave', function () {
    $('.block2').css({'background-color': 'transparent', 'color': 'whitesmoke'});
    // $(".child_block").html("");
    $(".child_block").css({'display':'none'})
})
$('.block3').on('mouseenter', function () {
    $('.block3').css({'background-color': '#66B1D9', 'color': 'dimgray'});
    $(".child_block").html("");
    $(".child_block").css({'display':'block'})
    loadchildblock3();
    tag = 3;
})
$('.block3').on('mouseleave', function () {
    $('.block3').css({'background-color': 'transparent', 'color': 'whitesmoke'});
    // $(".child_block").html("");
    $(".child_block").css({'display':'none'})
})

$('#child_block').on('mouseenter', function () {
    if (tag == 0) {
        $('.block0').css({'background-color': '#66B1D9', 'color': 'dimgray'});
        // loadchildblock0();
        $(".child_block").css({'display':'block'})
    } else if (tag == 1) {
        $('.block1').css({'background-color': '#66B1D9', 'color': 'dimgray'});
        // loadchildblock1();
        $(".child_block").css({'display':'block'})
    } else if (tag == 2) {
        $('.block2').css({'background-color': '#66B1D9', 'color': 'dimgray'});
        // loadchildblock2();
        $(".child_block").css({'display':'block'})
    } else if (tag == 3) {
        $('.block3').css({'background-color': '#66B1D9', 'color': 'dimgray'});
        // loadchildblock3();
        $(".child_block").css({'display':'block'})
    }
})
$('#child_block').on('mouseleave', function () {
    if (tag == 0) {
        $('.block0').css({'background-color': 'transparent', 'color': 'whitesmoke'});
        // $(".child_block").html("");
        $(".child_block").css({'display':'none'})
    } else if (tag == 1) {
        $('.block1').css({'background-color': 'transparent', 'color': 'whitesmoke'});
        // $(".child_block").html("");
        $(".child_block").css({'display':'none'})
    } else if (tag == 2) {
        $('.block2').css({'background-color': 'transparent', 'color': 'whitesmoke'});
        // $(".child_block").html("");
        $(".child_block").css({'display':'none'})
    } else if (tag == 3) {
        $('.block3').css({'background-color': 'transparent', 'color': 'whitesmoke'});
        // $(".child_block").html("");
        $(".child_block").css({'display':'none'})
    }
})









