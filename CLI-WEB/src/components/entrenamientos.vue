<template >
  
  <div class="container">
    <div>
    <p>Entrenamientos:</p>
    <hr>
  <ul>
    <div  v-for="(ent, index) in entrenamientos" :key="index">
      <div>
      <Ent :entrenamiento="ent" @click="this.$store.state.entrenamiento = ent"></Ent>
      </div>
      <br>
    </div>
  </ul>
    </div>
    </div>
  <loading v-model:active="isLoading" :can-cancel="false" :is-full-page="true" />
</template>
<script>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import Ent from './ent.vue'
export default {
  name: 'Entrenamientos',
  data() {
    return {
      isLoading: false,
      entrenamientos: null
    }
  },
  components: {
    Loading,
    Ent
  },
  mounted() {
    this.isLoading = true
    let tipo=["entrenador","alumnno"]
    fetch(this.$store.state.connection + "entrenamiento_by_"+tipo[this.$store.state.session.tipo]+"/" + this.$store.state.session.id)
      .then(response => {
        return response.json();
      })
      .then(json => {
        if (json.error == null) {
          this.entrenamientos = json.Entrenamientos
          this.$store.state.entrenamiento = json.Entrenamientos[0]
        } else {
          console.log(json.error)
        }
      })
      .catch(error => {
        console.log(error)
      })
    this.isLoading = false
  },
}
</script>