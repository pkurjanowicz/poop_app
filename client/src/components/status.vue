<template>
  <div class="general-status">
    <h1>Did Shant Poop Today?</h1>
      <h2>{{message}}</h2>
      <p>Shant's last poop date: {{last_poop_date}}</p>
      <p>Shant's message while pooping:</p>
      <em><b><span>{{poop_message}}</span></b></em><br>
      <em>Poop Rating(out of 5): <b>{{poop_rating}}</b></em>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
    data() {
      return {
        message: '',
        last_poop_date: '',
        poop_message: '',
        poop_rating: '',
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

</style>
