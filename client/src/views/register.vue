<template>
<div class=register-box>
  <div class="register-form">
    <p class='error' v-if='error'>{{error}}</p>
    <input @keyup.enter.exact='addUser' type="text" v-model="username" placeholder="Username"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="password" placeholder="Password"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="retypePassword" placeholder="Retype Password"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="code" placeholder="Code"/>
    <button @click="addUser">Register</button>
    <div class='sign-up-btn'>Already have an account?<a href="/login"> Login</a></div>
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
      code: '',
    }
  },
  methods: {
    /* add a new user, note there is no 
    client side validation in place yet...*/ 
    addUser() {
      if (this.password == this.retypePassword) {
        axios.post('adduser', {
        username: this.username, 
        password: this.password,
        code: this.code,
        })
        .then(response => {
            if (response.data.success == false) {
                this.$router.push({ path: '/register'})
                this.error = 'Incorrect code'
            } else {
                this.username = '';
                this.password = '';
                /* this setTimeout() allows for the session to be set and then will redirect*/
                setTimeout(() => this.$router.push({ path: '/yourstatus'}), 500);
            }
        console.log(response);
        })
        .catch(error => {
        console.log(error);
      });
      } else {
        this.error = 'Passwords do not match'
      }
    }
  },
}

</script>

<style scoped>

.error {
    color: red
}

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
.sign-up-btn, a {
  font-size: 13px;
  text-decoration: none;
}
button {
  padding: 10px;
  font-size: 20px;
  background: #7F94CD;
  color: white;
  margin: 10px 0;
}

input[type=text], input[type=password] {
      font-size: 20px;
      margin: 10px 0;
      padding: 10px;
    }

</style>