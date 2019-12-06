<template>
  <div class="general-status">
    <h1>Did Shant Poop Today?</h1>
      <h2>{{message}}</h2>
      <p>Shant's last poop date: <em><b>{{last_poop_date}}</b></em></p><br>
      <div class='rating'>
        <p>Shant's message while pooping: <em><b>{{poop_message}}</b></em></p>    
        <p class='poop-rating'>
          <span>Poop Rating(out of 5):</span>
          <span v-for='(emoji, index) in poop_rating_array' :key='index'><img :src='poop_emoji'/></span>
        </p>
        <div class='num-of-likes'>
          <img :src='num_likes'/>
          <span>1</span>
        </div>
        <hr>
        <div class="like-comment-box">
          <span><input type='image' :src='like_btn'/></span><span>Comment</span>
        </div>
        <hr>
        <p><button>Login to Comment</button></p>
        <div class='comments-box'>
          <br>
          <br>
          <br>
        </div>
        <div class='commit-submit'>
        <input type='text' placeholder="Leave a Comment...">
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios";

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
      }
    },
    methods: {
    getPoopDetails() {
      axios.get('get-poops')
      .then(resp => {
        this.message = resp.data.message
        this.last_poop_date = resp.data.last_poop_date
        this.poop_message = resp.data.poop_message
        this.poop_rating = resp.data.poop_rating
        //this for loop just determines how many emojis will be used
        for (let step = 0; step < Number(this.poop_rating); step++) {
        this.poop_rating_array.push('0')
      }
      })
    }
  },
  mounted() {
    this.getPoopDetails()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
  border: 3px solid black;
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

</style>
