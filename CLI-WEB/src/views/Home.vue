<template>
    <div class="container ">
        <div class="row justify-content-md-center">
            <div class="col order-md-2 contenedor">
                <div class="row justify-content-md-center d-flex d-flex  align-items-md-center ">
                <div class="col-md order-md-3  ">
                    <Login v-if="this.$store.state.session==null"></Login>
                </div>
                <div class="col-md order-md-2  ">
                    <Info ></Info>
                </div>
                </div>
            </div>
        <div class="col-md-1 nav order-md-1 justify-content-center " v-if="cantidad == 3">1256615</div>
        
    </div>
    </div>
</template>
<script>
import Info from '@/components/info.vue'
import Login from '@/components/login.vue'
export default {
    name: 'Home',
    components: {
        Info,
        Login
    },

    data() {
        return {
            cantidad: 0
        }

    },
    methods: {
        inicio() {
            if (!this.$store.state.session!=null ||this.$store.state.session.tipo == 1) {
                this.cantidad = 2
            } else {
                this.cantidad = 3
            }
            console.log(this.cantidad)
        }
    },
    mounted() {
        this.inicio()

    }

}
</script>