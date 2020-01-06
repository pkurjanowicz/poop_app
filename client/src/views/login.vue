<template>
    <div class='login-box'>
        <div class="login-form">
            <input @keyup.enter.exact='checkUser' type="text" v-model="username" placeholder="Username"/>
            <input @keyup.enter.exact='checkUser' type="password" v-model="password" placeholder="Password"/>
            <button @click="checkUser" >Login</button>
            <div><router-link to="/register">Register</router-link></div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
// import { isAuthenticated } from '../helpers.js'

export default {
    name: "login",
    data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    /* authenticates the user in the db */
    checkUser() {
      axios.post('checklogin', {
        username: this.username, 
        password: this.password
        })
        .then(function (response) {
        console.log(response);
        })
        .catch(function (error) {
        console.log(error);
      });
      this.username = '';
      this.password = '';
      /* this setTimeout() allows for the session to be set and then will redirect*/
      setTimeout(() => this.$router.push({ path: '/yourstatus'}), 300);
    }
  }
}
</script>

<style scoped>

.login-box {
      margin: 70px 30px;
      height: 300px;
      width: 300px;
    }

.login-form {
    padding: 15%;
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.login-form div {
    padding: 10% 0;
}
.login-form div a {
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




