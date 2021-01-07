<template>
  <div id="app">
    <!-- give connection with routers-->
    <Menu></Menu>
    <Crumbs class="row justify-content-center mt-4" 
    :crumbs="crumbs" @selected="selected"></Crumbs>
    <!-- <div class="container-fluid my-5"> -->
      <router-view/>
     <!-- </div> -->
    <Footer></Footer>     
  </div>
</template>

<script>

import Menu from '@/components/Menu'
import Footer from '@/components/Footer'

import Crumbs from '@/components/BreadCrumbs'

export default {
  name:"App", 
  components:{
    Menu,
    Crumbs,
    Footer
    },
   data(){
     return {
       crumbs:['Home','Category','SubCategory',]
     }
   },
   methods:{
     selected(crumb){
      //  add/delete crumb
       console.log('breadcrumbs clicked',crumb);
     }
   }     
  // },
  // option N1 user has expired access_token 
  // how to use refresh token ???
//   created: function () {
//   axios.interceptors.response.use(undefined, function (err) {
//     return new Promise(function (resolve, reject) {
//       if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
//       // if you ever get an unauthorized, logout the user
//         this.$store.dispatch(AUTH_LOGOUT)
//       // you can also redirect to /login if needed !
//       }
//       throw err;
//     });
//   });
// }
// option N2 user has expired access-token
  // created: function () {
  //   this.$http.interceptors.response.use(undefined, function (err) {
  //     return new Promise(function (resolve, reject) {
  //       if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
  //         this.$store.dispatch(logout)
  //       }
  //       throw err;
  //     });
  //   });
  // } 
  
}
</script>     

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.unstyled{
  list-style-type: none;
}
.wrapper {
        min-height: 100vh;
    }
</style>
