<template>
  <div class="general-status">
    <h1>Did Shant Poop Today?</h1>
      <h2>{{message}}</h2>
      <p>Shant's last poop date: <em><b>{{last_poop_date}}</b></em></p>
      <p>Shant's message while pooping: <em><b>{{poop_message}}</b></em></p>
      <p>Poop Rating(out of 5):</p>
      <span v-for='(emoji, index) in poop_rating_array' :key='index'><img :src='image'/></span>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'status',
    data() {
      return {
        image: require('@/assets/580b57fcd9996e24bc43c39c.png'),
        message: '',
        last_poop_date: '',
        poop_message: '',
        poop_rating: '',
        poop_rating_array: [], //this is to interate through and generate emojis
      }
    },
    methods: {
    getPoopDetails() {
      axios.get('get-poops')
      .then(resp => {
        this.message = resp.data.message
        this.last_poop_date = resp.data.last_poop_date
        this.poop_message = resp.data.poop_message
        this.poop_rating = resp.data.poop_rating
        //this for loop just determines how many emojis will be used
        for (let step = 0; step < Number(this.poop_rating); step++) {
        this.poop_rating_array.push('0')
      }
      })
    }
  },
  mounted() {
    this.getPoopDetails()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.general-status img{
  max-height: 30px;
}

</style>
