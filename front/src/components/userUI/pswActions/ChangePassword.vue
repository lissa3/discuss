<template>
  <div class="container py-md-5 py-4">
    <h1>Hi, user {{showDisplayName}}</h1>
    <div class="row">
        <h1> Change Your Password</h1>   
        <div class="col col-md-10 py-2"> 
          <!-- start wrapper for the form -->
          <div class="change-psw-form">      
              <b-form @submit.prevent="changePsw" novalidate>
                  <div class="form-group">
                      <label for= "currentPsw">Current Password:</label> 
                      <b-form-input id="currentPsw" v-model.trim="currentPsw" type="password" 
                      placeholder="Enter your current password"
                      :class="{'is-invalid warning': this.$v.currentPsw.$error}"            
                      @blur="$v.currentPsw.$touch()"></b-form-input>
                  </div>
                  <div class="form-group">
                      <label for= "newPsw">New password:</label>        
                      <b-form-input id="newPsw" v-model.trim="newPsw" type="password" 
                       placeholder="Enter a new password"
                       :class="{'is-invalid warning': this.$v.newPsw.$error}"            
                      @blur="$v.newPsw.$touch()">
                      </b-form-input>
                  
                  <!--  front-side password errors -->  
                   <ul class="mistake unstyled mt-2" v-if="$v.newPsw.$dirty&&correctPsw">           
                        <li class="" v-for="note in correctPsw" :key="note.id">{{note}}</li>            
                  </ul>                  
                    <b-form-invalid-feedback v-if="$v.newPsw.$dirty&&!$v.newPsw.minLength" class="invalid-feedback"
                      >password should at least {{$v.newPsw.$params.minLength.min}} chars
                   </b-form-invalid-feedback>
                   <b-form-invalid-feedback v-if="$v.newPsw.$dirty&&!$v.newPsw.maxLength" class="invalid-feedback"
                      >password should at most {{$v.newPsw.$params.maxLength.max}} chars
                    </b-form-invalid-feedback> 
                    <b-form-invalid-feedback v-if="!$v.newPsw.required"
                    class="invalid-feedback">{{fieldRequired}}
                  </b-form-invalid-feedback>
                  
                  </div>
                  <div class="form-group">
                        <label for= "reNewPsw">Repeat new password:</label>        
                        <b-form-input id="reNewPsw" v-model.trim="reNewPsw" type="password" placeholder="Repeat new password"
                        :class="{'is-invalid warning': this.$v.reNewPsw.$error}"            
                        @blur="$v.reNewPsw.$touch()">
                        </b-form-input>
                        <b-form-invalid-feedback
                        v-if="$v.reNewPsw.$dirty &&!$v.reNewPsw.sameAs"
                        class="invalid-feedback"
                        >Passwords must be identical
                      </b-form-invalid-feedback>
                  </div>               
                <ul class="unstyled">
                   <!-- render server side errors  -->
                  <li v-for="err in serverErrMsg" :key="err" class="red">Error {{err}}</li> 
                </ul>                          
                <b-button type="submit" variant="success" :disabled="formInValid">Submit change</b-button>
            </b-form>
        </div> <!--end wrapper for the form -->
        <ul class="password-rules-main mt-3">Password should contain:
          <li class="password-rules">
            at least {{$v.newPsw.$params.minLength.min}} chars
          </li>
          <li class="password-rules">at least one capital letter: (A-Z)
          </li>
          <li class="password-rules" >at least one digit: 0-9
          </li>
          <li class="password-rules">at least one special character: ! @ $ % #
          </li>          
          <li class="password-rules mt-2"
            ><span class="text-info">All fields are required  </span>        
          </li>
        </ul>     
      <div class="wrap mt-3">
        <b-button type="" variant="primary" @click="goTo('Home')">Back To Home</b-button>
      </div>
        
      </div>
    </div> 
  </div> 
</template>

<script>
import {getAPI} from '@/api/index'
import {mapGetters} from 'vuex'
import {required, minLength,  maxLength,  sameAs } from "vuelidate/lib/validators";

export default {  
   name: 'ChangePassword',
  data(){
      return {           
          currentPsw:"",
          newPsw:"",
          reNewPsw:"",
          //front-side vars/errors
          fieldRequired:"This field is required",
          serverErrMsg:[]                     
        }    
  },
   computed:{
      formInValid() {
        return this.$v.$invalid;
        },
      correctPsw(){
          const customErrors=[]
          if(!this.$v.newPsw.$dirty) return customErrors;
          !/(?=.*[A-Z])/.test(this.newPsw)&&customErrors.push("Your passsword should have a capital letter");
          !/(?=.*\d)/.test(this.newPsw)&&customErrors.push("Your password should have a digit")
          !/([!@$%#])/.test(this.newPsw)&&customErrors.push("Your password should have a special chars");
          return customErrors;
     },
     ...mapGetters(["showDisplayName"])
       
   },
  validations: {
    currentPsw: { required },
    newPsw: {
      required,
      minLength: minLength(8),
      maxLength: maxLength(128),
    },
    reNewPsw: {
      required,
      minLength: minLength(8),
      maxLength: maxLength(128),
      sameAs: sameAs("newPsw"),
    },
  },  
  methods:{
     goBack(direction){
      this.$router.push({name:direction});      
    },
     changePsw(){
       const payload = {
            "current_password":this.currentPsw,
            "new_password":this.newPsw,
            "re_new_password":this.reNewPsw
            };
        const url = "/auth/users/reset_password/"; 
        // const url = "/auth/users/set_password/"; 
        getAPI.post( url, payload)
            .then((resp)=>{
              console.log("status resp 204 (created)?",resp.status);
                // this.$store.commit('SET_DISPLAY_NAME', resp.data.display_name);
                this.$router.push({name:"ProfileDetail"});
            })
            .catch((error)=>{
                console.log("err",error);
                // this.serverErrMsg = error;# nasty looking error (don't render it as raw) ;
                this.serverErrMsg.push("server error: something went wrong!");
                console.log(error.data);

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
        
    
      

  
  