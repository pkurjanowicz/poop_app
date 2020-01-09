<template>
    <div class='main-container'>
        <div class="sub-container">
          <button @click='openModal'>Edit Your Profile</button>
            <div class='profile-container'>
              <div class='profile-bio'>
                <h3>Your Profile</h3>
                <hr>
                <p v-if='!profileBio'>Please enter a profile</p>
                <p v-else style="white-space: pre-line">{{profileBio}}</p>
                <hr>
              </div>
              <br>
              <div class='profile-img'>
                <img :src="profileImage">
              </div>
            <editProfileModal
              v-if='openModalView'
              @close='closeModal()'
              :userSessionID='userSessionID'
            />
          </div>
        </div>
    </div>
</template>

<script>
import { isAuthenticated } from '../views/helpers.js'
import editProfileModal from '../components/editProfileModal'
import axios from 'axios'

export default {
    name: "your-profile",
    data() {
      return {
        openModalView: false,
        userSessionID: '',
        profileImage: '',
        profileBio: '',
      }
    },
    components: {
      editProfileModal
    },
    methods: {
      openModal() {
        this.openModalView= true
      },
      closeModal() {
        this.openModalView = false
        this.getProfileImage()
        this.getProfileBio()
      },
      getProfileImage() {
        axios.post('/getimagelink', {
          user_id: this.userSessionID
        })
        .then(resp =>{
          this.profileImage = resp.data.image
        })
      },
      getProfileBio() {
        axios.post('/getprofile', {
          user_id: this.userSessionID
        })
        .then(resp => {
          this.profileBio = resp.data.profile
        })
      }
    },
    mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
        this.userSessionID = data['user']
        this.getProfileImage()
        this.getProfileBio()
      }
    })
  }
}
</script>

<style scoped>
.main-container {
    margin: 70px 30px;
}

button {
  padding: 8px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
  margin: 20px 0 5px;
}

.profile-img img {
  max-width: 100%;
}

.profile-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  max-width: 700px;
}

</style>