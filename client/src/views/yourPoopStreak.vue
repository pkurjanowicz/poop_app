<template>
    <div class='main-container'>
        <div class="sub-container">
            <h1>Coming soon...</h1>
        </div>
    </div>
</template>

<script>
import { isAuthenticated } from '../views/helpers.js'

export default {
    name: "your-poopstreak",
    mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      }
    })
  }
}
</script>

<style scoped>
.main-container {
    margin: 70px 30px;
}
</style>