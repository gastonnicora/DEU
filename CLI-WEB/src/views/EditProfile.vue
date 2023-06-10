<template>
    <h1>Editar Perfil</h1>
    <form @submit.prevent="save" id="form">
        <p>Nombre:</p>
        <input :value="nombre"/>
        <p>Apellido:</p>
        <input :value="apellido"/>
        <p>Email:</p>
        <input :value="email"/>
        <input class="boton btn " type="submit" value="Guardar">
    </form>

</template>

<script>
export default {
    name:'Edit',
    props:{
        nombre:String,
        apellido:String,
        email:String,
    },
    methods:{
        
        save(){
            fetch(this.$store.state.connection + 'usuario_editar', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: this.nombre,apellido:this.apellido,email: this.email })
            })
                .then(response => {
                    localStorage.setItem('user',response.data)
                    this.$store.state.session = response.body
                    return response.json();
                })
                .then(json => {
                    if(json.error){
                        this.error= json.error
                    }
                })
                .catch(error => {
                   console.log(error)
                })
        }
    }


}


</script>