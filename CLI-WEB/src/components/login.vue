<template>
    <h4><font-awesome-icon :icon="['fas', 'door-open']" /> Iniciar sesión</h4>
    <br>
    <form @submit.prevent="iniciarSesion" id="form">
        <label for="email">Email: </label>
        <input type="text" id="email" required>
        <br>
        <label for="pass">Contraseña: </label>
        <input type="text" id="pass" required>
        <div  class="error" v-if="error" > {{ this.error }}</div>
        <br>
        <input class="btn " type="submit" value="INICIAR SESIÓN">

        <div id="cod"> </div>
    </form>
</template>

<script>
export default {
    name: 'Login',
    data(){
        return {
            error:null
        }
    },
    methods: {
        iniciarSesion() {
            let email = document.getElementById("email").value
            let pass = document.getElementById("pass").value
            fetch(this.$store.state.connection + 'login', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email, contra: pass })
            })
                .then(response => {
                    var campo_usuarios_get_cod = document.getElementById("cod")
                    campo_usuarios_get_cod.innerText = response.status
                    localStorage.setItem('user',response.data.response)
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


