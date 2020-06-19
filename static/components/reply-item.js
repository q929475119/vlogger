Vue.component('reply_items',{
    props:[
        'reply_items'
    ],
    template:`
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
                                    <div class="reply-con"><p>{{ item.reply_con }}</p></div>
                                    <div class="reply-footer">
                                        <div class="like"><i></i>喜爱</div>
                                        <div class="collect"><i></i>收藏</div>
                                        <div class="dislike"><i></i>不喜欢</div>
                                        <span class="floor-num">{{ item.floor_num }}层</span>
                                    </div>
                                </div>
                            </div>
                            `
})