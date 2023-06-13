<template>
</template>
<script>
export default {
    name:'ListadoNotificaciones',
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    }
</script>