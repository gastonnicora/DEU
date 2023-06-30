<template >
  <div class="container">
    <div>
      <p>Entrenamientos:</p>
      <hr>
      <ul>
        <div v-for="(ent, index) in entrenamientos" :key="index">
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
import moment from 'moment'
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
  methods: {
    compare(a, b) {
      let fa = Date.parse(a.fecha)
      let fb = Date.parse(b.fecha)
      if (fa < fb) {
        return -1;
      }
      if (fa > fb) {
        return 1;
      }
      // a debe ser igual b
      return 0;
    },
    short(list) {
      return list.sort(this.compare)
    },
    delete(list) {
      let lista = []
      let ayer= new Date((new Date()).getTime()-24*60*60*1000)
      list.forEach(e => {
        let f=Date.parse(e.fecha)
        if(ayer<f && this.$route.path != '/historial_entrenamientos'){
          lista.push(e)
        }
        if(ayer>f && this.$route.path == '/historial_entrenamientos'){
          lista.push(e)
        }
        
      });
      
      return lista
    }
  },
  mounted() {
    this.isLoading = true
    let tipo = ["entrenador", "alumnno"]
    fetch(this.$store.state.connection + "entrenamiento_by_" + tipo[this.$store.state.session.tipo] + "/" + this.$store.state.session.id)
      .then(response => {
        return response.json();
      })
      .then(json => {
        if (json.error == null) {
          this.entrenamientos = this.delete(this.short(json.Entrenamientos))
          this.$store.state.entrenamiento = this.entrenamientos[0]
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