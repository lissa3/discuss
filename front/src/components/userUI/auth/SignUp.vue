<template>
  <div class="container">
    <div class="w-50 mx-auto border p-3 rounded mb-3">
      <h5>SignUp via Google</h5>    
       <b-button @click="googleGo()" variant="danger">
          Continue with Google
        </b-button>
    </div>
    <div class="w-50 mx-auto border p-3 rounded">
      <b-form @submit.prevent="signUp" novalidate>
        <h5>SignUp with Email and Password</h5>
        <div class="form-group required">
          <label for="email" class="control-lable">Email:</label>
          <b-form-input  id="email"  v-model.trim="email" type="email"            
          autocomplete="off" required autofocus="autofocus" placeholder="Enter email"
          :class="{'is-invalid warning': this.$v.email.$error}"            
          @blur="$v.email.$touch()"
            ></b-form-input>
           <!--server-side errors  -->
          <div v-if="emailError">
            <div class="alert alert-danger" role="alert" v-for="err in emailError" :key="err.index" >
              <p>{{err}}</p>
            </div>
          </div>  
          <!-- front-side errors -->
          <b-form-invalid-feedback v-if="emailRequired" class="invalid-feedback"
            >{{fieldRequired}} </b-form-invalid-feedback>
            <b-form-invalid-feedback v-if="validEmail" class="invalid-feedback"
            >This field should be a valid email</b-form-invalid-feedback>  
        </div>          
        <div class="form-group required">
          <label for="password" class="control-lable">Password:</label>
          <div class="row border">
            <div class="col-md-10 border-0">
          <b-form-input id="password"  v-model.trim="password" required placeholder="Enter password" autocomplete="off" 
          class="form-control border-0"  :type="showPassword?'text':'password'"
          @blur="$v.password.$touch()"
            :class="{'is-invalid warning': this.$v.password.$error}"
          >
          </b-form-input>
            </div>
            <div class="col-md-2 border-0 pt-1">
            <span><b-icon-eye @click="toggleShowPws"/></span> 
            </div>
          </div>
          
        </div> 
        <ul class="password-rules-main">Password should contain:
          <li class="password-rules">
            at least {{$v.password.$params.minLength.min}} chars
          </li>
          <li class="password-rules">at least one capital letter: (A-Z)
          </li>
          <li class="password-rules" >at least one digit: 0-9
          </li>
          <li class="password-rules">at least one special character: ! @ $ % #
          </li>
          
          <li class="password-rules mt-2"
            >Fields marked as <span class="text-danger">*</span> are
            required          
        </li>
        </ul> 
        <!-- server password errors -->
          <div v-if="pswError">
          <div class="alert alert-danger" role="alert" v-for="err in pswError" :key="err.index" >
            <p>{{err}}</p>
            </div>
          </div>
          <!-- front-side password errors -->
          <ul class="mistake" v-if="$v.password.$dirty&&correctPsw">           
              <li class="" v-for="note in correctPsw" :key="note.id">{{note}}</li>            
          </ul>
          <b-form-invalid-feedback v-if="validPswMinLen" class="invalid-feedback"
            >password should at least {{$v.password.$params.minLength.min}} chars</b-form-invalid-feedback>
          <b-form-invalid-feedback v-if="validPswMaxLen" class="invalid-feedback"
            >password should at most {{$v.password.$params.maxLength.max}} chars
          </b-form-invalid-feedback>
          <b-list-group class="mistake" v-if="checkSimilar">           
              <b-list-group-item>{{checkSimilar}}</b-list-group-item>            
          </b-list-group>              
                  
        <div class="form-group required">
          <label for="rePsw" class="control-lable"
            >Repeat password,please:</label
          >
          <b-form-input
            id="rePsw"
            v-model.trim="rePsw"
            placeholder="Confirm  password"
            type="password"
            autocomplete="off"  
            @blur="$v.rePsw.$touch()"
            :class="{'is-invalid warning': this.$v.rePsw.$error}"        
          >
          </b-form-input>
          <!-- front-side rePsw errors -->
          <b-form-invalid-feedback
            v-if="$v.rePsw.$dirty &&!$v.rePsw.sameAs"
            class="invalid-feedback"
            >Passwords must be identical
          </b-form-invalid-feedback>          

        <!-- server non field errors: psw don't match -->          
        <div v-if="nonFieldErr">
          <div class="alert alert-danger" role="alert" v-for="err in nonFieldErr" :key="err.index">
            <p>{{err}}</p>
            </div>
        </div> 
        <!-- server error: status 500 -->
        <div v-if="serverError">
          <div class="alert alert-danger" role="alert">
            <p>{{serverError}}</p>
            </div>
        </div> 
        <!-- another server error -->
        <div v-if="generalError">
          <div class="alert alert-danger" role="alert">
            <p>{{generalError}}</p>
            </div>
        </div> 
      </div>  
      <div class="form-group required">        
        <b-form-checkbox
            id="checkbox-1"
            v-model="status"
            name="checkbox-1"
            value="accepted"
            unchecked-value="not_accepted"
            class="control-lable"         
            @blur="$v.state.$touch()">
            I accept the rules
          </b-form-checkbox>
          <div>State now: <strong>{{ status }}</strong></div>         
      </div>        
      <!-- button  Submit   -->      
        <b-button type="submit" variant="success"
        :disabled="formInValid" >
          Sing Up
        </b-button>        
         <!--may be to delete because button will be disabled at this point  -->
        <p class="mistake" v-if="submitStatus === 'FORM_ERROR'">Please fill the form correctly.</p>
        <p class="mistake" v-if="submitStatus === 'SERVER_ERROR'">SORRY, THERE IS A SERVER ERROR</p>
        <!-- <p class="mistake" v-if="submitStatus === 'CONNECTION_ERROR'">SORRY, THERE IS A SERVER ERROR</p> -->
        <p class="pending-submision" v-if="submitStatus === 'PENDING'">Sending...</p> 
        </b-form>
      <p class="mt-3">
        Already have an account? <router-link to="/login">Login</router-link>
      </p>
      <hr />
      <small id="emailHelp" class="form-text text-muted"
        >We'll never share your email with anyone else.</small
      >
    </div>
  </div>
</template>      
              
        
<script>
import { getAPI,getApiFormIncoded } from "@/api/index";
import {required,  email,  minLength,  maxLength,  sameAs } from "vuelidate/lib/validators";

   
export default {
  name: "SignUp",
  data() {
    return {
      email: "",
      password: "",
      rePsw: "",
      // user agree with terms and use
      status: 'not accepted',
      giveFeedback:false,
      // toggle password visiabilty
      showPassword:false,
      //front-side vars/errors
      fieldRequired:"This field is required",
      submitStatus:null, 
      // server-side errors
      emailError:'',     
      pswError: null,
      nonFieldErr:null,
      serverError:null,
      generalError:null    
    }
  },
  validations: {
    email: { required, email },
    // status:{required},    
    password: {
      required,
      minLength: minLength(8),
      maxLength: maxLength(128),
    },
    rePsw: {
      required,
      minLength: minLength(8),
      maxLength: maxLength(128),
      sameAs: sameAs("password"),
    },
  },
  computed:{
    formInValid() {
      return this.$v.$invalid||!this.checkSelected;
    },
    correctPsw(){
      const customErrors=[]
      if(!this.$v.password.$dirty) return customErrors;
      !/(?=.*[A-Z])/.test(this.password)&&customErrors.push("Your passsword should have a capital letter")
      !/(?=.*\d)/.test(this.password)&&customErrors.push("Your password should have a digit")
      !/([!@$%#])/.test(this.password)&&customErrors.push("Your password should have a special chars")

      return customErrors;
    },
    checkSimilar(){
      let lookLike = "";
      if(!this.$v.password.$dirty) return lookLike;
      const head = this.email.split('@',1)[0];
      console.log("found first part",head);
      // if ( this.password.includes(head) >= 0){
      if ( this.password.toLowerCase().indexOf(head) >= 0){
        lookLike = "Email and password are too similar"
        return lookLike;
      }else{
        return lookLike;
      }
    },
    checkSelected(){
      return this.status=="accepted"; 
    },
    emailRequired(){return this.$v.email.$dirty&&!this.$v.email.required},
    validEmail(){return this.$v.email.$dirty&&!this.$v.email.email},
    pswRequired(){return this.$v.password.$dirty&&!this.$v.password.required},
    validPswMinLen(){return this.$v.password.$dirty&&!this.$v.password.minLength},
    validPswMaxLen(){return this.$v.password.$dirty&&!this.$v.password.maxLength},
    
    },
  methods: {
    toggleShowPws(){
            this.showPassword = !this.showPassword;
        },    
    signUp() {
        console.log("signup clicked");
        this.$v.$touch()        
          if(this.$v.$invalid){
            this.submitStatus = 'ERROR'
          }else{
          this.submitStatus = 'PENDING'        
          
          const creds = {
              email: this.email,
              password: this.password,
              rePsw: this.rePsw
          }        
          this.$store.dispatch('userSignUp',creds)
          .then((resp) => {
            console.log("from then method SignUp.vue resp", resp); 
              if(resp.status ===201){
                this.$router.push({ name: "Confirm" });
              }else if(resp.status ===400){          
                console.log("server response status 400");
                this.emailError = resp.emailErr;            
                this.pswError = resp.pswErr;            
                this.nonFieldErr = resp.nonFieldErr;
                this.submitStatus = 'ERROR'
              }else if(resp.status === 401){
                // unauth request, url misused
                this.generalError = "Something went wrong.Unauthorized request."
                this.submitStatus = null;             
              }else if(resp.status === 404){
                // unauth request, url misused
                this.$router.push({name:"notFound"})              
              }else if(resp.status===500){
                console.log("server error 500")
                this.serverError = "Server error.Something went wrong"
              }else{
                console.log("Server can't be reached)");
                // this.submitStatus = 'SERVER_ERROR'              
                this.generalError = "Something went wrong.Please check your internet connection and try again later"
              }                       
              
            })
          .catch((error) => {
            console.log("catch SignUp error",error); 
            this.submitStatus = null;  
            // if django server (of npm run (?) problem) unresponsive|=> general error     
            this.generalError = "Something went wrong.Server connection problem.Please try again later";          
            });      
          }
        },
    googleGo(){
       getAPI.get('/auth/o/google-oauth2/?redirect_uri=http://localhost:8000')
       .then((resp)=>{
        console.log("greet from google",resp.data.authorization_url);        
        window.location.replace(resp.data.authorization_url);
        let initStr = window.location.search.substring(1);  
        console.log("cut [1] from server response",initStr)
        // let myUrl = resp.data.authorization_url.split("?")[1]    
        let params = new URLSearchParams(initStr);
        console.log("state",params.get("state"));
        console.log("code",params.get("code"));
        let state = params.get("state");
        let code = params.get("code");        
        const rawDetails = {'code':code,'state':state};
        console.log("details",rawDetails);
        const formBody = Object.keys(rawDetails).map(key=>
        encodeURIComponent(key) +"="+encodeURIComponent(rawDetails[key])).join('&');
        console.log("formBody",formBody);       
        return getApiFormIncoded.post(`http://127.0.0.1:8000/auth/o/google-oauth2/?${formBody}`)
        
      })
      .then((resp)=>{
            console.log("success",resp.data);
            console.log("total resp",resp);
          })
      .catch((err)=>{
            console.log("err from ",err);
            this.$router.push({name:"AuthFailed"}) 
       }) ;        
       
    }
   
  }
}

</script>

<style scoped>
.form-group.required .control-lable::after {
  content: " *";
  color: red;
}
.red{
  color:red;
}
.warning {
  background-color:#f1cfcfa1;
}
.mistake{
  color:red;
  text-align: left;
  font-size: 0.8rem;
}
.ok-submit{
  color:green;
}
.pending-submision{
  color:blue;
}
.password-rules{
  text-align: left;
  font-size: 0.8rem;
}
.password-rules-main{
  background-color: beige;
  padding-bottom: 1rem;
}

</style>


        