<template>
    <h4>Agregar alumno</h4>
    <br>
    {{ mensaje }}
    <br>
    <table class="table table-striped" aria-label="Agregar alumno">
        <thead>
            <tr>
                <th scope="col">Nombre</th>
                <th scope="col">Apellido</th>
                <th scope="col">Email</th>
                <th scope="col"></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(alu, index) in listAlumnos" :key="index">
                <td>{{ alu.nombre }}</td>
                <td>{{ alu.apellido }}</td>
                <td>{{ alu.email }}</td>
                <td><button class="btn boton" @click="agregar(alu.id)" :aria-label="'Agregar '+alu.nombre+' '+alu.apellido+' email:'+alu.email">Agregar</button></td>
            </tr>
        </tbody>
    </table>
</template>
<script>
export default {
    name: 'AgregarAlumno',
    created() {
        if (this.$store.state.session == null) {

            this.$router.replace("home");
        }
    },
    data() {
        return {
            listAlumnos: {},
            mensaje: ""
        }
    },
    methods: {
        agregar(id) {
            fetch(this.$store.state.connection + 'entrenador_alumno', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ alumno: id, entrenador: this.$store.state.session.id })
            })
                .then(response => {
                    return response.json();
                })
                .then(json => {
                    if (json.error) {
                        this.mensaje = json.error
                    } else {
                        this.mensaje = "Alumno agregado"
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    mounted() {
        fetch(this.$store.state.connection + 'usuario/alumnos', {
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
                    this.listAlumnos = JSON.parse(JSON.stringify(json.Alumnos))
                }
            })
            .catch(error => {
                console.log(error)
            })
    },
}

</script>