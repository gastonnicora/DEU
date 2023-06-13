<template>
    <div class="links" id="enla" name="enla" @click="collapse"><a>Enlaces <font-awesome-icon :icon="['fas', 'bars']" /></a></div>
    <div class="links" id="links" name="links">
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Entrenamiento:</div>
                <ul class="ul-link">

                    <li class="d-flex justify-content-start">
                        <router-link to="/crear_entrenamiento" @click="new_url('/crear_entrenamiento')"
                            v-if="url != '/crear_entrenamiento'">Crear entrenamiento</router-link>
                        <div v-if="url == '/crear_entrenamiento'">Crear entrenamiento</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <div>
                        <router-link to="/" v-if="url != '/'" @click="new_url('/')">Próximos entrenamientos</router-link>
                        <div v-if="url == '/'">Próximos entrenamientos</div>
                        <ul class="ul-link ">
                            <li class="d-flex justify-content-start">
                                <div v-if="url == '/editar_entrenamiento/*'">Edición de entrenamiento</div>
                            </li>
                        </ul>
                    </div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/historial_entrenamientos" v-if="url != '/historial_entrenamientos'" @click="new_url('/historial_entrenamientos')">Historial de entrenamiento</router-link>
                        <div v-if="url == '/historial_entrenamientos'">Historial de entrenamientos</div>
                    </li>

                </ul>

            </li>
        </ul>
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Alumnos:</div>
                <ul class="ul-link ">
                    <li class="d-flex justify-content-start">
                        <router-link to="/agregar_alumno" v-if="url != '/agregar_alumno'" @click="new_url('/agregar_alumno')">Agregar alumno</router-link>
                        <div v-if="url == '/agregar_alumno'">Agregar alumno</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/listado_alumnos" v-if="url != '/listado_alumnos'" @click="new_url('/listado_alumnos')">Listado de alumnos</router-link>
                        <div v-if="url == '/listado_alumnos'">Listado de alumnos</div>
                    </li>
                </ul>

            </li>
        </ul>
        <ul class="ul-nombre ">
            <li>
                <div class="d-flex justify-content-start">Notificaciones:</div>
                <ul class="ul-link">
                    <li class="d-flex justify-content-start">
                        <router-link to="/crear_notificacion" v-if="url != '/crear_notificacion'" @click="new_url('/crear_notificacion')">Crear notificación</router-link>
                        <div v-if="url == '/crear_notificacion'">Crear notificación</div>
                    </li>
                    <li class="d-flex justify-content-start">
                        <router-link to="/listado_notificaciones" v-if="url != '/listado_notificaciones'" @click="new_url('/listado_notificaciones')">Listado de notificaciones</router-link>
                        <div v-if="url == '/listado_notificaciones'">Listado de notificaciones</div>
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
            url: window.location.pathname,
            collapsed:false
        }
    },
    methods: {
        new_url(url) {
            this.url = url
        },
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
