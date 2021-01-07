<template>
<div class="container">
    <h1>Password Reset Confirmation</h1>
    <h4>Final Step SallySally200#</h4>
     <div class="col col-md-10 py-2"> 
        <b-form @submit.prevent="confirmPswReset" novalidate>
          <div class="form-group">
          <label for="newPsw" class="control-lable">New Password:</label>          
            <b-form-input 
                id="newPsw"
                type="password"
                v-model.trim="newPsw" placeholder="Enter password" autocomplete="off" 
                :class="{'is-invalid warning': this.$v.newPsw.$error}" 
                @blur="$v.newPsw.$touch()">                    
            </b-form-input>            
            <b-form-invalid-feedback v-if="validPswMinLen" class="invalid-feedback">password should at least {{$v.newPsw.$params.minLength.min}} chars
            </b-form-invalid-feedback>
            <b-form-invalid-feedback v-if="validPswMaxLen" class="invalid-feedback">password should at most {{$v.newPsw.$params.maxLength.max}} chars
            </b-form-invalid-feedback> 
            <b-form-invalid-feedback v-if="!pswRequired"  class="invalid-feedback">{{fieldRequired}}
            </b-form-invalid-feedback>         
        </div> <!-- end form-group for new password -->
        <!-- server password errors -->
          <div v-if="newPswError">
          <div class="alert alert-danger" role="alert" v-for="err in newPswError" :key="err.index" >
            <p>{{err}}</p>
            </div>
          </div>        
        <!--  front-side password errors custom validation-->  
        <ul class="mistake unstyled" v-if="$v.newPsw.$dirty&&correctPsw">            
              <li class="" v-for="note in correctPsw" :key="note.id">{{note}}</li>            
        </ul> 
        <div class="form-group">
          <label for="reNewPsw" class="control-lable"> Confirm Password:</label>          
          <b-form-input
                  id="reNewPsw"
                  v-model.trim="reNewPsw"
                  placeholder="Confirm  password"
                  type="password"
                  autocomplete="off" 
                  :class="{'is-invalid warning': this.$v.newPsw.$error}"  
                  @blur="$v.reNewPsw.$touch()"                          
                >
          </b-form-input>            
          <b-form-invalid-feedback
                v-if="$v.reNewPsw.$dirty&&!$v.reNewPsw.sameAs"
                class="invalid-feedback"
                >Passwords must be identical
          </b-form-invalid-feedback>          
        </div><!-- end div form-group re new password-->       
              
               
        <ul class="password-rules-main text-left text-rules"><span class="streep">Password should contain:</span>
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
            ><span class="">Both fields are required </span>         
          </li>
        </ul>           
        <b-button type="submit" variant="success" :disabled="formInValid">Reset Password
        </b-button>  
        </b-form>  
    </div>
</div>
      
            
    
</template>
<script>
import { getAPI } from '@/api/index';
import {required, minLength,  maxLength,  sameAs } from "vuelidate/lib/validators";
export default {
    name: 'ResetPasswordConfirm',
    data() {
      return {
        newPsw:"",
        reNewPsw:"",
        errMsg:"",
        newPswError:"",
        //front-side vars/errors
        fieldRequired:"This field is required",
        serverError:""
      }
    },
    validations: {
      newPsw: {
        required,
        minLength: minLength(8),
        maxLength: maxLength(128),
      },
      reNewPsw: {
        required,
        minLength: minLength(8),
        maxLength: maxLength(128),
        sameAs: sameAs('newPsw'),
      }
  },
  computed:{
      formInValid() {return this.$v.$invalid;},
      correctPsw(){
      const customErrors=[]
      if(!this.$v.newPsw.$dirty) return customErrors;
      !/(?=.*[A-Z])/.test(this.newPsw)&&customErrors.push("Your passsword should have a capital letter");
      !/(?=.*\d)/.test(this.newPsw)&&customErrors.push("Your password should have a digit")
      !/([!@$%#])/.test(this.newPsw)&&customErrors.push("Your password should have a special chars like !@$%#");
      return customErrors;
    },
    validPswMinLen(){return this.$v.newPsw.$dirty&&!this.$v.newPsw.minLength},
    validPswMaxLen(){return this.$v.newPsw.$dirty&&!this.$v.newPsw.maxLength},
    pswRequired(){return this.$v.newPsw.$dirty&&!this.$v.newPsw.required},
    

  },
    methods:{
      confirmPswReset(){
        console.log("final step to reset psw");
        // console.log("url router:",this.$router);
        // console.log("url:",this.$route.params)
        let uid= this.$route.params.uid;
        let token = this.$route.params.token;
        const newCreds={
          uid:uid,
          token:token,
          "new_password":this.newPsw,
          "new_re_password":this.reNewPsw
          }
      getAPI.post('/auth/users/reset_password_confirm/',newCreds) 
        .then((resp)=>{
          console.log(resp.status);
          // status == 204
          this.$router.push({name:"Login"});
        }) 
        .catch((err)=>{
          if(err.response.request.status === 500){
            this.errMsg= "Server error. Please try again later"
            }else{
            console.log("smth went wrong",err);
            this.errMsg = err;
          }
        })  
      }
    }   
}
</script>
<style scoped>
.text-rules{
  color:#315038;
}
.streep{
  text-decoration-line:underline;
}
</style>