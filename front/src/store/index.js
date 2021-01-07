import Vue from 'vue';
import Vuex from 'vuex';
import {getAPI} from '@/api/index';
import { getters } from "./index/getters";
import { state } from "./index/state";
import { mutations } from "./index/mutations";
import auth from "./auth/auth";

import {IDEAS,GET_USER_INF} from '@/api/routes';

Vue.use(Vuex)

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions:{
  //  userLogin({commit},usercredentials){
  //     // commit('AUTH_REQUEST')
  //     return new Promise((resolve,reject)=>{
  //       getAPI.post(LOGIN(),
  //       {
  //         email:usercredentials.email,
  //         password:usercredentials.password,
  //       })
  //       .then(response=>{
  //         localStorage.setItem('access_token',response.data.access);
  //         localStorage.setItem('refresh_token',response.data.refresh); 
  //         commit('LOGIN_SUCCESS',response.data.access)                      
  //         // you have your token, now log in your user|=> let op check it out
  //         //dispatch(USER_REQUEST)     
  //         resolve()         
          
  //       })
  //       .catch((err)=>{
  //         console.log("of course there will be a error");
  //             console.log("error",err);
  //             commit('LOGIN_ERROR',err)
  //             localStorage.removeItem('access_token');
  //             localStorage.clear();          
  //             reject()
  //           })        
  //    })
  //   },
    userLogout(context){
      if(context.getters.logIn){
        // commit('logout')
        // localStorage.removeItem('token')
        console.log("User is logged but wants to logout");        
        context.commit('DESTROY_TOKEN');
        context.commit('DESTROY_PROFILE');
        localStorage.clear();
      }         
    },
    async fetchIdeas({commit}){
      try{      
        const serverAnt = await getAPI.get(IDEAS())       
          // console.log("response is 200",serverAnt.status);
          if(serverAnt.data){
          commit('UPDATE_API_IDEAS',serverAnt.data)
          }
        }
      catch (err) {
        console.log("error in ideas");
      }       
       },
    getUserInfo({commit}){
      return new Promise((resolve,reject)=>{
        // ${this.state.currentJWT}
        let JWT = localStorage.getItem('access_token')
        getAPI.get(GET_USER_INF(),
          {headers:{'Authorization':`JWT ${JWT}`},
            "Content-Type":"application/json; charset=utf-8"
          }
        )
        .then(resp=>{
          // console.log("do you see a profile?");
          localStorage.setItem('userId',resp.data.id);
          localStorage.setItem('profile',JSON.stringify(resp.data));         
          commit('SET_USER_ID',resp.data.id); 
          // why don't you the name?
          commit('SET_DISPLAY_NAME',resp.data.profile.name);
          commit('SET_PROFILE',resp.data.profile);
          // optional localStorage.setItem('currentUserEmail',resp.data.email);
          resolve()
        })
        .catch((err)=>{
          console.log("error",err);
          reject()
        })
      })
    },

    
  },
  modules:{
    auth
  }
})



