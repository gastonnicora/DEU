<template >
    <div class="container" v-if="this.$store.state.entrenamiento!=null">
        <div>
            Entrenamiento el dia:
            <br>
            {{ this.$store.state.entrenamiento.fecha }}
            <br>
            <br>
            Calentamiento:
            <ul>
                <div v-for="(eje, index) in this.$store.state.entrenamiento.Ejercicios" :key="index">
                    <div v-if="eje.categoria==0">
                        <Ejercicio :eje="eje"></Ejercicio>

                    </div>
                </div>
            </ul>
            <br>
           Entrenamiento:
            <ul>
                <div v-for="(eje, index) in this.$store.state.entrenamiento.Ejercicios" :key="index">
                    <div v-if="eje.categoria==1">
                        <Ejercicio :eje="eje"></Ejercicio>

                    </div>
                </div>
            </ul>
            <br>
            Regenerativo:
            <ul>
                <div v-for="(eje, index) in this.$store.state.entrenamiento.Ejercicios" :key="index">
                    <div v-if="eje.categoria==2">
                        <Ejercicio :eje="eje"></Ejercicio>

                    </div>
                </div>
            </ul>
        </div>
    </div>
</template>
<script>
import Ejercicio from './ejercicio.vue'
export default {
    name: 'Entrenamiento',
    components:{
        Ejercicio
    },
    mounted() {
        let ent = ["Fuerza", "Velocidad", "Resistencia", "Estrategia"]
    }
}
</script>