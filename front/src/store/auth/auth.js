// import {IDEAS,TOKEN_REFRESH,GET_USER_INF, LOGIN,} from '@/api/routes';
import {TOKEN_REFRESH,LOGIN,SIGN_UP} from '@/api/routes';
import {getAPI} from '@/api/index';
import router from '@/router';

// import {getAPI,goSignUp} from '@/api/index';


export default{
    state:{
        currentJWT:localStorage.getItem('access_token')||"",
        refreshJWT:localStorage.getItem('refresh_token')||"",
        currentUserIdLocalStorage:localStorage.getItem('userId')||'',
        currentUserId:'',
        emailPotentialUser:'',
        logout:true,
        // TODO: track status(may be it's useless?)
        status:'',        
        isNotActive:false

    },
    getters:{
        logIn(state){return state.currentJWT;},
        getUserInfo(state){return state.currentUserId;},
        showEmailPotentUser(state){return state.emailPotentialUser;}, 
        userNotActive(state){return state.msgUserNotActive;},
        getIsNotActive(state){return state.isNotActive;},
        getRefreshJWT(state){return state.refreshJWT;}

    },
    mutations:{
        SET_USER_ID(state,userId){state.currentUserId = userId;},
        LOGIN_SUCCESS(state,jwt){ 
          console.log("setting current JWT and loggedIn");     
          state.currentJWT = jwt;
          state.status="succes";      
        },
        LOGIN_ERROR(state){
          state.status = "error";
          state.isNotActive = true;
          
        },
        DESTROY_TOKEN(state){
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            // state.loggedIn = false; 
            state.currentJWT=""; 
            state.status="";     
          },
        PASS_EMAIL_POTENTIAL_USER(state,email){
            state.emailPotentialUser = email;
          }

    },
    actions:{
      // danger!!!! WHILE LOOP это функция крутится до упада|=> set debug on line 75 s.v.p
      async refreshToken({commit}){
        try{
          console.log("need new access token, trying with refrsh");
          let refresh2 =localStorage.getItem('refresh_token');
          const resp = await getAPI.post(TOKEN_REFRESH(),{          
          // getAPI.post('/auth/jwt/refresh/',{          
            refresh:refresh2
          })
          console.log("auth.js response",resp);
          console.log("asked for access token using refresh");
          console.log("got it",resp.data.access);
          localStorage.setItem('access_token',resp.data.access);
          commit('LOGIN_SUCCESS',resp.data.access);         
            
        }
        catch(err){             
          console.log("err",err);
          router.push("/login")
          if(err.non_field_errors){
            console.log("err.non field",err.non_field_errors);
          }
        }             
      },
      async userLogin({commit},usercredentials){
          // servResp collects status + possible errors
          // and gets passed to Login.vue promise via return
          // if status === 200 |=> localStorage JWT and errors=empty
          let servResp = {
            emailErr:[],
            pswErr:[],
            nonFieldErr:[],
            status:"",
            specialMsg:""
          }
           try{
              const resp = await getAPI.post(LOGIN(),
              {
                email:usercredentials.email,
                password:usercredentials.password,
              })
              if(resp.status ===200){                               
                localStorage.setItem('access_token',resp.data.access);
                localStorage.setItem('refresh_token',resp.data.refresh); 
                servResp.status = resp.status;               
                // this commit == pivotal for menu(logged-in?)
                commit('LOGIN_SUCCESS',resp.data.access)                      
                // you have your token, now log in your user|=> let op check it out
                //dispatch(USER_REQUEST)    
              } else{
                console.log("auth try block: resp",resp)
              }
                return servResp;              
            } 
            catch(err){
              // err comes via interceptor api/index.js
              if(err === "Network problem"){
                // not really true
              servResp.status = "pass"; 
              console.log(servResp.status);
              servResp.specialMsg = "network problem";
              }else{
              servResp.status = err.response.status;
              console.log(servResp.status)
              servResp.nonFieldErr = err.response.data.non_field_errors;          
              servResp.specialMsg = err.response.data.detail;
              console.log("from auth catch err msg",servResp.specialMsg)
              //TODO: do smth with this commit
              commit('LOGIN_ERROR',servResp.specialMsg)
              localStorage.removeItem('access_token');
              localStorage.clear();
              // must be useless
              servResp.emailErr = err.response.data.email;              
              servResp.pswErr = err.response.data.password;              
              }
                return servResp;
                                
            }             
          },
        async userSignUp({commit},creds){
          // see comment for login func
          let servResp = {
            emailErr:[],
            pswErr:[],
            nonFieldErr:[],
            status:""
          }
          try{                   
            let payload = {
              email:creds.email,
              password:creds.password,
              re_password:creds.rePsw
            };           
            const resp = await getAPI.post(
             SIGN_UP(),payload)
            if(resp.status ===201){
              console.log("try block status",resp.status)
              commit('PASS_EMAIL_POTENTIAL_USER',creds.email); 
              servResp.status = resp.status;               
            } 
            return servResp; 
          }
          catch(err){            
            servResp.status = err.response.status;
            servResp.emailErr = err.response.data.email;
            servResp.pswErr = err.response.data.password;
            servResp.nonFieldErr = err.response.data.non_field_errors;
            return servResp;
            
          }
        }                          
    }         
    
}