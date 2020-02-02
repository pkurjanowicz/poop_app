<template>
  <div class='main-container'>
    <updateYourStatusModal
      v-if='modalView'
      @close='modalClose()'
      :session_id='userSessionID'
    />
    <div class="general-status">
      <div v-if='poop_message != ""'>
        <h1>Your Status</h1>
          <p>Your last poop date: <em><b>{{last_poop_date}}</b></em></p>
          <div class='rating'>
            <p>Your message while pooping: <em><b>{{poop_message}}</b></em></p>    
            <p class='poop-rating'>
              <span>Poop Rating(out of 5):</span>
              <span v-for='(emoji, index) in poop_rating_array' :key='index'><img :src='poop_emoji'/></span>
            </p>
            <div class='num-of-likes'>
              <img :src='num_likes'/>
              <span>{{likes}}</span>
            </div>
            <hr>
          </div>
        </div>
        <div v-else>
          <h1>Please Update your Status</h1>
        </div>
        <div>
          <button @click='openModal()'>Update Your Status</button>
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import updateYourStatusModal from '../components/updateYourStatusModal'
import { isAuthenticated } from '../views/helpers.js'


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
        modalView: false,
        likes: '',
        userSessionID: '',
      }
    },
    components: {
      updateYourStatusModal
    },
    methods: {
    openModal() {
      this.modalView=true
    },
    modalClose() {
      this.modalView=false
      this.getPoopDetails()
    },
    getPoopDetails() {
      axios.post('get-specific-user-latest-poop', {
        session_id: this.userSessionID
      })
      .then(resp => {
        this.last_poop_date = resp.data[0].date
        this.poop_message = resp.data[0].message
        this.poop_rating = resp.data[0].rating
        this.message_id = resp.data[0].id
        //this for loop just determines how many emojis will be used
        for (let step = 0; step < Number(this.poop_rating); step++) {
        this.poop_rating_array.push('0')
        }
        this.getCurrentLikes()
      })
    },
    like_post() {
      axios.post('like-post',{
        post_message: this.poop_message
      })
      .then(resp => {
        this.likes = resp.data.likes
        this.setLikeSession()
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
      if (this.modelNameValue == '') {
        this.userNameEntered = false;
      } else {
        this.userNameEntered = true;
      }
      this.modelNameValue = ''
      this.placeHolder = 'Leave a Comment '+this.userName+' ...'
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
  mounted() {
      isAuthenticated().then(data => {
      if (data['session'] === false) {
          this.$router.push('/login')
      } else {
          this.userSessionID = data['user']
          this.getPoopDetails()
      }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.centeredModal{
    position: absolute;
    background: #fff;
    z-index: 100;
    width: 400px;
    left: 50%;
    margin-left: -200px;
    top: 25%;
  }

.general-status {
  display: flex;
  flex-direction: column;
  margin: 70px 30px;
}
.general-status img{
  max-height: 30px;
}
em b{
  color: rgb(152, 0, 0);
}

.comments-box {
  display: flex;
  flex-direction: column;
}

.like-comment-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.like-comment-box span {
  padding: 0 20px;
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

button {
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

.form-btn {
  margin: 10px 0 20px;
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
