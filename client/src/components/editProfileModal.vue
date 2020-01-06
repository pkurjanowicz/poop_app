<template>
    <div class="modal-backdrop">
        <div class='modal-box'>
            <button class="x-out-button" @click='close'> X </button>
            <div class="upload">
                <label class="custom-file-upload">
                Upload Image
                <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/><br><br>
                </label><br>
                <p v-if="file">Selection Successful! Click submit to upload</p>
                <button @click="addImage()">Submit</button><br>
                <p v-if="successfulUpload">{{ successfulUpload }}<p>
                <p style="display:none">{{userSessionID}}</p>
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
    }
  },
  methods: {
    /* This function adds an image to imgur via the 
    API and then adds that image w/ user session to database */
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
            .then(response => {
              console.log(response);
              this.successfulUpload = 'Success!'
              this.file = ''
            })
            .catch(error => {
              console.log(error);
            });
        console.log(response.data.data.link);
        })
        .catch(error => {
        console.log(error);
      });
    },
    //this is bound to file input section in html
    handleFileUpload(){
        this.file = this.$refs.file.files[0]
        this.successfulUpload = ''
    },
    close() {
        this.$emit('close')
    },
    getImgurKey() {
        axios.post('/getimgurkey', {
            user_id: this.userSessionID
        })
        .then(resp => {
            this.imgur_key = resp.data.key
        })
    }
  },
  mounted() {
    this.getImgurKey()
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
    height: 300px;
    width: 300px;
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
  padding: 10px;
  font-size: 20px;
  background: #7F94CD;
  color: white;
  margin: 10px 0;
}
</style>