import axios from 'axios'
// import router from '@/router';
import store from '@/store';

const foundToken = localStorage.getItem('access_token');
console.log("msg from axios",foundToken);

const APIUrl = 'http://127.0.0.1:8000' // django server address
// let currentJWT = localStorage.getItem('access_token');

const getApiFormIncoded = axios.create({
  baseURL: APIUrl,
  headers:{
    'Content-Type':'application/x-www.form-urlencoded'
  }
})

const simpleAPI = axios.create({
  baseURL: APIUrl,
  headers:{
    Accept:"application/json",
    'Content-Type': 'application/json',
    }
 })

const getAPI = axios.create({
  baseURL: APIUrl,
  // timeout:3000,  
  headers: { 
    Accept:"application/json",
    'Content-Type': 'application/json',
    // &&'' or null|=> otherwise error
    Authorization:localStorage.getItem('access_token')? `JWT ${localStorage.getItem('access_token')}`:null
  }
})
//https://github.com/axios/axios/issues/383
// https://www.intricatecloud.io/2020/03/how-to-handle-api-errors-in-your-web-app-using-axios/
// let op: network error(server down) status error?
getAPI.interceptors.response.use((resp)=>{
  // console.log("response from axios-api status 200",resp.status);
  // important  to return resp
  return resp;
  },
  function(error){
  console.log(error)
  // case when dj server is down and is UNABLE to send ANY response
    if(!error.response){
    //  == "Error: Network Error"){
      console.log("axios interseptor",error);
      error="Network problem"
  }else if(error.response.status === 401){   
    // console.log("api index calling",error.response.data) ;
    //console.log("data.code",error.response.data.code) == undefined if user.is_active() = False
    // error.response.data ==No active account found with the given credentials  
    if(error.response.data.code==="token_not_valid"){
      console.log("Token is not valid.");
      store.dispatch("refreshToken");
      // store.dispatch("LogOut");
      this.$router.push('/login')
      // router.push("/")
      
      }
    return Promise.reject(error);
  }else{
    console.log("error, but status !=401")
  }
  return Promise.reject(error);
})


// if you need Axios + CSRF
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'



export { getAPI,getApiFormIncoded,simpleAPI }

