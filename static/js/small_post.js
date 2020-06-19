$(".like").click(function(){
        let x = $(this).data('a')
        let y = $(".small_post").data("loginuser")//得到登录用户
        if(y==""){
            alert("先登录");
            return;
        }
        if(this.style.color=="rgb(235, 115, 80)")
        {
            this.style.color="#808080"
            $("#small_post"+x).find(".like i").attr("class","fa fa-thumbs-o-up")
        }/*取消点赞*/
        else
        {
            $("#small_post"+x).find(".like i").attr("class","fa fa-thumbs-up")
            this.style.color="#eb7350"/*点赞*/
            dislike_color = $("#small_post"+x).children(".dislike").css('color')
            if(dislike_color=="rgb(235, 115, 80)")
             {
                  $("#small_post"+x).children('.dislike').css({'color':'#808080'});
                  $("#small_post"+x).find(".dislike i").attr("class","fa fa-thumbs-o-down")
             }
        }

        $.ajax({
            url:"/like/",
            data:{"loginuser":y,"post_id":x},
            type:"POST",
            success:function(data){
            },
            error:function(data){
            }
        })
    })

$(".dislike").click(function(){
        let x = $(this).data('a');
        let y=$(".small_post").data('loginuser');
        if(y==""){
            alert("先登录");
            return;
        }
        if(this.style.color=="rgb(235, 115, 80)")/*取消反对*/
        {
            this.style.color="#808080"
            $("#small_post"+x).find(".dislike i").attr("class","fa fa-thumbs-o-down")
        }
        else
        {
            $("#small_post"+x).find(".dislike i").attr("class","fa fa-thumbs-down")
            this.style.color="#eb7350"/*反对*/
            like_color = $("#small_post"+x).children(".like").css('color')
            if(like_color=="rgb(235, 115, 80)")
             {
                  $("#small_post"+x).children('.like').css({'color':'#808080'});
                  $("#small_post"+x).find(".like i").attr("class","fa fa-thumbs-o-up")
             }
        }
        $.ajax({
            url:"/oppose/",
            data:{"loginuser":y,"post_id":x},
            type:"POST",
            success:function(data){
                // alert("√"+data)
            },
            error:function(data){
                // alert("×"+data)
            }
        })
    })

$(".collect").click(function(){
        let x = $(this).data('a');
        let y=$(".small_post").data('loginuser');
        if(y==""){
            alert("先登录");
            return;
        }
        if(this.style.color=="rgb(235, 115, 80)")
        {
            this.style.color="#808080"
            $("#small_post"+x).find(".collect i").attr("class","fa fa-star-o")
        }
        else
        {
            this.style.color="#eb7350"
             $("#small_post"+x).find(".collect i").attr("class","fa fa-star")
        }
        $.ajax({
            url:"/collect/",
            data:{"loginuser":y,"post_id":x},
            type:"POST",
            success:function(data){
            },
            error:function(data){
            }
        })
    })


