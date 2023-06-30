<template>
    <div class="container ent" data-toggle="modal" v-bind:data-target="'#'+ modal ">
        <div class="row">
            <div class="col-2 p-1 d-flex d-flex align-items-center justify-content-center">
                <video class="imagen" :src="this.$store.state.connection + 'static/videos/' + eje.video.nombre" width="420" height="240"></video>
    
            </div>
            <div class="col-8 ">
                <p> {{ eje.nombre }}</p>
                <p> {{ descripcion }}</p>
            </div>
            <div class="col-1 d-flex d-flex  align-items-center ml-auto">
                <font-awesome-icon :icon="['fas', 'chevron-right']" />
            </div>


        </div>
    </div>
    <!--aca empieza el modal-->
    <div class="modal  " v-bind:id="modal " tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered modal-md" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ eje.nombre }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-md-7    d-flex d-flex align-items-center justify-content-center">
                                <video controls :src="this.$store.state.connection + 'static/videos/' + eje.video.nombre" class="imagen" width="420" height="240"></video>
    
                            </div>
                            <div class="col-md-5   ">
                                <p> {{ eje.descripcion }}</p>
                            </div>
                            
                        </div>
                    </div>
                </div>
                <div class="modal-footer justify-content-center">
                    <div v-if="eje.tipo==0">
                    <p>Tiempo del ejercicio: {{ eje.tiempo }} {{  eje.tipo_tiempo }}</p></div>
                    <div v-if="eje.tipo==1">
                    <p>Repeticiones: {{ eje.repeticiones }}</p></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Ejercicio',
    props: [
        "eje"
    ],
    data(){
        return{
        modal:"miModal"+this.eje.id,
        descripcion:this.desc()
        }
    },
    methods:{
        desc(){
           if(this.eje.descripcion.length>100){
            return this.eje.descripcion.slice(0,99)+"..."
           }
           return this.eje.descripcion
        }
    }
}
</script>