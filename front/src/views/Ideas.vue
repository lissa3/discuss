<template>
  
  <div class="container py-md-5 py-4">
    <div class="row">
      <h1>All Ideas</h1>
      <br>     
      
      <div class="col col-md-10 text-center">
      <p>Status LoggedIn: {{logIn}}</p>
      <!-- filter if only JWT present -->
      <!-- <p>Status LoggedIn: {{this.$store.state.currentJWT|shortText}}</p> -->
      </div>
      <br>
      <hr>            
      <div class="col col-md-10 py-2">
        <div class="card mb-3 p-2" style="width: 28rem;" v-for="idea in showIdeas" :key="idea.id">
          <div class="card-body">
          <h5 class="card-title" 
          >Title: {{idea.title}}</h5>
          <h5 class="card-title">Author: {{idea.owner_idea}}</h5>   
          <h5>Created: {{idea.created_at}}</h5>       
          <h5>Created: {{idea.created_at|filterDateTime}}</h5>       
          <p class="card-text">Description: {{idea.lead_text}}</p> 
          <img :src="idea.thumbnail" alt="image for idea" class="idea-img mb-3">        
                    
          <a href="#" class="btn btn-primary" @click="goTo(idea.id)">
                    More Details
          </a>          
        </div>
      </div>
      </div>
    </div>  
  </div>

</template>

<script>


// import {mapGetters} from 'vuex'
import {mapGetters} from 'vuex'

export default {
  name: 'Ideas', 
  computed:{
    ...mapGetters(['showIdeas','logIn']), 
    // filterIdeas(){
    //   let = this.$store.APIDataIdeas.filter()
    // }   
  },
  methods:{
    goTo(id){
      this.$router.push({name:'IdeaDetail',params:{id:id}})
    }  
    
  },
  created(){
    this.$store.dispatch('fetchIdeas')
    // let token = this.$store.state.accessToken    
    // {headers:{Authorization:load}}
    // headers to be add as a param to getAPI
    // {headers:{Authorization:`JWT ${this.$store.state.accessToken}`
    // getAPI.get('/api/v1/ideas/',{headers:{Authorization:`JWT ${this.$store.state.accessToken}`}})
    //     .then(resp=>{
    //         this.$store.state.APIDataIdeas = resp.data
    //     })
    //     .catch(err=>{
    //         console.log("err",err)
    //     })
    
  },
  filters: {
    // Filter full date with (local+) time
    // 2020-07-23 20:41:43.833825
    filterDateTime(item) {
      // console.log("item is",item);
      // console.log("date",new Date(item).getDate());
      // console.log("month",new Date(item).getMonth());
      // console.log("month",new Date(item).getFullYear());

     let initialDate = new Date(item)
        return `
          ${initialDate.getDate()}.${initialDate.getMonth()}.${initialDate.getFullYear()} - ${initialDate.getHours()}:${initialDate.getMinutes()}`
    
        },
    shortText(value){           
      return value.slice(0,12)
    }    
  },  
 
  
}
</script>
<style  scoped>
body{
  background-color:bisque;
}
.idea-img{
  width:18rem;
}
</style>
