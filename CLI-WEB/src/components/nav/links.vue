<template>
    <div class="links" id="enla" name="enla" @click="collapse"><a>Enlaces <font-awesome-icon :icon="['fas', 'bars']" /></a></div>
    <div class="links" id="links" name="links">
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Entrenamiento:</div>
                <ul class="ul-link">

                    <li class="d-flex justify-content-start">
                        <router-link to="/crear_entrenamiento" 
                            v-if="this.$route.path != '/crear_entrenamiento'">Crear entrenamiento</router-link>
                        <div v-if="this.$route.path == '/crear_entrenamiento'">Crear entrenamiento</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <div>
                        <router-link to="/" v-if="this.$route.path != '/'">Próximos entrenamientos</router-link>
                        <div v-if="this.$route.path == '/'">Próximos entrenamientos</div>
                        <ul class="ul-link ">
                            <li class="d-flex justify-content-start">
                                <div v-if="this.$route.path == '/editar_entrenamiento/*'">Edición de entrenamiento</div>
                            </li>
                        </ul>
                    </div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/historial_entrenamientos" v-if="this.$route.path != '/historial_entrenamientos'" >Historial de entrenamiento</router-link>
                        <div v-if="this.$route.path == '/historial_entrenamientos'">Historial de entrenamientos</div>
                    </li>

                </ul>

            </li>
        </ul>
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Ejercicios:</div>
                <ul class="ul-link">
                    <li class="d-flex justify-content-start">
                        <router-link to="/crear_ejercicio" v-if="this.$route.path != '/crear_ejercicio'" >Crear ejercicio</router-link>
                        <div v-if="this.$route.path == '/crear_ejercicio'">Crear ejercicio</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/listado_ejercicios" v-if="this.$route.path != '/listado_ejercicios'" >Listado de ejercicios</router-link>
                        <div v-if="this.$route.path == '/listado_ejercicios'">Listado de ejercicios</div>
                    </li>
                </ul>

            </li>

        </ul>
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Alumnos:</div>
                <ul class="ul-link ">
                    <li class="d-flex justify-content-start">
                        <router-link to="/agregar_alumno" v-if="this.$route.path != '/agregar_alumno'" >Agregar alumno</router-link>
                        <div v-if="this.$route.path == '/agregar_alumno'">Agregar alumno</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/listado_alumnos" v-if="this.$route.path != '/listado_alumnos'">Listado de alumnos</router-link>
                        <div v-if="this.$route.path == '/listado_alumnos'">Listado de alumnos</div>
                    </li>
                </ul>

            </li>
        </ul>
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Notificaciones:</div>
                <ul class="ul-link">
                    <li class="d-flex justify-content-start">
                        <router-link to="/crear_notificacion" v-if="this.$route.path != '/crear_notificacion'" >Crear notificación</router-link>
                        <div v-if="this.$route.path == '/crear_notificacion'">Crear notificación</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/listado_notificaciones" v-if="this.$route.path != '/listado_notificaciones'" >Listado de notificaciones</router-link>
                        <div v-if="this.$route.path == '/listado_notificaciones'">Listado de notificaciones</div>
                    </li>
                </ul>

            </li>

        </ul>
    </div>
</template>
<script>
export default {
    name: 'Links',
    data() {
        return {
            collapsed:false
        }
    },
    methods: {
        collapse(){
            if(this.collapsed){
            links.classList.remove("hidden")
            }else{
            links.classList.add("hidden")
            }
            this.collapsed=!this.collapsed
        }
    },
    mounted() {
        var mql = window.matchMedia('(max-width: 801px)');

            mql.addListener(function (event) {
            if (event.matches) { // La media querie coincide
                links.classList.add("hidden")
            this.collapsed=true
            enla.classList.remove("hidden")
        }else{
            enla.classList.add("hidden")
            this.collapsed=false
            links.classList.remove("hidden")
        }
            });
        let ancho=window.innerWidth
        if(ancho<=801){
            links.classList.add("hidden")
            this.collapsed=true
        }else{
            enla.classList.add("hidden")
            this.collapsed=false
        }
    },

} 
</script>
