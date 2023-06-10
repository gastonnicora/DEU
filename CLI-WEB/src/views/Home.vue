<template>
    <div class="container ">
        <div class="row justify-content-center">
            <div class="col-md-10 order-md-2 ">
                <div class="row justify-content-center d-flex d-flex  align-items-md-center ">
                    <div class="col-md order-md-3  ">
                        <Login v-if="this.$store.state.session == null"></Login>
                        <Entrenamiento v-if="this.$store.state.session != null && this.$store.state.entrenamiento != null">
                        </Entrenamiento>
                    </div>
                    <div class="col-md order-md-2  ">
                        <Info v-if="this.$store.state.session == null"></Info>

                        <Entrenamientos v-if="this.$store.state.session != null"></Entrenamientos>
                    </div>
                </div>
            </div>
            <div class="col-md-2 nav order-md-1 justify-content-center " v-if="cantidad == 3">1256615</div>

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

    data() {
        return {
            cantidad: 0
        }

    },
    methods: {
        inicio() {
            if (!this.$store.state.session == null || this.$store.state.session.tipo == 1) {
                this.cantidad = 2
            } else {
                this.cantidad = 3
            }
        }
    },
    mounted() {
        this.inicio()

    }

}
</script>