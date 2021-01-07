<template>
    <div class="container">
        <div class="row">            
            <div class="col col-md-10" >
                <div class='container'>
                    <div class="wrapper">
                        <h1>Please check your 
                            email {{showEmailPotentUser}} to see the link to confirm
                        </h1>  
                                          
                    </div>                    
                </div>                
            </div>
        </div>
    </div>           
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name:'Confirm',    
    computed:
        mapGetters(['showEmailPotentUser']) 
               
   
}
</script>

<style scoped>

</style>