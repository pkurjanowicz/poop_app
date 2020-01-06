<template>
<div class=register-box>
  <div class="register-form">
    <p class='error' v-if='error'>Passwords do not match</p>
    <input @keyup.enter.exact='addUser' type="text" v-model="username" placeholder="Username"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="password" placeholder="Password"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="retypePassword" placeholder="Retype Password"/>
    <button @click="addUser">Register</button>
    <div><router-link to="/login">Already have an account?</router-link></div>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
    name: "register",
    data() {
    return {
      username: '',
      password: '',
      retypePassword:'',
      error: '',
    }
  },
  methods: {
    /* add a new user, note there is no 
    client side validation in place yet...*/ 
    addUser() {
      if (this.password == this.retypePassword) {
        axios.post('adduser', {
        username: this.username, 
        password: this.password
        })
        .then(response => {
        console.log(response);
        })
        .catch(error => {
        console.log(error);
      });
      this.username = '';
      this.password = '';
      /* this setTimeout() allows for the session to be set and then will redirect*/
      setTimeout(() => this.$router.push({ path: '/yourstatus'}), 500);
      } else {
        this.error = 'Passwords do not match'
      }
    }
  },
}

</script>

<style scoped>

.register-box {
      margin: 70px 30px;
      height: 300px;
      width: 300px;
    }

.register-form {
    padding: 15%;
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.register-form div {
    padding: 10% 0;
}
.register-form div a {
      font-size: 20px;
    }
button {
      padding: 5px;
      font-size: 20px;
    }

input[type=text], input[type=password] {
      font-size: 20px;
      margin: 10px 0
    }

</style>