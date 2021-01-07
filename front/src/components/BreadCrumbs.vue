<template>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
      <!-- crumb== string,crumIndx -- int -->
    <li class="breadcrumb-item align-items-center" v-for="(crumb,crumIndx) in crumbs" :key="crumIndx">
        <!-- add bootrap class 'disabled' for the but dynam -->
        
        <button type="button" class="btn btn-link" :class="{disabled:isLast(crumIndx)}" @click="selected(crumb)">
            {{crumb}}
        </button>
    </li>
    
  </ol>
</nav>
    
</template>

<script>
export default {
    name:'Crumbs',
    props:{
        crumbs:Array
        
    },
    methods:{
        isLast(crumIndx){
            console.log('index',crumIndx)
            return this.crumbs.length -1;
        },
        selected(crumb){
            this.$emit('selected',crumb);
        }
    }
}
</script>

<style scoped>
.breadcrumb{
    background-color: blanchedalmond;
    border: 1px sold lightsalmon;
    /* 0 0 0 0.125 */
    border-radius: 0.37rem;
}

</style>