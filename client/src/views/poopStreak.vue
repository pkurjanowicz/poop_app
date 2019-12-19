<template>
    <div class='main-container'>
        <div class="poop-streak">
            <h1>Poop Streak</h1>
                <p>Days pooped in a row: <b>{{streak}}</b></p>
                <p> Most Poopy Day: <b>{{most_poops_date}}</b></p>
                <p>Messages from that fateful day...</p>
                <span v-for='(poop, index) in most_poops' :key='index'>
                    <div class='poop-box'>
                    <p>Likes: {{poop.likes}}</p>
                    <p>Message: {{poop.message}}</p>
                    <p>Rating: {{poop.rating}}</p>
                    </div>
                  </span>
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
        most_poops: '',
        most_poops_date: '',
      }
    },
    methods: {
      getStreak() {
        axios.get('streak')
        .then(resp => {
          this.streak = resp.data.streak
        })
      },
      getConsecutiveDays() {
        axios.get('consecutive-days')
        .then(resp => {
          this.most_poops = resp.data
          this.most_poops_date = resp.data[0].date
        })
      }
    },
    mounted() {
      this.getStreak()
      this.getConsecutiveDays()
    }
}
</script>


<style scoped>
.poop-streak {
  display: flex;
  flex-direction: column;
  margin: 30px;
}

.poop-box {
  display: flex;
  flex-direction: column;
  margin: 5px;
  background-color: #7E94CD;
  color: white;
  border-radius: 5px;
  padding: 10px;
}
.poop-box p {
  margin: 1px;
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