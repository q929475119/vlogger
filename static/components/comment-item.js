Vue.component('comment-item', {
    props:
        [
            'comment_id',
            'floor_num',
            'user_img',
            'user_name',
            'comment_time',
            'comment_con',
            'reply_num',
            'reply_items',
            'like',
            'collect',
            'dislike',
            'comment_img'
        ],
    data() {
        like1.set(this.like);
        collect1.set(this.collect);
        dislike1.set(this.dislike);
        return {
            display_con:{
                con:true
            },
            post_text:'',
            like_comment: this.like,
            collect_comment: this.collect,
            dislike_comment: this.dislike,
            LikeIcon: {
                con: like1.getIcon(),
                color: like1.getColor()
            },
            CollectIcon: {
                con: collect1.getIcon(),
                color: collect1.getColor()
            },
            DislikeIcon: {
                con: dislike1.getIcon(),
                color: dislike1.getColor()
            }
        }
    },
    methods: {
        submit() {
                    const file = this.$refs.fileInt.files[0];
                    console.log(file);
                    if(file.size>50000)
                    {
                        window.alert('你的文件太大，请上传小于50M的文件')
                        return
                    }
                    const formData = new FormData();
                    formData.append('file', file);
                    console.log(formData)
                    axios.post('/createcomment/',formData,
                        {  // 设置axios的参数
                            method: 'POST',
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },
                            params: {
                                post_id: post_id,
                                comment_id: this.comment_id,
                                post_text: this.post_text
                            }
                        }
                    )
                        .then(function (response) {
                            console.log(formData)
                            if (response.data == 'error')
                                window.alert('发布失败，请登录')
                            else {
                                window.alert('发布成功')
                                location.reload()
                            }

                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                },
        isvideo(filePath) {
                    if (filePath === 'None' || filePath == null) {
                        return false;
                    }
                    var index = filePath.lastIndexOf(".");
                    //获取后缀
                    var ext = filePath.substr(index + 1);
                    return [
                        'mp4'].indexOf(ext.toLowerCase()) !== -1;
                },
        isimg(filePath) {
                    if (filePath == 'None'||filePath==null) {
                        return false;
                    }
                    var index = filePath.lastIndexOf(".");
                    //获取后缀
                    var ext = filePath.substr(index + 1);
                    return [
                        'png', 'jpg', 'jpeg', 'bmp', 'gif', 'webp', 'svg', 'tiff'].indexOf(ext.toLowerCase()) !== -1;
                },
             display() {
                     if (is_login)
                        this.$set(this.display_con, 'con', !this.display_con.con);
                    else {
                        window.alert('请先登录')
                        return
                    }
                }
                ,
        likecomment() {
             if(is_login!=='True')
                {
                    window.alert('请登录')
                    return
                }
            this.like_comment = 1 - this.like_comment;
            like1.set(this.like_comment);
            this.$set(this.LikeIcon, "con", like1.getIcon());
            this.$set(this.LikeIcon, "color", like1.getColor());
            axios.post('/like1/', {
                method: 'like_comment',
                value: this.like_comment,
                comment_id: this.comment_id
            })
                .then(function (response) {
                    console.log('like comment commit success');
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        collectcomment() {
             if(is_login!=='True')
                {
                    window.alert('请登录')
                    return
                }
            this.collect_comment = 1 - this.collect_comment;
            collect1.set(this.collect_comment);
            this.$set(this.CollectIcon, "con", collect1.getIcon());
            this.$set(this.CollectIcon, "color", collect1.getColor());
            axios.post('/like1/', {
                method: 'collect_comment',
                value: this.collect_comment,
                comment_id: this.comment_id
            })
                .then(function (response) {
                    console.log('collect comment commit success');
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        dislikecomment() {
             if(is_login!=='True')
                {
                    window.alert('请登录')
                    return
                }
            this.dislike_comment = 1 - this.dislike_comment;
            dislike1.set(this.dislike_comment);
            this.$set(this.DislikeIcon, "con", dislike1.getIcon());
            this.$set(this.DislikeIcon, "color", dislike1.getColor());
            axios.post('/like1/', {
                method: 'dislike_comment',
                value: this.dislike_comment,
                comment_id: this.comment_id
            })
                .then(function (response) {
                    console.log('dislike comment commit success');
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },
    template: `<div class="comment-item">
                    <div class="comment-info">
                        <div class="user-pic">
                            <img :src="user_img" alt>
                        </div>
                        <div class="user-info">
                            <div class="comment-user-info">
                                {{ user_name }}
                            </div>
                            <div class="comment-time">
                                发布于&nbsp;&nbsp;{{ comment_time }}
                            </div>
                        </div>
                    </div>
                    <div class="comment-con"><p v-html="comment_con"></p>
                    <div v-if="isimg(comment_img)">
                        <img :src="comment_img">
                    </div>
                    <div v-if="isvideo(comment_img)">
                        <video width="400" controls :src="comment_img">
                        </video>
                    </div>
                    </div>
                    <div class="comment-footer">
                        <div class="reply" @click="display"><i></i>回复</div>
                        <div class="like" @click="likecomment" :style="{color:LikeIcon.color}"><i
                        :style="{backgroundImage:'url('+LikeIcon.con+')'}"></i>喜爱</div>
                        <div class="collect" @click="collectcomment" :style="{color:CollectIcon.color}"><i
                        :style="{backgroundImage:'url('+CollectIcon.con+')'}"></i>收藏</div>
                        <div class="dislike" @click="dislikecomment" :style="{color:DislikeIcon.color}"><i
                        :style="{backgroundImage:'url('+DislikeIcon.con+')'}"></i>不喜欢</div>
                        <span class="floor-num">{{ floor_num }}楼</span>
                    </div>
                     <div class="publisher smart-green" :class="{nodisplay:display_con.con}">
                    <link rel="stylesheet" href="https://at.alicdn.com/t/font_1696224_zabz6disucb.css">
                    <textarea id="post_text" v-model="post_text" maxlength="400" placeholder="分享你的看法，限400字"></textarea>
                    <a id="file_a" href="###" style="cursor:pointer" class="iconfont icon-wenjian"><b></b>文件</a>
                    <input type="file" name="file" ref="fileInt" class="fi"
                           style="width:50px;opacity:0;cursor:pointer;position:absolute;z-index:10;margin:3px 0 0 10px"
                           id="file"/>
                    <label>
                        <span>&nbsp; </span>
                        <input type="submit" @click="submit" class="button" value="发布"/>
                    </label>
                    <div style="clear: both"></div>
                </div>
                    <div class="comment-reply">
                        <div v-if="reply_num>0">
                            <p class="reply-display">查看回复({{ reply_num }})</p>
                            <div style="clear: both"></div>
                               
                              <div class="reply-items">
                                <div class="reply-item" v-for="item in reply_items">
                                    <div class="reply-user-pic">
                                        <img :src="item.user_img" alt>
                                    </div>
                                    <div class="reply-user-info">
                                        <div class="reply-user-name">
                                            {{ item.user_name }}
                                        </div>
                                        <div class="reply-time">
                                            发布于&nbsp;&nbsp;{{ item.reply_time }}
                                        </div>
                                    </div>
                                    <div class="reply-con"><p v-html="item.reply_con"></p>
                                    <div v-if="isimg(item.reply_img)">
                                        <img :src="item.reply_img">
                                    </div></div>
                                    <div class="reply-footer">
<!--                                        <div class="like"><i></i>喜爱</div>-->
<!--                                        <div class="collect"><i></i>收藏</div>-->
<!--                                        <div class="dislike"><i></i>不喜欢</div>-->
                                        <span class="floor-num">{{ item.floor_num }}层</span>
                                    </div>
                                </div>
                            </div>  
                            
                        </div>
                  </div>
                </div>
                `
})