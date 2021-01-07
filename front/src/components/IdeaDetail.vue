<template>
  <div class="container py-md-5 py-4">
    <div class="row">
      <h1>Idea Details {{id}}</h1>
       <hr>   
           
      <div class="col col-md-10 py-2">
        <div class="card mb-3 p-2" style="width: 28rem;">
          <div class="card-body">
          <h5 class="card-title" 
          >Title: {{idea.title}}</h5>
          <h5 class="card-title">Author: {{idea.owner_idea}}</h5>   
          <h5>Created: {{idea.created_at}}</h5>       
          <h5>Created: {{idea.created_at|filterDateTime}}</h5>       
          <p class="card-text">Description: {{idea.lead_text}}</p>         
                    
          <a href="#" class="btn btn-primary" @click="goBack()" >
                    Back To Home 
          </a>          
        </div>
      </div>
      </div>
    </div>  
  </div>
</template>

<script>
import {getAPI} from '@/api/index';
import {IDEA_DETAIL} from '@/api/routes';



export default {
  name: 'IdeaDetail',
  data(){
      return {
            idea:{},
            id:this.$route.params.id
        }    
  },
  methods:{
    goBack(){
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/');
      // this.$router.push({name:"Home"});      
    }
  },   
  created(){    
      getAPI.get(IDEA_DETAIL(this.id))      
        .then(resp=>{
            this.idea = resp.data;
        })
        .catch(err=>{
            console.log("err",err);
        })    
    //async ()=>{
      //console.log("got waited response");
      //const resp = await getAPI.get(IDEA_DETAIL(this.id));
      //this.idea = resp.data;
        // .then(resp=>{
        //     this.idea = resp.data
        // })
        // .catch(err=>{
        //     console.log("err",err)
        // })    
    //}
  },  
  filters: {
    // Filter full date with (local+) time
    // 2020-07-23 20:41:43.833825
    filterDateTime(item) {
     let initialDate = new Date(item)
        return `
          ${initialDate.getDate()}.${initialDate.getMonth()}.${initialDate.getFullYear()} - ${initialDate.getHours()}:${initialDate.getMinutes()}`    
        }
  },  
  
}
</script>