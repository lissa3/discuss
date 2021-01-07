<template>
  
  <div class="container py-md-5 py-4">
    <div class="row">
      <h1>Search Results of Ideas</h1>
      <br>     
      
      <div class="col col-md-10 text-center">
      <p>Status LoggedIn: {{this.$store.state.currentJWT|shortText}}</p>
      <h2><a href="#" @click="goTo('Ideas')" >World of ideas rules the world</a></h2>       
      </div>
      <br>
      <hr>         
      <div class="col col-md-10 py-2" v-if="arr">
        <div class="card mb-3 p-2"  style="width: 28rem;" v-for="idea in arr" :key="idea.id">
          <div class="card-body">
          <h5 class="card-title" 
          >Title: {{idea.title}}</h5>
          <h5 class="card-title">Author: {{idea.owner_idea}}</h5>   
          <h5>Created: {{idea.created_at|filterDateTime}}</h5>       
          <p class="card-text">Description: {{idea.lead_text}}</p> 
          <img :src="idea.thumbnail" alt="image for idea" class="idea-img mb-3">       
           <a href="#" class="btn btn-primary" @click="goTo(idea.id)">More Details</a>          
        </div>
      </div>
    </div>
    <div class="col col-md-10 py-2" >
        <div v-if="!arr">Sorry, nothing found for your search</div>
    </div>  
    
    </div>  
  </div>

</template>

<script>


import {mapGetters} from 'vuex'
// import {mapGetters} from 'vuex'

function filterByValue(array, value) {
  return array.filter((data) =>  JSON.stringify(data).toLowerCase().indexOf(value.toLowerCase()) !== -1);
}

export default {
  name: 'IdeasSearch',
  data(){
      return {
          // term:this.$route.params.search,
          term:this.$store.getters.getLookUp,
          arr:[],
              
                
      }
  }, 
  methods:{
    goTo(id){
      this.$router.push({name:'IdeaDetail',params:{id:id}})
    }      
    
  },
  computed:{
    ...mapGetters(['getLookUp']),
    // getSearch(){    
    // return filterByValue(this.$store.getters.showIdeas,this.term);        
    // },   
  },
  created(){
    this.arr = filterByValue(this.$store.getters.showIdeas,this.term)
    
  },
  watch:{
      getLookUp(){
        this.arr = filterByValue(
          this.$store.getters.showIdeas,
          this.getLookUp
          )
      }
  },
  filters: {
    // Filter full date with (local+) time
    // 2020-07-23 20:41:43.833825
    filterDateTime(item) {
     let initialDate = new Date(item)
        return `
          ${initialDate.getDate()}.${initialDate.getMonth()}.${initialDate.getFullYear()} - ${initialDate.getHours()}:${initialDate.getMinutes()}`
    
        },
    shortText(value){           
      return value.slice(0,12)
    }    
  }   
  
  
}
</script>
      
        
<style  scoped>
body{
  background-color:rgb(226, 170, 101);
}
.idea-img{
  width:18rem;
}
</style>
