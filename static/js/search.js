  $(function () {
        let isInsearchbox = false;
        $('#search_txt').on('focus', function () {
            //当文本框的内容不为空(包括空串和空格，消除空格)
                $('#search_btn').css({ 'background-color': '#e33e33' });
        });
        $('#search_txt').on('mouseenter',function () {
              isInsearchbox = true;
        })
        $('#search_txt').on('mouseleave',function () {
              isInsearchbox = false;
        })
      $(document).on('click',function () {
          if (isInsearchbox) {
              $('#search_btn').css({'background-color': '#e33e33'});

          } else {
              $('#search_btn').css({'background-color': '#d5d0d0'});
          }


              })
    });

function init(i){
    $("#small_post"+i).children(".like").unbind("click").click(function(){
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

 $("#small_post"+i).children(".dislike").unbind("click").click(function(){
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
            },
            error:function(data){
            }
        })
    })

 $("#small_post"+i).children(".collect").unbind("click").click(function(){
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



}
$(function() {
    a = $(".post").data("posts");
    $(".post").html("");
    if (is_click==true) return;

    for (let j = 0; j < 4&&j<a.length; j++) {
        let str = '/small_post/' + a[j] + '/' + y;
        if (y == "")
            str = '/small_post/' + a[j];
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


  function loadsmallpost(i) {
      let str = '/small_post/' + a[i] + '/' + y;
      if (y == "")
          str = '/small_post/' + a[i]
      let newdiv = "div" + i;
      let div1 = window.document.createElement("div")
      div1.className = newdiv;
      div1.style.position = "relative";
      div1.id = "div" + i
      document.getElementById("s").appendChild(div1);

               $("." + newdiv).load(str, function () {
            init(a[i]);
            })

  }






