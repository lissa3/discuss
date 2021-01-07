<template>
  <div class="container py-md-5 py-4">
    <!-- <p>{{profileInfo.first_name}}</p> -->
    <div class="row">
      <!-- <h1>Profile Details {{profile.unid}}</h1>        -->
       <div class="col col-md-10 py-2">
        <div class="card mb-3 p-2" style="width: 28rem;">
          <div class="card-body">             
             <p>Display name via store: {{showDisplayName}}</p>             
          <p class="text-mutated">(* will be visible on the website)</p> 
             <h5 class="card-title">               
                <a href="#" @click="goTo('ChangeDisplayName',profileInfo.unid)">
                  Change display Name: {{showDisplayName}}
                </a>
              </h5>           
          <h5 class="card-title">First Name: {{profileInfo.first_name}}</h5>           
          <h5 class="card-title" 
          >Last Name: {{profileInfo.last_name}}</h5>            
          <h5 class="card-title" v-if="profileInfo.website"
          >Web site: {{profileInfo.website}}</h5>
          <img v-if="profileInfo.image" :src="profileInfo.image" alt="profile image" class="idea-img mb-3">
          <hr>   
          <div class="d-flex flex-row justify-content-between ">
            <div class="p-2"><b-button @click="goTo('Home')">Home</b-button></div>
            
            <div class="p-2"><b-button variant="success" 
            @click="goTo('ChangeProfile',profileInfo.unid)">Change Profile</b-button></div>
          </div>              
                    
        </div>
      </div>
      </div>
    </div>  
  </div>
</template>

<script>

import {mapGetters} from 'vuex'
export default {
  
  name: 'ProfileDetail',
  data(){
      return {
        //unid:""
            //profile:JSON.parse(localStorage.getItem('profile')),
            // unid:this.$route.params.unid
        }    
  },
  methods:{
    goTo(direction,unid){
      this.$router.push({name:direction,params:{unid:unid}});      
    }

  }, 
  computed:{
    ...mapGetters(['profileInfo','showDisplayName']),
    
  },  
  created(){
       
    
    
  }
  
  
}
</script>