<template>
    <div class="container">
         <div class="row">            
            <div class="col col-md-10" >
                <div class='container'>
                    <div class="wrapper">
                        <h1>Verify your Account:</h1>
                        <button  @click="activate" class="btn btn-success">                
                            Verify
                        </button>
                        </div>
                        <p v-if="errorMsg">Errors: {{errorMsg}}</p>
                    </div> 
            </div>
        </div>
    </div>
</template>
                        
<script>
// '@/components/userUI/pswActions/ChangePassword'
import {getAPI} from '@/api/index'
export default {
    name:"Activate",
    data(){
        return{
            errorMsg:""
        }
    },
    methods:{
        activate(){
            // get from url
            console.log("url router:",this.$router);
            console.log("url:",this.$route.params)
            let uid= this.$route.params.uid;
            let token = this.$route.params.token; 
            getAPI.post('/auth/users/activation/',{
                uid:uid,
                token:token
            })
            .then(resp=>{
                console.log(resp.status);
                // status == 204
                this.$router.push({name:"Login"});
            })
            .catch(err=>{
                console.log("err",err);
                this.errorMsg = err
            })   

        }
    }
}
</script>
