<template>
</template>
<script>
export default {
    name:'ListadoNotificaciones',
    created() {
        if(this.$store.state.session==null){
            
           this.$router.replace("home");
        }
    },
    }
</script>