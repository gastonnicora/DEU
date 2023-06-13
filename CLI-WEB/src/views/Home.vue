<template>
    <div class="contenedor_c ">
        <div class="row u justify-content-center  ">
            <div class="col-md order-md-2 hijo  justify-content-center d-flex align-items-center  ">
                <div>
                <Login v-if="this.$store.state.session == null"></Login>
                <Entrenamiento v-if="this.$store.state.session != null && this.$store.state.entrenamiento != null">
                </Entrenamiento>
            </div>
            </div>
            <div class="col-md order-md-1  hijo   justify-content-center d-flex align-items-center ">
                <div>
                <Info v-if="this.$store.state.session == null"></Info>

                <Entrenamientos v-if="this.$store.state.session != null"></Entrenamientos>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
import Info from '@/components/info.vue'
import Login from '@/components/login.vue'
import Entrenamientos from '@/components/entrenamientos.vue'
import Entrenamiento from '@/components/entrenamiento.vue'
export default {
    name: 'Home',
    components: {
        Info,
        Login,
        Entrenamientos,
        Entrenamiento
    },

   

}
</script>