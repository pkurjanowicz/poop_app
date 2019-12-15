<template>
    <div class='main-container'>
        <div class="shant">
            <h1>Who is Shant?</h1>
                <p>Coming soon...</p>
        </div>
    </div>
</template>


<script>
export default {
    name: 'topRated',
    props: ['poops'],
}
</script>

<style scoped>
.shant {
  display: flex;
  flex-direction: column;
  margin: 30px;
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
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .shant {
      margin: 70px 30px;
    }
  }

</style>