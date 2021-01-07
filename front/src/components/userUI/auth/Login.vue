<template>
<div class="w-25 mx-auto border p-3 rounded">
    <div>
        <p>SallySally20#</p>
        <p v-if="netWorkIssue" class="red">Sorry.Network problem.Please try again later.</p>
        <p v-if="alertServMsg" class="red">Server.error.Please try again later.</p>
        <p v-if="finalErr" class="red">Sorry.Something went wrong, Try again please.</p>
        <p v-if="alertForUser" class="red" >Incorrect email or password entered - please try again</p>
        <p v-if="alertEmailConf" class="email-confirm-warning">Have you confirmed your email address after sign-up?</p>        
    </div>    
      
    <b-form @submit.prevent="setLogin" >
      <div class="form-group">
          <label for= "email">Email:</label>        
          <b-form-input id="email" v-model.trim="email" type="email" required
            placeholder="Enter email"
            :class="{'is-invalid warning': this.$v.email.$error}"            
          @blur="$v.email.$touch()"></b-form-input>
        </div>
        <!-- front-side errors -->
        <div v-if="emailRequired" class="red"
            >{{fieldRequired}} 
        </div>
        <div v-if="validEmail" class="red"
            >This field should be a valid email
        </div>  
        <div class="form-group">
            <label for="password">Password:</label>          
            <div class="row border" :class="{'is-invalid warning': this.$v.password.$error}">
                <div class="col-md-10 border-0">
                <b-form-input id="password" class="form-control border-0" 
                :class="{'is-invalid warning': this.$v.password.$error}"
                v-model.trim="password" required  placeholder="Password" :type="showPassword?'text':'password'" 
                @blur="$v.password.$touch()">  
                </b-form-input>
                </div>
                <div class="col-md-2 border-0 pt-1">
                    <span><b-icon-eye @click="toggleShowPws" 
                    /></span>                     
                </div>                
            </div>
            <!-- front-side errors -->
            <div v-if="pswRequired" class="red"
            >{{fieldRequired}} </div>
            <div v-if="validPswMinLen" class="red"
            >password should at least {{$v.password.$params.minLength.min}} chars</div>
          <div v-if="validPswMaxLen" class="red"
            >password should at most {{$v.password.$params.maxLength.max}} chars
          </div> 
      </div>
      <b-button type="submit" variant="success"
      :disabled="formInValid"
      >Log In</b-button>
      <p class="mistake" v-if="submitStatus === 'ERROR'">Please fill the form correctly.</p>
      <p class="pending-submision" v-if="submitStatus === 'PENDING'">Sending...</p> 
      <li v-for="err in message" :key="err" class="red">Error {{err}}</li>  
     
    </b-form>
    <p class="mt-3">Not registed? 
        <span class="mute-link"><router-link to="/signup">Sign Up</router-link></span>
    </p>
    <p class="mt-3">Forgot yout password? 
        <span class="mute-link"><router-link to="/reset-password">Here</router-link></span>
    </p><br> <br><br> 
    
    
    
</div> 
 
    
</template>
<script>

import {required,  email,  minLength,  maxLength } from "vuelidate/lib/validators";
// import {mapGetters} from 'vuex';


export default {
    name:"Login",
    data(){
        return {
            password:"",
            email:"",
            //front-side vars/errors
            fieldRequired:"This field is required",  
            submitStatus:null,           
            // "eye for pws input"           
            showPassword:false, 
            // server-side errors (errors 401,500,general)
            // if user.is_active = false(no email confirm/banned/account deleted) ==401
            customIncorrect:false,
            alertForUser:false,
            alertServMsg:false,
            netWorkIssue:false,
            finalErr:false,
            alertEmailConf:"",
            message:"",// ? do you need it
            emailError:"",
            pswError:"",
            nonFieldErr:"",
            serverError:"",// check it again to be used
            generalError:""
        }
    },
    validations: {
    email: { required, email },
    password: { required,minLength: minLength(8),maxLength: maxLength(128)},
    
   },  
    methods:{ 
        //  ...mapGetters(['getIsNotActive']),
        toggleShowPws(){
            this.showPassword = !this.showPassword
        },
        setLogin(){
            console.log("login clicked");
            this.$v.$touch()      
        if(this.$v.$invalid){
         this.submitStatus = 'ERROR';
        }else{
        this.submitStatus = 'PENDING';
        
        this.$store.dispatch('userLogin', {
          email:this.email,
          password:this.password               
          })
          .then((resp)=>{
              console.log("login then(success) response",resp);
              console.log("login then resp status",resp.status);
              // case when dj server DOWN and sends no response at all!
              if(resp.status==="pass"||resp.specialMsg==="network problem"){
                  this.netWorkIssue = true;
              }else if(resp.status===200){
                  this.$router.push({name:"Home"})
              }else if(resp.status === 401){
                  // specialMsg == resp djoser in case of 401
                  console.log("401?",resp.status)
                  this.alertForUser = true;
                  this.alertEmailConf = resp.specialMsg;
              }else if(resp.status===500) {
                  this.alertServMsg = true;
                  
              }else{
                  this.finalErr = true;
                  console.log(resp);
              }

           })
          .catch((error)=>{ 
              this.finalErr = true;
              console.log("last catch of error",error) ;
                      
            })            
        }      
    }
    },
    computed:{        
        formInValid(){return this.$v.$invalid;},
        validPswMinLen(){return this.$v.password.$dirty&&!this.$v.password.minLength},
        validPswMaxLen(){return this.$v.password.$dirty&&!this.$v.password.maxLength},
        pswRequired(){return this.$v.password.$dirty&&!this.$v.password.required},
        emailRequired(){return this.$v.email.$dirty&&!this.$v.email.required},
        validEmail(){return this.$v.email.$dirty&&!this.$v.email.email},
        // isNotActive(){return this.getIsNotActive();}    
    },
}
//   console.log("err login.vue:",error.response.data.detail);
            // console.log("The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.");
            // console.log("err dir",error.response.status) 
</script>

<style>
.red{
    color:red;
}
.warning {
  background-color:#f1cfcfa1;
}
.email-confirm-warning{
    color:#106d25;
}
.mistake{
  color:red;
  text-align: left;
  font-size: 0.8rem;
}
.small-font{
    font-size: 0.7rem;
    padding-left: 0.7rem;
}
.mute-link a{
    color:#e0ac5e;  
    text-decoration: none;  
}
.mute-link a:hover {
    color:#ef9816;
    text-decoration: none; 
}
</style>
