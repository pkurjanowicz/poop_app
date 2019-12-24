<template>
    <div class='main-container'>
        <div class="shant">
            <h1>Who is Shant?</h1><br>
                <p>"Everyone has their morning routine.. some like to drink coffee, some like to go outside for fresh air, and some like to poop.</p>
<p>It all started when I woke up on a Monday but didn't actually start my day until Tuesday. Sometimes the daily struggle can be real, and nothing is more important to me than a poop to get the day going.</p>
<p>There's something about pooping that makes the day that much more enjoyable, and that much more pleasant. If I haven't pooped yet, I don't want to be around people because pooping is the only thing on my mind. Like the old Wu-Tang said... Poop Rules Everything Around Me."</p>
<p> - Shant</p>        
        </div>
        <div class='pic'>
          <img :src='shant_pic'/>
        </div>
    </div>
</template>


<script>
export default {
    name: 'topRated',
    props: ['poops'],
    data() {
      return {
        shant_pic: require('@/assets/unnamed.jpg'),
      }
    }
}
</script>

<style scoped>
.shant {
  display: flex;
  flex-direction: column;
  margin: 70px 30px;
}

.main-container {
  display:flex;
  flex-direction: column;
  align-items: center;
}

.pic img{
  max-width: 500px;
}

@media only screen and (max-width: 450px) {
  .shant {
      margin: 70px 30px;
    }
    .shant h1 {
      font-size: 24px;
    }
    .shant h2 {
      font-size: 20px;
    }
    .shant p {
      margin: 6px 0;
    }
    .shant img{
      max-height: 15px;
  }
  .pic img{
  max-width: 450px;
  }
}
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .shant {
      margin: 70px 30px;
    }
  }

</style>