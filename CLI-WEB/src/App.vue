<template>
  <Navbar v-if="fun_ini"></Navbar>
  <div id="body" name="body"><router-view /></div>

  <nav class="footer navbar fixed-bottom ">
    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link class="nav-item" to="/">Ayuda</router-link>
      </li>
    </ul>

    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link class="nav-item" to="/">Redes</router-link>
      </li>
    </ul>
    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link class="nav-item" to="/">Contacto</router-link>
      </li>
    </ul>

  </nav>
  <loading v-model:active="isLoading" :can-cancel="false" :is-full-page="true" />
  
</template>

<style>
@import './assets/style.css';
</style>
<script>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import Navbar from '@/components/nav/navbar.vue'
export default {
  async created() {
    this.$store.commit('SET_CONNECTION');
  },
  data() {
    return {
      isLoading: false,
      modo: 1,
      fuente: 2,
      id_config: 1,
      fun_ini:false
    }
  },
  components: {
    Loading,
    Navbar
  },

  methods: {
    
    cerrarSesion() {
      localStorage.removeItem('sesion')
      this.$store.state.session = null
    },
    inicio() {
      this.isLoading = true
      this.$store.state.session = JSON.parse(localStorage.getItem('sesion'))
      let modo = localStorage.getItem("modo")
      this.$store.state.modo = modo
      let fuente = localStorage.getItem("fuente")
      if (fuente) this.fuente = fuente
      body.style.fontSize = this.fuente + "rem"
      if (location.hostname === "localhost" || location.hostname === "127.0.0.1") {
        this.$api = "http://localhost:4000/"
      }
      else {
        this.$api = "api/"
      }
      if (this.$store.state.session != null) {
        this.getConfig()
      } else {
        this.color(modo)
      }
      this.fun_ini=true
      this.isLoading = false
    },
    color(modo) {
      if (modo == 0 || modo == null || modo == undefined) {
        document.documentElement.style.setProperty('--background', "#000");
        document.documentElement.style.setProperty('--text_nav', "#fff");
        document.documentElement.style.setProperty('--nav', "#333");
        document.documentElement.style.setProperty('--text', "#fff");
      } else {
        document.documentElement.style.setProperty('--background', "#fff");
        document.documentElement.style.setProperty('--text_nav', "#000a");
        document.documentElement.style.setProperty('--nav', "#d9d9d9");
        document.documentElement.style.setProperty('--text', "#000");
      }
    },
    getConfig() {
      fetch(this.$store.state.connection + "configByUser/" + this.$store.state.session.id)
        .then(response => {
          return response.json();
        })
        .then(json => {
          if (json.error == null) {
            localStorage.setItem("modo", json.tema)
            this.$store.state.modo = json.tema
            this.$store.state.id_config = json.id
            this.color(json.tema)
          } else {
            console.log(json.error)
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.inicio()

  }

}
</script>
