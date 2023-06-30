<template>
    <div class="container">
        <div class="row  justify-content-center  ">
            <div class="col-md   ">
                <div class="container">
                    <div>
                        <p>Alumnos:</p>
                        <hr>
                        <ul>
                            <div v-for="(alu, index) in alumnos" :key="index">
                                <div>
                                    <Alumno :alumno="alu" @click="this.$store.state.alumno = alu"></Alumno>
                                </div>
                                <br>
                            </div>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col-md  ">

            </div>
        </div>
    </div>
</template>
<script>
import Alumno from '@/components/alumno.vue'
export default {
    name: 'ListadoAlumnos',
    data() {
        return {
            alumnos: null
        }
    },
    created() {
        if(this.$store.state.session==null){
            
           this.$router.replace("home");
        }
    },
    components: {
        Alumno
    },
    mounted() {
        fetch(this.$store.state.connection + "/usuario/alumnos/" + this.$store.state.session.id)
            .then(response => {
                return response.json();
            })
            .then(json => {
                if (json.error == null) {
                    this.alumnos = json.Alumnos
                    this.$store.state.entrenamiento = json.Alumnos[0]
                } else {
                    console.log(json.error)
                }
            })
            .catch(error => {
                console.log(error)
            })
    },
}
</script>