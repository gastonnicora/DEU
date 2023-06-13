<template>
</template>
<script>
export default {
    name:'EditarEntrenamiento',
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    }
</script>