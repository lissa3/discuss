<template>  
  <div class="container py-md-5 py-4">
    <div class="row long">      
      <div class="col col-md-10 text-center">
        <div class="not-found">
          <h1>Page not found</h1>
          <h2><router-link :to="{name:'Home'}">Go Home</router-link></h2>     
      
        </div>
      </div> 
    </div>     
  </div>
</template>

<script>
export default {
  name: 'notFound',
  methods:{
    goTo(direction){
      this.$router.push({name:direction});
      },
    }    
  
}
</script>
<style  scoped>
.long{
    min-height: 100vh;
}
.not-found {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
h1 {
  color: #ffffff;
  font-size: 70px;
  margin-bottom: 20px;
}
</style>
