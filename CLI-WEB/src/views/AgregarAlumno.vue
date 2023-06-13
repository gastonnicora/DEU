<template>
</template>
<script>
export default {
    name:'AgregarAlumno',
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    }
    
</script>