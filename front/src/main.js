import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// import axios from 'axios';
// import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import "@/assets/css/main.css";
import Vuelidate from 'vuelidate'
//to do import { axios_defaults_baseURL } from "./config";
// Vue.use
// Vue.use(VueAxios);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(Vuelidate)

Vue.config.productionTip = false;


router.beforeEach((to,from,next)=>{
  // go to router/index.js; collect routes with meta:requiresLogin true;
  // if yes|=> sent to login; otherwise |=> proceed without login
  if(to.matched.some(record=>record.meta.requiresLogin)){
    if(!store.getters.logIn){
      // if auth needed but not loggedIn
      console.log("no access token");
      console.log("found refresh",store.getters.getRefreshJWT)
        next({name:'Login'})
        }else{
          // auth needed and loggedIn
          next()
        }
      }//no need to loggedIn
      else{
        next()
    }
  }

)

new Vue({
  router,
  // important for this.$store ... as global var
  store,
  render: h => h(App)
}).$mount('#app')

// // axios.defaults.baseURL = axios_defaults_baseURL;
// to think about
// import store from './store'
// import Axios from 'axios'
//1
// Vue.prototype.$http = Axios;
// const token = localStorage.getItem('token')
// if (token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = token
// }

//2
// axios.interceptors.response.use(
//   (response) => {
//     return response;
//   },
//   function (error) {
//     if (error.response.status === 401) {
//       if (error.response.data.hasOwnProperty("detail")) {
//         if (error.response.data.detail === "Signature has expired.") {
//           const dataForPopUpMessage = {
//             message: "Token is not valid.Please login again",
//             type: "warning",
//           };
//           store.dispatch("popUpMessage", dataForPopUpMessage);
//           store.dispatch("logout");
//           router.push("/");
//         }
//       }
//       return Promise.reject(error);
//     }
//     return Promise.reject(error);
//   }
// );
//3
//https://github.com/konshensx16/vue-todo-frontend/blob/master/src/main.js
