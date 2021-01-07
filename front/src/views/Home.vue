<template>
  
  <div class="container py-md-5 py-4">
    <div class="row">      
      <div class="col col-md-10 text-center">
      <h1>Welcome at our site</h1>
      <h2><router-link :to="{name:'Ideas'}"></router-link></h2>      
        
      <!-- <h2><a href="#" @click="goTo('Ideas')" >World of ideas rules the world</a></h2>  -->
      </div> 

      <div class="col col-md-10 text-center">
      <p>Status LoggedIn: {{logIn}}</p> 
      
      <!-- filter can be used if JWT present otherwise error  -->
      <!-- <p>Status LoggedIn: {{this.$store.state.currentJWT|shortText}}</p>       -->
      </div>
      <br>
      <div class="col col-md-10 py-2">
        <div class="card mb-3 p-2" style="width: 28rem;" v-for="idea in APIDataIdeas" :key="idea.id">
          <h5 class="card-title" >Title: {{idea.title}}</h5>                            

        </div>
      </div>
      <div class="col clo-md-10">
      <button class="btn btn-primary" @click="checkRT">Check refresh func</button>
      </div>
                       
      
    </div> 
    <div class="filling"></div> 
  </div>

</template>

<script>


import {mapGetters} from 'vuex'
import {getAPI} from '@/api/index';

export default {
  name: 'Home',
  data(){
    return {
      APIDataIdeas:[]
    }
  },  
  methods:{
    goTo(direction){
      this.$router.push({name:direction});
      },
      
    // checkRT(){	        
    //   return new Promise((resolve,reject)=>{
    //     let refr = localStorage.getItem('refresh_token');
    //     console.log("found refresh token",typeof(refr));
    //     simpleAPI.post('/auth/jwt/refresh/',{refresh:refr})        
    //     .then((response)=>{	  
    //       console.log(response)
    //       console.log("data in response:",response.data.access); 
    //       localStorage.setItem('access_token',response.data.access);
    //       resolve()
    //     })	  
    //     .catch((err)=>{	  
    //       console.log("of course there will be a error");	 
    //       console.log("error",err.non_field_errors);	  
    //       reject()	  
    //     })        	      
    //  })	  
    checkRT(){	
        let data = localStorage.getItem('refresh_token');
        let url = '/auth/jwt/refresh/';
        // console.log("found refresh token",refresh2);
        getAPI.post(url,{refresh:data})
        .then((resp)=>{
          console.log("resp",resp)
        })
        .catch((err)=>{
          console.log("error in checkRT",err);
          console.log("status:",err.response);
          console.log("status:",err.response.status);
          // localStorage.removeItem('access_token');
          // localStorage.removeItem('refresh_token');
          // localStorage.clear();
          if(err.response.status === 401){
            console.log("401 calling");
            // export const LOGIN = ()=>'/auth/jwt/create/';
            this.$router.push('/login')
          }
          else if(err.response.status ===400){
            // when refresh_token (var in LocalStorage null)
            console.log("stastus 400 calling")
          }

        })
      }
    },
    computed:{
      ...mapGetters(['showIdeas','logIn'])
    },
    created(){
    // TODO: what is the flow? 
    // to chain 2 req's? 
    // getAPI.get('/api/v1/ideas/')
    //     .then((resp)=>{	
    //         console.log("response:",resp)	            
    //         this.APIDataIdeas = resp.data;	            
                        
    //     })	        
    //     .catch(err=>{	        
    //         console.log("err",err)
    //     })	           

    //console.log("home calling , calling fetch in store");
    this.$store.dispatch('fetchIdeas');       
    },
    filters: {
      // TODO: only if value exists
      // shortText(value){           
      //   return value.slice(0,12);
      // }    
    }  
  
}
</script>
<style  scoped>
.idea-img{
  width:18rem;
}

</style>
