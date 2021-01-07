<template>
<header class="bg-dark">

  <b-navbar toggleable="lg" type="dark" variant="dark" class="w-75 mx-auto">
    
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <b-navbar-nav>
        <b-nav-item href="#"><router-link :to="{name:'Home'}" class="link-decor">Home</router-link></b-nav-item>
        <b-nav-item href="#">
          <router-link :to="{name:'Ideas'}" class="link-decor">Ideas</router-link> </b-nav-item>
        <b-nav-item href="#"><router-link :to="{name:'About'}" class="link-decor">About</router-link>
          
          </b-nav-item>      
        <b-nav-item href="#" v-if="!logIn"><router-link :to="{name:'Login'}" class="link-decor">Log In</router-link></b-nav-item>        
        <b-nav-item href="#" v-if="!logIn"><router-link class="link-decor" :to="{name:'SignUp'}">Sign Up</router-link></b-nav-item>
        <!--  -->
         <!-- <b-nav-item href="#" v-if="logIn" @click="goTo('Logout')">Logout</b-nav-item>  -->
        <b-nav-item href="#" v-if="logIn"><router-link class="link-decor" :to="{name:'Logout'}">Logout</router-link></b-nav-item>
        <b-nav-item href="#">Welcome:{{showDisplayName}}</b-nav-item>
        <!-- <b-nav-item href="#">Welcome:{{profileInfo.display_name}}</b-nav-item> -->


      </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">        
        <b-nav-item-dropdown right v-if="logIn" >
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>Dashboard</em>
          </template>
          <b-dropdown-item href="#">Manage your ideas</b-dropdown-item>
          <b-dropdown-item href="#" @click="showMe()" v-if="logIn">Profile</b-dropdown-item>
          <!-- debug condition -->
          <b-dropdown-item href="#" @click="goTo('ChangePassword')" v-if="logIn">Change password</b-dropdown-item>
          <b-dropdown-item href="#" v-if="logIn">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-form  @submit.prevent="searchRequest">
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model.trim="term" ></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>
        <!-- <b-nav-form  @submit.prevent="searchRequest">
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model.trim="term" ></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form> -->
      </b-navbar-nav>
    </b-collapse>    
  </b-navbar>
</header>
</template>

<script>

import {mapGetters} from 'vuex'

export default {
    name:"Menu",    
    data(){
      return{      
          login:false ,
          term:"",
          curUser:""         
      }
    }, 
    computed: {
      ...mapGetters(['logIn','profileInfo','showDisplayName'])
    },      
    
    methods:{  
      goTo(direction){
        // console.log("going direction",direction);      
        this.$router.push({name:direction});
      },
      showMe(){
        // todo: re-direct to profile detail (with ready to go data in store)
        // console.log('showing user info and profile');
        this.$store.dispatch('getUserInfo');
        // console.log("sent to getuserinfo func to fetch data")
        //let userId = localStorage.getItem('userId');
        //console.log("found userId",userId,"starting with promise to get profile");
        //this.$store.dispatch('getProfile',{userId});
        this.$router.push({name:"ProfileDetail"}) 
      },
      reLoader(){
        window.location='/'
      },
      
      searchRequest(){
        // no request to dj backend; user existing qs from store              
        this.$store.commit('SET_LOOK_UP',this.term);                
        this.$router.push({name:'IdeaSearch'}); 
        this.term = "";         
        
        
      }
    } 
}   
  

</script>
<style scoped>
.navbar,.navbar-brand{
  font-size: 16pt;
}
.link-decor{
  color:rgba(255,255,255,.5);
  text-decoration: none;

}
</style>

