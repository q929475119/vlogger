$(function() {
            $("#click_topic").click(function () {
                $("#topic").css("display", "block");
            });
            n_topic =0;
            $("#endtopic").click(function () {
                var topic_str = $("#topic_name").val();
				if (topic_str===""){
					$("#topic_name").attr("placeholder","不能为空");
				}else if(topic_str.length>10){
					$("#topic_name").attr("placeholder","话题不能超过12");
				}
				else{
					var topic_tab = $("#topic_try").html();
					var topic_op = "<input type='radio' name='topic_select' id='t"+n_topic+"'><label for='t"+n_topic+"'>"+topic_str+"</label>"
					n_topic += 1;
					var topic_label = topic_tab + topic_op;
					$("#topic_try").html(topic_label);
					$("#topic").css("display", "none");
				}
            });

            $("#topic_name").keyup(function(event){
            var search_text = $("#topic_name").val();
            if(search_text !== ''){
                id_i = 0;
                var tab = "<br>";
                $.each(topic_list,function (id,item) {
                    if(item.title.indexOf(search_text)!==-1){
                        id_i += 1;
                        tab+="<li id='l"+id_i+"' style='list-style-type: none;\n" +
                            "    background-color: #FFFFFF;\n" +
                            "    width: 150px;\n" +
                            "    height:20px;\n" +
                            "    color:#A8A297;\n" +
                            "    font-size: 15px;\n" +
                            "    margin-top: 8px;\n" +
                            "    border-radius: 5px;\n" +
                            "    -webkit-border-radius: 5px;\n" +
                            "    -moz-border-radius: 5px;\n" +
                            "    padding-left: 10px;'>" +
                            item.title+"</li>"
                    }
                });
                $("#old_topic").html(tab);
                tab = "";
            }else{
                $("#old_topic").html("");
            }
            });
        $("#old_topic").on("click","li",function(){
            var topic_str = $(this).text();
            var topic_tab = $("#topic_try").html();
            var topic_op = "<input type='radio' name='topic_select' id='t"+n_topic+"'><label for='t"+n_topic+"'>"+topic_str+"</label>"
            var n_topic = n_topic+1;
            var topic_label = topic_tab + topic_op;
            $("#topic_try").html(topic_label);
            $("#topic").css("display", "none");
        })
        $("#old_topic").on("mouseover","li",function(){
            $(this).css({"backgroundColor":"grey","color":"#FFFFFF"});
        })
        $("#old_topic").on("mouseout","li",function(){
            $(this).css({"backgroundColor":"#FFFFFF","color":"#A8A297"});
        })
        $("#no_topic").click(function(){
            $("#topic").css("display", "none");
        })
        $("#block_p").change(function(){
            $("#block_c").empty();
            var which_block;
            var parent = $("#block_p").val();
            if (parent === '1'){
                alert(block_all.block0);
                which_block = block_all.block0;
            }else if(parent === '2'){
                which_block = block_all.block1;
            }else if(parent === '3'){
                which_block = block_all.block2;
            }else if(parent === '4'){
                which_block = block_all.block3;
            }
            $.each(which_block,function (i,m) {
                var selectnode = document.createTextNode(m);
                var opEle = document.createElement('option');
                $(opEle).val(m);
                $(opEle).append(selectnode);
                $(opEle).appendTo($("#block_c"));
            })
        })
        $("#post_form").submit(function () {
            if($("#login_user").val()===''){
				alert("请先登录");
				return false;
			}
			if($("#title").val()===""){
                $("#title").attr("placeholder","标题不能为空");
                return false;
            }
            if($("#post_text").val()==="") {
                $("#post_text").attr("placeholder", "正文内容不能为空");
                return false;
            }
			
            
        })
        $("#click_topic").mouseover(function () {
            $(this).css("color","red");
        })
        $("#click_topic").mouseout(function () {
            $(this).css("color","white");
        })
        $("#file").mouseover(function () {
            $("#file_a").css("color","blue");
        })
        $("#file").mouseout(function () {
            $("#file_a").css("color","white");
        })
    });