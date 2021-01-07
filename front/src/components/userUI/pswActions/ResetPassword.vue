<template>
  <div class="container py-md-5 py-4">
      <div class="row">
        <h1> Request Password Reset</h1>   
        <div class="col col-md-10 py-2">       
          <b-form @submit.prevent="resetPassword" novalidate>
            <div class="form-group">
              <label for= "email">Email:</label> 
              <b-form-input id="email" v-model.trim="email" type="email" required
                placeholder="Enter your email"
                :class="{'is-invalid warning': this.$v.email.$error}"            
                @blur="$v.email.$touch()">
              </b-form-input>
            </div> 
            <!-- front-side errors -->            
        <div v-if="emailRequired" class="red"
            >{{fieldRequired}} 
        </div>
        <div v-if="validEmail" class="red"
            >This field should be a valid email
        </div>  
            <!-- server side errors -->
            <div class="red">{{emailDoesNotExist}}</div>
            <ul>         
              <li v-for="err in message" :key="err" class="red">Error {{err}}</li>   
            </ul>
            <!-- end server side errors  -->
            <b-button type="submit" variant="success"
            :disabled="formInValid">Reset Password
            </b-button>
            <!-- front side Ok -->            
            <div class="pending-submision mt-3" v-if="submitStatus === 'PENDING'">Sending...</div> 
          </b-form>
          <div class="wrap mt-3">
            <b-button type=""  variant="light" @click="goTo('Home')">Back To Home</b-button>
          </div>           
      </div>
    </div>  
  </div>
</template>

<script>
import {getAPI} from '@/api/index'

// import {mapGetters} from 'vuex'
import {required,  email } from "vuelidate/lib/validators";

export default {  
  name: 'ResetPassword',
  data(){
      return {           
          email:"",
          submitStatus:null,
          message:"",          
          //front-side vars/errors
          fieldRequired:"This field is required",
          // server-side errors
          emailError:"",
          nonFieldErr:"",
          serverError:"",
          generalError:"",
          emailDoesNotExist:""
      }         
  },
  validations: {
    email: { required, email }       
  },  
  computed:{
      formInValid() {return this.$v.$invalid;},
      emailRequired(){return this.$v.email.$dirty&&!this.$v.email.required},
      validEmail(){return this.$v.email.$dirty&&!this.$v.email.email}
  },
  methods:{
    goTo(direction){
      this.$router.push({name:direction});      
    },
    resetPassword(){
      // send email to get a form for set a new password
      if(!this.$v.$invalid){         
        this.submitStatus = 'PENDING'
        }         
        const url = "/auth/users/reset_password/";
        getAPI.post( url, {"email":this.email})
            .then((resp)=>{              
                this.$store.state.emailPotentialUser = this.email;
                this.$router.push({ name: "Confirm" });
                console.log("response ", resp.status);    
                console.log("resp",resp.data);
                
              })              
            .catch((error) => {
            if(error.response.request.status === 400){        
            this.emailError = error.response.data.email;            
            this.nonFieldErr = error.response.data.non_field_errors;
            
            }else if(error.response.request.status === 500){
              this.serverError = "Server error. Please try again later"
            }
            else{
              this.generalError = "Something went wrong. Please try again later"
            }          
          });      
            
  },     

}
}
</script>

<style scoped>
.wrap{

   display: flex;
   justify-content: center;
 }
 
 </style>
        
    
      

  
  