<template>
    <div class="modal-backdrop">
        <div class='subscribe-box' v-if='!response'>
            <button class="x-out-button" @click='close'> X </button>
            <div class='subscribe-form'>
                <div v-for='(error,index) in errors' :key='index'>
                    <span class='error'>{{error}}</span>
                </div>
                <input type='text' placeholder="Enter Your Name..." v-model='name'/>
                <input type='text' placeholder="Enter Your Email..." v-model='email'/>
                <span class='submit-form'><button @click='checkForm(pooper_id)'>Subscribe</button></span>
            </div>
        </div>
        <div class='subscribe-box' v-else>
            <button class="x-out-button" @click='close'> X </button>
            <div class='subscribe-form'>
                <p>Thank you for your subscription!</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";


export default {
    name: 'subscribeModal',
    props: ['pooper_id'],
    data() {
        return {
            name: '',
            email: '',
            response: '',
            errors: [],
        }
    },
    methods: {
        checkForm(pooper_id) {
            this.errors = [];

            if (!this.name) {
                this.errors.push("Name required.");
            }
            if (!this.email) {
                this.errors.push('Email required.');
            } else if (!this.validEmail(this.email)) {
                this.errors.push('Valid email required.');
            }

            if (!this.errors.length) {
                this.registerNotification(pooper_id)
                return true;
            }

        },
        registerNotification(pooper_id) {
            axios.post('register-notification', {
                name: this.name,
                email: this.email,
                subscribed_to: pooper_id,
            })
            .then(resp => {
                this.response = resp.data
            })
        },
        close() {
            this.$emit('close')
        },
        validEmail(email) {
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
        }
    }
}
</script>

<style scoped>

.subscribe-form {
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px 0 0 0;
}
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}
.subscribe-box {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    height: 300px;
    width: 300px;
    padding:30px;
}

.x-out-button {
    margin-left: auto;
    order: 0;
}

.subscribe-box button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}

.subscribe-form input[type='text'] {
  width: 80%;
  padding: 10px;
  font-size: 15px;
  margin: 10px 0;
}
.submit-form {
    margin: 30px 0 0 0;
}
.error {
    color:red;
}
</style>