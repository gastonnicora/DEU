<template>
    <h5>Crear entrenamiento</h5>
    <div class="container">
        <div class="row  justify-content-center  ">
            <div class="col-md   ">
                
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col"><input type="checkbox" id="todos" name="todos" v-model="todos"></th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Apellido</th>
                            <th scope="col">Posición</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(alu, index) in listAlumnos" :key="index">
                            <th scope="row"><input type="checkbox" :id="alu.id" name="check" :checked="todos"></th>
                            <td>{{ alu.nombre }}</td>
                            <td>{{ alu.apellido }}</td>
                            <td>{{ pos(alu.posicion) }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-md  ">
                <form @submit.prevent="pass">
                                <p>Contraseña:</p>
                                <p><input type="password" required name="contra" id="contra" /></p>
                                <p>Nueva contraseña:</p>
                                <p><input type="password" required name="new_contra" id="new_contra" /></p>
                                <p>Repita la contraseña:</p>
                                <p><input type="password" required name="rp_contra" id="rp_contra" /></p>

                                <p><input class="boton btn " type="submit" value="Guardar"></p>

                            </form>
            </div>
        </div>
    </div>
    <button class="btn boton">Guardar</button>
    <p id="sms" name="sms"></p>
</template>

<script>
export default {
    name: 'CrearEntrenamiento',
    data() {
        return {
            user: this.$store.state.session,
            error: null,
            oscuro: false,
            alumnos: [],
            listAlumnos: [],
            todos: false,
            
        };

    },
    created() {
        if(this.$store.state.session==null){
            
            router.push({ path: 'Home' })
        }
    },
    methods: {
        pos(p){
            let posicion=["Defensa","Medio campo","Ataque"]
            console.log(posicion[p])
            console.log(this.listAlumnos)
            return posicion[p]
        },
        iniciar() {
            //usuario/alumnos
            fetch(this.$store.state.connection + 'usuario/alumnos/' + this.$store.state.session.id, {
                method: 'Get',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',

                }
            })
                .then(response => {

                    return response.json();
                })
                .then(json => {
                    if (json.error) {
                        this.error = json.error
                    } else {
                        this.alumnos = JSON.parse(JSON.stringify(json.Alumnos))
                        this.listAlumnos = JSON.parse(JSON.stringify(json.Alumnos))
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        save() {
            fetch(this.$store.state.connection + 'usuario_editar', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',

                },
                body: JSON.stringify({ nombre: this.user.nombre, apellido: this.user.apellido, email: this.user.email, contra: this.user.contra, id: this.user.id, posicion: this.user.posicion, tipo: this.user.tipo })
            })
                .then(response => {

                    return response.json();
                })
                .then(json => {
                    if (json.error) {
                        this.error = json.error
                    } else {
                        this.$store.state.session = json
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }

    },
    mounted() {
        
        this.iniciar()
    },


}


</script>