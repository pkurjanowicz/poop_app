<template>
    <div>
        <div class="navbar">
            <!-- router-link is actually linked to the router.js file -->
            <router-link to="/"><button class='navbar-btn'>Home</button></router-link>
            <router-link to="/toprated"><button class='navbar-btn'>Liked Poops</button></router-link>
            <router-link to="/shant"><button class='navbar-btn'>Who is Shant?</button></router-link>
            <router-link to="/poopstreak"><button class='navbar-btn'>Poop Streak</button></router-link>
        </div>
        <!-- <Slide class='mobile-navbar'>
            <a id="home" href="/"><span>Home</span></a>
            <a id="home" href="/toprated"><span>Liked Poops</span></a>
            <a id="home" href="/shant"><span>Who is Shant?</span></a>
            <a id="home" href="/poopstreak"><span>Poop Streak</span></a>
        </Slide> -->
        <Slide class='mobile-navbar'
          disableOutsideClick
        >
            <a @click='toggleShantSubMenu' id="home">
              <span>Shant</span>
                <div class='plus-minus-container'>
                  <span v-if='!shantSubMenuVisibile'>+</span>
                  <span v-if='shantSubMenuVisibile'>-</span>
                </div>
            </a>
              <div id="sub-menu-container" v-if='shantSubMenuVisibile'>
                <a id="sub-menu" href="/"><span>Status</span></a>
                <a id="sub-menu" href="/toprated"><span>Liked Poops</span></a>
                <a id="sub-menu" href="/shant"><span>Who is Shant?</span></a>
                <a id="sub-menu" href="/poopstreak"><span>Poop Streak</span></a>
              </div>
            <a @click='toggleProfileSubMenu' id="home">
              <span>Your Profile</span>
                <div class='plus-minus-container'>
                  <span v-if='!profileSubMenuVisibile'>+</span>
                  <span v-if='profileSubMenuVisibile'>-</span>
                </div>
            </a>
              <div id="sub-menu-container" v-if='profileSubMenuVisibile'>
                <a id="sub-menu" href="/"><span>Status</span></a>
                <a id="sub-menu" href="/toprated"><span>Liked Poops</span></a>
                <a id="sub-menu" href="/shant"><span>Profile</span></a>
                <a id="sub-menu" href="/poopstreak"><span>Poop Streak</span></a>
              </div>
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
    data() {
      return {
        shantSubMenuVisibile: false,
        profileSubMenuVisibile: false
      }
    },
    methods: {
      toggleShantSubMenu() {
        if (this.shantSubMenuVisibile == true) {
          this.shantSubMenuVisibile = false
        } else {
          this.shantSubMenuVisibile = true
        }
      },
      toggleProfileSubMenu() {
        if (this.profileSubMenuVisibile == true) {
          this.profileSubMenuVisibile = false
        } else {
          this.profileSubMenuVisibile = true
        }
    }
  }
}
</script>

<style scoped>

a {
  cursor: pointer;
}

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

#sub-menu {
  margin: 5px 30px;
  color: white;
  text-decoration: none;
}

#sub-menu-container {
  display:flex;
  flex-direction: column;
}

.plus-minus-container {
  float: right;
  width: 100%;
  justify-content:flex-end;
  display:flex;
}

.bm-item-list>* {
    padding: .9em;
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