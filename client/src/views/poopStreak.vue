<template>
    <div class='main-container'>
        <div class="poop-streak">
            <h1>Poop Streak</h1>
                <p>Days pooped in a row: {{streak}}</p>
        </div>
    </div>
</template>


<script>
import axios from "axios";

export default {
    name: 'topRated',
    data() {
      return {
        streak: '',
      }
    },
    methods: {
      getStreak() {
        axios.get('streak')
        .then(resp => {
          this.streak = resp.data.streak
        })
      }
    },
    mounted() {
      this.getStreak()
    }
}
</script>


<style scoped>
.poop-streak {
  display: flex;
  flex-direction: column;
  margin: 30px;
}

@media only screen and (max-width: 450px) {
  .poop-streak {
      margin: 70px 30px;
    }
    .poop-streak h1 {
      font-size: 24px;
    }
    .poop-streak h2 {
      font-size: 20px;
    }
    .poop-streak p {
      margin: 6px 0;
    }
    .poop-streak img{
      max-height: 15px;
  }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .poop-streak {
      margin: 70px 30px;
    }
  }

</style>