<template>
</template>
<script>
export default {
    name:'CrearNotificacion',
    created() {
        if(this.$store.state.session==null){
            
           this.$router.replace("home");
        }
    },
    }
</script>