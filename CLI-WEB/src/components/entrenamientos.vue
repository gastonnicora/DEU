<template>
  <ul>
    <div v-for="(ent, index) in entrenamientos" :key="index">
      <Ent :entrenamiento="ent" @click="this.$store.state.entrenamiento = ent; console.log(ent)"></Ent>
      <br>
    </div>
  </ul>
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
      entrenamientos: []
    }
  },
  components: {
    Loading,
    Ent
  },
  mounted() {
    this.isLoading = true
    fetch(this.$store.state.connection + "entrenamiento_by_entrenador/" + this.$store.state.session.id)
      .then(response => {
        return response.json();
      })
      .then(json => {
        if (json.error == null) {
          this.entrenamientos = json.Entrenamientos
          this.$store.state.entrenamiento = json.Entrenamientos[0]
          console.log(this.$store.state.entrenamiento)
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