<template>
  <div class="container py-md-5 py-4">
    <div class="row">
      <h1> Change Your Display name unid (via url params): {{unid}}</h1> 
      <p>profile info via getter: {{profileInfo}}</p>
       <p>profile unid: {{profileInfo.unid}}</p>   
       <div class="col col-md-10 py-2">       
       <b-form @submit.prevent="changeName">
            <div class="form-group">
              <label for= "display_name">
                Current display name:{{showDisplayName}}
                </label>        
              <b-form-input id="display_name" v-model="newDisplayName" type="text" required
              ></b-form-input>              
            </div>     
      <li v-for="err in message" :key="err" class="red">Error {{err}}</li>   
      <b-button type="submit" variant="success">Change</b-button>
     
      </b-form>
      <div class="wrap mt-3">
        <b-button type="" variant="primary">Back</b-button>
      </div>
        
      </div>
    </div>  
  </div>
</template>

<script>
import {getAPI} from '@/api/index'
import {mapGetters} from 'vuex'

export default {  
  name: 'ChangeDisplayName',
  data(){
      return {
            newDisplayName:"",
            message:"",
            unid:this.$route.params.unid,            
            userId:localStorage.getItem('userId'),
            profileId:null,
            //currentDisplayName:JSON.parse(localStorage.getItem('profile'))

                     
        }    
  },
  computed:{
    ...mapGetters(['showDisplayName','profileInfo']),
    
  },  
  methods:{
    goBack(direction){
      this.$router.push({name:direction});      
    },
    changeName(){     
        getAPI.put( `/api-profile/${this.userId}/`, {display_name:this.newDisplayName})
            .then(resp=>{
                this.$store.commit('SET_DISPLAY_NAME', resp.data.display_name);
                this.$router.push({name:"ProfileDetail"})
            })
            .catch((error)=>{
                console.log("err",error);
                console.log(error.responseJSON)

            })
    }

  }, 
    
}
</script>
<style scoped>
.wrap{

  display: flex;
  justify-content: center;
}
</style>
        
    
      

  
  