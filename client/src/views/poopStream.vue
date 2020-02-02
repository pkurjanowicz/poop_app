<template>
    <div class='main-container'>
        <div class="sub-container">
            <h1>Poop Stream</h1>
            <subscribeModal 
              v-if='modalView'
              @close='modalClose()'
              :pooper_id='pooper_id'
            />
            <span v-for='(poop) in allPoops' :key='poop.id'>
                <div class='poop-box'>
                    <div class='message'>
                        <p><span class='name'>{{poop.name}}</span><br><span>{{poop.poop_message}}</span></p>
                        <span class='date'>{{poop.last_poop_date}}</span>
                        <div class='num-of-likes'>
                            <img :src='num_likes'/>
                            <span v-if='poop.poop_likes == null'>0</span>
                            <span v-else>{{poop.poop_likes}}</span>
                        </div>
                        <hr>
                        <div class="like-comment-box">
                            <span><input type='image' :src='like_btn' @click='like_post(poop.poop_message)'/></span>
                            <span><button @click='openModal(poop.poop_id)'>Subscribe</button></span>
                            <span>
                                <md-badge class="md-primary md-square" md-position="bottom" md-content="12">
                                  <md-button @click='openCommentBox(poop)'>
                                    Comment
                                  </md-button>
                                </md-badge>
                            </span>
                        </div>
                    </div>
                    <div class='comments-box' v-if='currently_open == poop.poop_id'>
                      <div class='comment' v-for='(comment, index) in poop.comments' :key='index'>
                        <span class='name'>{{comment.name}}</span><br><span class='message'>{{comment.message}}</span>
                      </div>
                    </div> 
                </div>
            </span>
        </div>
    </div>
</template>

<script>
import { isAuthenticated } from '../views/helpers.js'
import axios from 'axios'
import subscribeModal from '../components/subscribeModal.vue'
var Vue = require('vue');

export default {
    name: "poop-stream",
    data() {
        return {
            userSessionID: '',
            allPoops: '',
            poop_emoji: require('@/assets/580b57fcd9996e24bc43c39c.png'),
            num_likes: require('@/assets/JD-22-512.png'),
            like_btn: require('@/assets/like_PNG90.png'),
            modalView: false,
            pooper_id: '',
            comments: '',
            currently_open: '',
        }
    },
    components: {
        subscribeModal
    },
    methods: {
        getAllPoops() {
            axios.get('/get-all-poops')
            .then(resp => {
              console.log(resp.data)
              this.allPoops = resp.data
            })
        },
        openModal(pooper_id) {
            this.pooper_id = pooper_id
            this.modalView=true
        },
        modalClose() {
            this.modalView=false
        },
        like_post(message) {
          axios.post('like-post-stream',{
            post_message: message
        })
          .then(() => {
            this.getAllPoops()
        })
      },
      setLikeSession() {
        axios.get('/nonloggedinsession')
        .then()
      },
      openCommentBox(poop) {
        this.currently_open = poop.poop_id
      },
    },
    mounted() {
    this.getAllPoops()
    isAuthenticated().then(data => {
      if (data['session'] === true) {
        this.userSessionID = data['user']
      }
    })
  }
}
</script>

<style scoped>
.main-container {
    margin: 70px 30px;
}
.name {
    font-size: 24px;
    font-weight: bold;
}

.poop-box {
  display: flex;
  flex-direction: column;
  margin: 5px 0 0 0;
  border-radius: 5px;
  padding: 10px;
  border: black solid 1px;
  max-width: 500px;
}
.poop-box p {
  margin: 1px;
}

.poop-rating {
  display:flex;
  align-items: center;
}
.poop-rating img{
  max-height: 30px;
}

.num-of-likes {
  display:flex;
  align-items: center;
}
.num-of-likes span {
  font-size: 14px;
}
.num-of-likes img{
  max-height: 30px;
}

.like-comment-box input[type="image"] {
  max-height: 30px;
}
.like-comment-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.like-comment-box span {
  padding: 5px;
}

.like-comment-box button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}

.comment {
  background: rgb(229, 236, 255);
  border-radius: 5px;
  padding: 6px;
  width: 60%;
  margin: 0 0 13px 0;
}

.name {
  font-size: 14px;
  color: rgb(35, 61, 125)
}
.message {
  font-size: 18px;
}

.comment-btn{
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
  width: 20%;
  margin: 0;
}

.v-badge__badge{
  width:auto;
  border-radius: 12px;
  padding: 5px 10px;
  margin-left: 20px
}

</style>

