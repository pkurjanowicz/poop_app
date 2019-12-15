<template>
  <div class='main-container'>
    <div class="general-status">
      <h1>Did Shant Poop Today?</h1>
        <h2>{{message}}</h2>
        <p>Shant's last poop date: <em><b>{{last_poop_date}}</b></em></p>
        <div class='rating'>
          <p>Shant's message while pooping: <em><b>{{poop_message}}</b></em></p>    
          <p class='poop-rating'>
            <span>Poop Rating(out of 5):</span>
            <span v-for='(emoji, index) in poop_rating_array' :key='index'><img :src='poop_emoji'/></span>
          </p>
          <div class='num-of-likes'>
            <img :src='num_likes'/>
            <span>{{likes}}</span>
          </div>
          <hr>
          <div class="like-comment-box">
            <span><input type='image' :src='like_btn' @click='like_post()'/></span>
          </div>
          <hr>
          <div class='little-message-box'>
            <p class='little-message'>Press enter or return to submit message and username</p>
          </div>
          <p><button v-if='displayLoginBtn' @click='commentLogin'>Login to Comment</button></p>
          <input class='userInput' v-if='displayLoginBtn == false && userNameEntered == false' type='text' placeholder="Input Username..." v-on:keyup.enter='enterUserName' v-model='modelNameValue'>
          <div class='comments-box'>
            <div class='comment' v-for='(comment, index) in comments' :key='index'>
              <span class='name'>{{comment.name}}</span><br><span class='message'>{{comment.message}}</span>
            </div>
          </div>
          <div class='commit-submit'>
          <input type='text' :placeholder='placeHolder' v-on:keyup.enter='submitComment' v-model='comment'>
          
          </div>
        </div>
      </div>
      <!-- <topRated 
        class='topRated'
        :poops='poop'
        /> -->
      <Slide class='mobile-navbar'>
        <a id="home" href="/"><span>Home</span></a>
        <a id="home" href="/toprated"><span>Liked Poops</span></a>
      </Slide>
  </div>
</template>

<script>
import axios from "axios";
// import topRated from '../components/topRated.vue';
import { Slide } from 'vue-burger-menu' 

export default {
  name: 'status',
    data() {
      return {
        poop_emoji: require('@/assets/580b57fcd9996e24bc43c39c.png'),
        num_likes: require('@/assets/JD-22-512.png'),
        like_btn: require('@/assets/like_PNG90.png'),
        message: '',
        last_poop_date: '',
        poop_message: '',
        poop_rating: '',
        poop_rating_array: [], //this is to interate through and generate emojis
        likes: '',
        comment: '',
        message_id: '',
        displayLoginBtn: true,
        modelNameValue: '',
        userName: '',
        placeHolder: 'Leave a Comment...',
        userNameEntered: false,
        comments: '',
        // poop: 'this is a message',
        nothing: '',
      }
    },
    components: {
      // topRated,
      Slide
    },
    methods: {
    getPoopDetails() {
      axios.get('get-poops')
      .then(resp => {
        this.message = resp.data.message
        this.last_poop_date = resp.data.last_poop_date
        this.poop_message = resp.data.poop_message
        this.poop_rating = resp.data.poop_rating
        this.message_id = resp.data.poop_id
        //this for loop just determines how many emojis will be used
        for (let step = 0; step < Number(this.poop_rating); step++) {
        this.poop_rating_array.push('0')
        }
        this.getCurrentLikes()
        this.getAllComments()
      })
    },
    like_post() {
      axios.post('like-post',{
        post_message: this.poop_message
      })
      .then(resp => {
        this.likes = resp.data.likes
      })
    },
    getCurrentLikes() {
      axios.post('get-likes', {
        post_message: this.poop_message
      })
      .then(resp => {
        this.likes = resp.data.likes
        if (this.likes != null) {
          this.likes = resp.data.likes
        } else {
          this.likes = '0'
        }
      })
    },
    submitComment() {
      axios.post('submit-comment',{
        comment: this.comment,
        name: this.userName,
        message: this.message_id
      })
      .then(resp => {
        this.nothing = resp
        this.comment = ''
        this.getAllComments()
      })
    },
    commentLogin() {
      this.displayLoginBtn = false
    },
    enterUserName() {
      this.userName = this.modelNameValue
      this.modelNameValue = ''
      this.placeHolder = 'Leave a Comment '+this.userName+' ...'
      this.userNameEntered = true
    },
    getAllComments() {
      axios.post('get-comments', {
        message: this.message_id
      })
      .then(resp => {
        this.comments = resp.data
      })
    }
  },
  beforeMount() {
    this.getPoopDetails()
  },
  mounted() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-container {
  display: flex;
  flex-direction: row;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
.topRated {
  margin: 30px;
}

.general-status {
  display: flex;
  flex-direction: column;
  margin: 30px;
}
.general-status img{
  max-height: 30px;
}
em b{
  color: rgb(152, 0, 0);
}
.rating {
  box-shadow: 5px 10px 8px 10px #888888;
  width: 50%;
  padding: 1% 3% 1% 3%;
}

.comments-box {
  display: flex;
  flex-direction: column;
}

.like-comment-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.like-comment-box span {
  padding: 0 10%;
}

.poop-rating {
  display:flex;
  align-items: center;
}

.num-of-likes {
  display:flex;
  align-items: center;
}
.num-of-likes span {
  font-size: 14px;
}

.rating button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}

.commit-submit input[type='text'] {
  width: 80%;
  padding: 10px;
  font-size: 15px;
  margin: 10px 0;
}

.like-comment-box input[type="image"] {
  max-height: 30px;
}

.userInput {
  width: 80%;
  padding: 10px;
  font-size: 15px;
  margin: 10px 0;
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
.little-message {
  font-size: 10px;
  background-color: yellow;
  width:270px;
}
.little-message-box {
  width:100%;
  display:flex;
}

.mobile-navbar {
    display:none;
}

/* mobile styles */
@media only screen and (max-width: 450px) {
      .rating {
        padding: 0;
        width: 100%;
        box-shadow: none;
    }
    .general-status {
      margin: 70px 30px;
    }
    .general-status h1 {
      font-size: 24px;
    }
    .general-status h2 {
      font-size: 20px;
    }
    .general-status p {
      margin: 6px 0;
    }
    .general-status img{
      max-height: 15px;
  }
  .topRated {
    display:none;
    }
  .mobile-navbar {
    display:block;
    }
}
  
  /* Tablet Styles */
  @media only screen and (min-width: 450px) and (max-width: 1025px) {
    .rating {
        padding: 0;
        width: 100%;
        box-shadow: none;
    }
    .general-status {
      margin: 70px 30px;
    }
    .topRated {
    display:none;
    }
    .mobile-navbar {
    display:block;
    }
  }


</style>
