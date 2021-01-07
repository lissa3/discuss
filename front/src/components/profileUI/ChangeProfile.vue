<template>
  <div class="container py-md-5 py-4">
    <div class="row">
      <h1>Change your profile</h1> 
      <!-- <div class="long">       -->
       <div class="col col-md-10 py-2 long">
        <div class="card mb-3 p-2" style="width: 28rem;">
          <div class="card-body">
              <p>Here comes a form for {{unid}}</p> 
              
        </div>
      </div>
      </div>
    <!-- </div> -->
    </div>  
  </div>
</template>

<script>

import {mapGetters} from 'vuex'
export default {
  
  name: 'ChangeProfile',
  data(){
      return {
            profile:{},
            unid:this.$route.params.unid
            
        }    
  },
  methods:{
    goTo(direction){
      this.$router.push({name:direction});      
    }

  }, 
  computed:{
    ...mapGetters(['profileInfo']),
    
  },  
  created(){
    // this.$store.dispatch('user_info')
    // let stateToken = this.$store.state.currentJWT;
    // let load = `JWT ${token}`
    // const localStorageToken = localStorage.getItem('access_token');
    // console.log("fysical presence: access_token in Local Storage detected",localStorageToken);
    // console.log("currentJWT from the state store.js",stateToken);
    // headers to be add as a param to getAPI
    // {headers:{Authorization:`JWT ${this.$store.state.accessToken}`}})    
    
    
  }
  
  
}
</script>
<style scoped>
.long {
  min-height: 100vh;
}
</style>