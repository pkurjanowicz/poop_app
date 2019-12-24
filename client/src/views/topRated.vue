<template>
    <div class='main-container'>
        <div class="top-rated">
            <h1>Top Liked Poops</h1>
                <span v-for='(poop, index) in poops' :key='index'>
                    <div class='poop-box'>
                    <p>Likes: {{poop.likes}}</p>
                    <p>Message: {{poop.message}}</p>
                    <p>Rating: {{poop.rating}}</p>
                    <p>Date: {{poop.date}}</p>
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
            poops: ['poop1','poop2']
        }
    },
    methods: {
      getAllPoopLikes() {
        axios.get('get-top-liked')
        .then(resp => {
          this.poops = resp.data
        })
      }
    },
    mounted() {
      this.getAllPoopLikes()
    }
}
</script>

<style scoped>
.top-rated {
  display: flex;
  flex-direction: column;
  margin: 70px 30px;
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
  .top-rated {
      margin: 70px 30px;
    }
    .top-rated h1 {
      font-size: 24px;
    }
    .top-rated h2 {
      font-size: 20px;
    }
    .top-rated p {
      margin: 6px 0;
    }
    .top-rated img{
      max-height: 15px;
  }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .top-rated {
      margin: 70px 30px;
    }
  }

</style>