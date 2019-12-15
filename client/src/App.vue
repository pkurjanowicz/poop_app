<template>
  <div id="app">
    <navBar/>
    <router-view></router-view>
  </div>
</template>

<script>
import navBar from './components/navBar.vue'

export default {
  name: 'app',
  components: {
    navBar,
  }
}
</script>

<style>
.main-container {
  display: flex;
  flex-direction: row;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>
