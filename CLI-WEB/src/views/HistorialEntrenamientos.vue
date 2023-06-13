<template>
</template>
<script>
export default {
    name:'HistorialEntrenamiento',
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    }
</script>