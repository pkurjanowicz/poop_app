<template>
    <div class="modal-backdrop">
        <div class='modal-box'>
            <button class="x-out-button" @click='close'> X </button>
            <div class="upload">
                <p>Update your profile image</p>
                <label class="custom-file-upload">
                Upload Image
                <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/><br><br>
                </label><br>
                <p class='file-name' v-if="file">{{file.name}}</p>
                <p>Update your profile</p>
                <textarea cols="50" rows="15" v-model="profile"/>
                <button @click="submit()">Submit</button><br>
                <p v-if='successfulSave'>You have successfully updated your profile!</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'editProfileModal',
    props:['userSessionID'],
    data() {
    return {
      file: '',
      successfulUpload: '',
      imgur_key: '',
      profile: '',
      successfulSave: false,
    }
  },
  methods: {
    submit() {
        if (this.file != '') {
            this.addImage()
        }
        this.addProfile()
        this.successfulSave = true
    },
    addImage() {
      let formData = new FormData();
      formData.append('image', this.file);
      axios.post('https://api.imgur.com/3/image', formData, {
        headers: {
          'Authorization': this.imgur_key,
          'Content-Type': 'multipart/form-data'
          },
        })
        .then(response => {
          axios.post('/addimage', {
              link: response.data.data.link,
              user_id: this.userSessionID
            })
            .then(() => {
              this.successfulUpload = 'Success!'
              this.file = ''
            })
        })
    },
    //this is bound to file input section in html
    handleFileUpload(){
        this.file = this.$refs.file.files[0]
        this.successfulUpload = ''
    },
    close() {
        this.$emit('close')
        this.successfulSave = false
    },
    getImgurKey() {
        axios.post('/getimgurkey', {
            user_id: this.userSessionID
        })
        .then(resp => {
            this.imgur_key = resp.data.key
        })
    },
    addProfile() {
        axios.post('/updateprofile', {
            user_id: this.userSessionID,
            profile: this.profile
        })
        .then((resp) => {
            this.profile = resp.data.profile
        })
    },
    getProfile() {
        axios.post('/getprofile', {
            user_id: this.userSessionID
        })
        .then((resp) => {
            this.profile = resp.data.profile
        })
    }
  },
  mounted() {
    this.getImgurKey()
    this.getProfile()
  }
}
</script>

<style scoped>
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

.modal-box {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    height: 600px;
    width: 400px;
    padding:30px;
}

.x-out-button {
    margin-left: auto;
    order: 0;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 12px 4px 12px;
    cursor: pointer;
    margin: 30px 0 0;
}

.upload {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
}
input[type=file] {
    display:none;
}
button {
  padding: 8px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
  margin: 20px 0 5px;
}

.file-name {
    font-size:12px;
}
</style>