<template>
</template>
<script>
export default {
    name:'CrearNotificacion',
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    }
</script>