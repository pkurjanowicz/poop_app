<template>
    <div class='main-container'>
        <div class="sub-container">
            <h1>Poop Stream</h1>
            <span v-for='(poop, index) in allPoops' :key='index'>
                <div class='poop-box'>
                    <div class='message'>
                        <p><span class='name'>{{poop.name}}</span><br><span>{{poop.poop_message}}</span></p>
                        <span class='date'>{{poop.last_poop_date}}</span>
                        <span class='poop-rating'>
                            <span>Rating(out of 5):</span>
                            <span class='no-display'>{{poopRating(poop.poop_rating)}}</span>
                            <span v-for='(emoji, index) in poop_array' :key='index'><img :src='poop_emoji'/></span>
                        </span>
                        <div class='num-of-likes'>
                            <img :src='num_likes'/>
                            <span>{{poop.poop_likes}}</span>
                        </div>
                        <subscribeModal 
                        v-if='modalView'
                        @close='modalClose()'
                        />
                        <hr>
                        <div class="like-comment-box">
                            <span><input type='image' :src='like_btn' @click='like_post()'/></span>
                            <span><button @click='openModal()'>Subscribe</button></span>
                            <span><button @click='commentLogin()'>Comment</button></span>
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

export default {
    name: "poop-stream",
    data() {
        return {
            userSessionID: '',
            allPoops: '',
            poop_emoji: require('@/assets/580b57fcd9996e24bc43c39c.png'),
            num_likes: require('@/assets/JD-22-512.png'),
            like_btn: require('@/assets/like_PNG90.png'),
            poop_array: [],
            modalView: false,
        }
    },
    components: {
        subscribeModal
    },
    methods: {
        getAllPoops() {
            axios.get('/get-all-poops')
            .then(resp => {
                this.allPoops = resp.data
            })
        },
        poopRating(num) {
            this.poop_array = []
            for (let step = 0; step < Number(num); step++) {
                this.poop_array.push('0')
            }
        },
        openModal() {
            this.modalView=true
        },
        modalClose() {
            this.modalView=false
        },
        like_post() {
            //need to pass in the post ID, query the DB and then add a like to that post only
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
  margin: 5px;
  border-radius: 5px;
  padding: 10px;
  border: black solid 1px;
  max-width: 500px;
  height: 200px;
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
  padding: 0 50px;
}

.like-comment-box button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}

</style>

