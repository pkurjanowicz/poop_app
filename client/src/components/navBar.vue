<template>
    <div>
        <div class="navbar">
            <!-- router-link is actually linked to the router.js file -->
            <router-link to="/"><button class='navbar-btn'>Home</button></router-link>
            <router-link to="/toprated"><button class='navbar-btn'>Liked Poops</button></router-link>
            <router-link to="/shant"><button class='navbar-btn'>Who is Shant?</button></router-link>
            <router-link to="/poopstreak"><button class='navbar-btn'>Poop Streak</button></router-link>
        </div>
        <Slide class='mobile-navbar'>
            <a id="home" href="/"><span>Home</span></a>
            <a id="home" href="/toprated"><span>Liked Poops</span></a>
            <a id="home" href="/shant"><span>Who is Shant?</span></a>
            <a id="home" href="/poopstreak"><span>Poop Streak</span></a>
        </Slide>
    </div>
</template>

<script>

import { Slide } from 'vue-burger-menu'  

export default {
  name: 'navBar',
  components: {
        Slide, 
    },
}
</script>

<style scoped>
.navbar {
    display: flex;
    flex-direction: row;
}

.navbar-btn {
    padding: 20px;
    height: 100%;
    background-color: #7E94CD;
    font-size: 15px;
    color: white;
    border: 3px;
    border-color: #7E94CD;
    border-style: solid;
    border-radius: 5px;
}

.navbar-btn:hover {
    background-color: white;
    border: 3px;
    border-color:   #7E94CD;
    border-style: solid;
    color:  #7E94CD;
    transition-duration: .3s;
    border-radius: 5px;
}

.mobile-navbar {
    display:none;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;

}

@media only screen and (max-width: 450px) {
  .navbar {
    display:none;
    }
  .mobile-navbar {
    display:block;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .navbar {
    display:none;
    }
  .mobile-navbar {
    display:block;
    }
  }

</style>