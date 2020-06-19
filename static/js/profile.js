$(document).ready(function () {
    //个人资料头像预览，并将表单提交
    $('#AvatarUpload').uploadPreview({
        Img: "AvatarShow",
        Width: 100,
        Height: 100,
        Callback: function () {
            $('#AvatarForm').submit();
        }
    });

    //点击button按钮，触发文件输入框的鼠标点击事件，进而可以弹出上传文件窗口
    $("#AvatarButton").click(function () {
        $("#AvatarUpload").click();
    });

    //通过监视距离顶部的距离，控制回到顶部div的显示
    $(window).scroll(function () {
        if ($(window).scrollTop() > 500) {
            $("#CornerButtons").fadeIn(1000);//一秒渐入动画
        } else {
            $("#CornerButtons").stop(true, true).fadeOut(1000);//一秒渐隐动画
        }
    });

    //点击后0.5s跳转到页面投
    $("#CornerButtons").click(function () {
        $('body,html').animate({scrollTop: 0}, 500);
    });

    /*让隐藏的背景层和弹出框显现*/
    $(".popBox").on("click", function () {
        $(".bg").css("display", "block");
        $(".dialog").css("display", "block");
        $(".dialogbox").css("display", "block");
    });

    /*点击叉后，让背景层和弹出框隐藏*/
    $(".close").on("click", function () {
        $(".bg").hide();
        $(".dialog").hide();
        $(".dialogbox").hide();
        /*重置表单，即清空原来输入的内容*/
        if ($(this).parent().find('form')[0]) {
            $(this).parent().find('form')[0].reset();
        }
    });
    // 点击小眼睛可以明文显示密码，反之隐藏密码；实际上就是改变了input框的类型；应用了Font Awesome库
    $("#eye0").click(function () {
        var pwd0 = $("#password0");
        if (pwd0.attr("type") === "password") {
            pwd0.attr("type", "text");
            $(this).attr("class", "fa fa-eye-slash eye");
        } else {
            pwd0.attr("type", "password");
            $(this).attr("class", "fa fa-eye eye");
        }
    });

    $("#eye1").click(function () {
        var pwd1 = $("#password1");
        if (pwd1.attr("type") === "password") {
            pwd1.attr("type", "text");
            $(this).attr("class", "fa fa-eye-slash eye");
        } else {
            pwd1.attr("type", "password");
            $(this).attr("class", "fa fa-eye eye");
        }
    });

    $("#eye2").click(function () {
        var pwd2 = $("#password2");
        if (pwd2.attr("type") === "password") {
            pwd2.attr("type", "text");
            $(this).attr("class", "fa fa-eye-slash eye");
        } else {
            pwd2.attr("type", "password");
            $(this).attr("class", "fa fa-eye eye");
        }
    });

    var y = $("#GetLoginuser").data("loginuser"); /*获取登录的用户名，是从会话中获取的account*/
    /*提交修改密码的表单*/
    $(".ChangePwdBtn").on("click", function () {
        $.ajax({
            cache: false,
            type: "POST",
            async: true,
            dataType: "json",
            data: $('.ChangePwdForm').serialize(),
            url: "/usercenter/change/password/" + y,
            success: function (data) {
                if (data.status === "success") {
                    alert("修改密码成功，请重新登录！");
                    window.location = "/login/"; // 后续修改为登录界面的url
                } else if (data.status === "fail") {
                    alert(data.message);
                }
            }
        });
    });

    // 如果未登录，即获取到的用户名为未定义，不能进行点赞反对收藏的事件
    if ((typeof y) !== "undefined") {
        $(".like").click(function () {
            let x = $(this).data('a');
            if (this.style.color == "rgb(235, 115, 80)") {
                this.style.color = "#808080"
                $("#small_post" + x).find(".like i").attr("class", "fa fa-thumbs-o-up")
            }/*取消点赞*/
            else {
                $("#small_post" + x).find(".like i").attr("class", "fa fa-thumbs-up")
                this.style.color = "#eb7350"/*点赞*/
                dislike_color = $("#small_post" + x).children(".dislike").css('color')
                if (dislike_color == "rgb(235, 115, 80)") {
                    $("#small_post" + x).children('.dislike').css({'color': '#808080'});
                    $("#small_post" + x).find(".dislike i").attr("class", "fa fa-thumbs-o-down")
                }
            }

            $.ajax({
                url: "/like/",
                data: {"loginuser": y, "post_id": x},
                type: "POST",
                success: function (data) {
                    // alert("√"+data)
                },
                error: function (data) {
                    // alert("×"+data)
                }
            })
        })

        $(".dislike").click(function () {
            let x = $(this).data('a');
            if (this.style.color == "rgb(235, 115, 80)")/*取消反对*/
            {
                this.style.color = "#808080"
                $("#small_post" + x).find(".dislike i").attr("class", "fa fa-thumbs-o-down")
            } else {
                $("#small_post" + x).find(".dislike i").attr("class", "fa fa-thumbs-down")
                this.style.color = "#eb7350"/*反对*/
                like_color = $("#small_post" + x).children(".like").css('color')
                if (like_color == "rgb(235, 115, 80)") {
                    $("#small_post" + x).children('.like').css({'color': '#808080'});
                    $("#small_post" + x).find(".like i").attr("class", "fa fa-thumbs-o-up")
                }
            }
            $.ajax({
                url: "/oppose/",
                data: {"loginuser": y, "post_id": x},
                type: "POST",
                success: function (data) {
                    // alert("√"+data)
                },
                error: function (data) {
                    // alert("×"+data)
                }
            })
        })

        $(".collect").click(function () {
            let x = $(this).data('a');
            if (this.style.color == "rgb(235, 115, 80)") {
                this.style.color = "#808080"
                $("#small_post" + x).find(".collect i").attr("class", "fa fa-star-o")
            } else {
                this.style.color = "#eb7350"
                $("#small_post" + x).find(".collect i").attr("class", "fa fa-star")
            }
            $.ajax({
                url: "/collect/",
                data: {"loginuser": y, "post_id": x},
                type: "POST",
                success: function (data) {
                    // alert("√"+data)
                },
                error: function (data) {
                    // alert("×"+data)
                }
            })
        })
    }
});
