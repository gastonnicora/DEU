<template >
    <div class="container ent">
        <div class="row">
            <div class="col-10 ">
                    <p>Fecha: {{ entrenamiento.fecha }}</p>
                    <p>Tipo: {{ tipo }}</p>
            </div>
            <div class="col-2 d-flex d-flex  align-items-center ml-auto">
                <font-awesome-icon :icon="['fas', 'chevron-right']" />
            </div>

        </div>
    </div>
</template>
<script>
export default {
    name: 'Ent',
    data() {
        return {
            tipo:null
        }
    },
    props: [
        "entrenamiento"
    ],
    mounted(){
        let ent=["Fuerza","Velocidad","Resistencia","Estrategia"]
        this.tipo=ent[this.entrenamiento.tipo]
    }
}
</script>