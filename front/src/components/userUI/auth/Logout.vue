<template>
    <div class="container">
        <h1>Logout</h1>
        <h3>Do you really want to logout?</h3>
        <div class="trap">
            <div class="trap-elem">
                <button @click="logOut" class="btn btn-danger">Logout</button>
            </div>
            <div class="trap-elem">
                <a href="#" @click="goHome('Home')">Back to Home</a>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    name:"Logout",
    methods:{
        logOut(){
            console.log("User wants to logout"); 
            this.$store.dispatch('userLogout') 
            .then(()=>{
                      this.$router.push({name:"Home"}) 
                   }
               ).catch((error)=>{
                   console.log("err",error);
                    // this.customIncorrect = true;
               })       

            // sessionStorage.removeItem('access_token');
            // sessionStorage.removeItem('refresh_token') ;        
            // this.$router.push({name:"Home"})
    
        },
        goHome(direction){
            this.$router.push({'name':direction});
        }
    }
}
</script>
<style scoped>
.trap{
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
.trap-elem{
    padding: 1rem 0;
}
</style>