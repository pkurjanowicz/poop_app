<template>
    <div class='main-container'>
        <div class="sub-container">
          <p class='error' v-if='error'>{{error}}</p>
            <div class='profile-container'>
              <div class='profile-bio'>
                <h3 v-if='current_number != null' class='current-number-parent'>Your Phone Number
                <p class='current-number'>{{current_number}}</p>
                </h3>
                <h3 v-else class='current-number-parent' >Your Phone Number
                <span class='current-number'>Please Input Your Number</span>
                </h3>
                <button @click='inputNumberClick()'>Input your phone number</button>
                <p v-if='openNumberInput == false && validSubmission'>Phone Number Updated!</p>
                <div v-if='openNumberInput' class='phone-input'>
                  <vue-tel-input 
                    v-bind="bindProps"
                    placeholder='Phone Number...'
                    @onInput='onInput'
                  />
                  <button @click='submitNumber'>Submit</button>
                </div>
                <hr>
                <h3>Your Profile</h3>
                <p v-if='!profileBio'>Please enter a profile</p>
                <p v-else style="white-space: pre-line">{{profileBio}}</p>
                <button @click='openModal'>Edit Your Profile</button>
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
import { VueTelInput } from 'vue-tel-input'

export default {
    name: "your-profile",
    data() {
      return {
        openModalView: false,
        userSessionID: '',
        profileImage: '',
        profileBio: '',
        openNumberInput: false,
        error: '',
        validSubmission: false,
        current_number: '',
        phone: {
          number: '',
          isValid: false,
        },
        bindProps: { 
          onlyCountries: ["US"],
          defaultCountry: 'US',
          validCharactersOnly: true,
        }
      }
    },
    components: {
      editProfileModal,
      VueTelInput,
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
      },
      inputNumberClick() {
        if (this.openNumberInput == false) {
          this.openNumberInput = true
          this.validSubmission = false
        } else {
          this.openNumberInput = false
          this.error = ''
        }
      },
      submitNumber() {
        if (this.phone.isValid == true) {
          axios.post('/update_number', {
            number: this.phone.number.input,
            user_id: this.userSessionID
          })
          .then(() => {
            this.error = ''
            this.validSubmission = true
            this.openNumberInput = false
            this.current_number = this.getPhoneNumber()
          })
        } else {
          this.error = 'Invalid Number'
        }
      },
      onInput({ number, isValid, country }) {
      this.phone.number = number;
      this.phone.isValid = isValid;
      this.phone.country = country;
      },
      getPhoneNumber() {
        axios.post('/get_number', {
          user_id: this.userSessionID
        })
        .then(resp => {
          this.current_number = resp.data.number
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
        this.getPhoneNumber()
      }
    })
  }
}
</script>

<style scoped>

.error {
    color: red
}

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
.sub-container {
  display: flex;
  flex-direction: column;
}
.sub-container input[type='text'] {
  width: 80%;
  padding: 10px;
  font-size: 15px;
  margin: 10px 0;
}

.vue-tel-input {
  padding: 10px;
  font-size: 15px;
  margin: 10px 0;
}

/* .phone-input {
  max-width: 40%;
} */

.sub-container button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}
.current-number-parent {
  display: flex;
  flex-direction: column;
  margin: 20px 0 0 0;
}
.current-number {
  font-size: 15px;
}

</style>