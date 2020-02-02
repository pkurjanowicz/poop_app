<template>
    <div class="modal-backdrop">
        <div class='status-box'>
            <div class='status-form'>
                <p><input type='text' placeholder="Input  your poop date"></p>
                <p><input type='text' placeholder="Input your Message"></p>
                <p><input type='text' placeholder="Input your rating"></p>
                <p><button @click='close'>Close</button></p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'updateYourStatusModal',
    methods: {
        close() {
            this.$emit('close')
        },
    }
}
</script>

<style scoped>
.status-form {
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
.status-box {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    height: 70%;
    width: 100%;
    padding:30px;
}

.x-out-button {
    margin-left: auto;
    order: 0;
}

.status-box button {
  padding: 7px;
  font-size: 15px;
  background: #7F94CD;
  color: white;
}

.status-form input[type='text'] {
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