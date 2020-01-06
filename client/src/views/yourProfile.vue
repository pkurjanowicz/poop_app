<template>
    <div class='main-container'>
        <div class="sub-container">
          <button @click='openModal'>Edit Your Profile</button>
          <editProfileModal
            v-if='openModalView'
            @close='closeModal()'
            :userSessionID='userSessionID'
          />
        </div>
    </div>
</template>

<script>
import { isAuthenticated } from '../views/helpers.js'
import editProfileModal from '../components/editProfileModal'

export default {
    name: "your-profile",
    data() {
      return {
        openModalView: false,
        userSessionID: ''
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
      }
    },
    mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
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

button {
  padding: 10px;
  font-size: 20px;
  background: #7F94CD;
  color: white;
  margin: 10px 0;
}

</style>