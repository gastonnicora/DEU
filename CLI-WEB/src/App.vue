<template>
  
  <nav class="nav navbar fixed-top ">

    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <div style="padding:0rem .5rem" @click="$router.go(-1)"><font-awesome-icon :icon="['fas', 'arrow-left']" /></div>
      </li>
    </ul>
    
    <router-link class="navbar-brand" to="/">Inicio</router-link>
    <ul  class="navbar-nav  ml-auto" style="right: 0;">
      <li class="nav-item dropdown">
        <a v-if="this.$store.state.session!=null" class="nav-link dropdown-toggle " style="padding:0rem .5rem" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <font-awesome-icon  :icon="['far', 'user']" />
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <router-link to="#" class="dropdown-item"> <font-awesome-icon :icon="['fas', 'user-pen']" /> Editar Perfil</router-link>
          <div class="dropdown-divider"></div>
          <router-link to="#" class="dropdown-item"> <font-awesome-icon :icon="['fas', 'key']" /> Cambiar Contraseña</router-link>
          <div class="dropdown-divider"></div>
          <router-link to="#" class="dropdown-item"> <font-awesome-icon :icon="['fas', 'palette']" /> Tema</router-link>
          <div class="dropdown-divider"></div>
          <router-link to="#" class="dropdown-item"><font-awesome-icon :icon="['fas', 'door-closed']" /> Cerrar Sesión</router-link>
        </div>
      </li>
    </ul>

  </nav>
  <div id="body"><router-view /></div>
  
  
  <nav class="footer navbar fixed-bottom ">

    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link  class="nav-item" to="/">Ayuda</router-link>
      </li>
    </ul>

    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link class="nav-item" to="/">Redes</router-link>
      </li>
    </ul>
    <ul class="navbar-nav ">
      <li class="nav-item active">
        <router-link  class="nav-item" to="/">Contacto</router-link>
      </li>
    </ul>

  </nav>
</template>

<style>
@import './assets/style.css';
</style>
<script>
export default {
    async created(){
      this.$store.commit('SET_CONNECTION');
    },

  methods: {
    inicio() {
      this.$store.state.session = localStorage.getItem('sesion')
      let modo = localStorage.getItem("modo")
      this.color(modo)
      if (location.hostname === "localhost" || location.hostname === "127.0.0.1")
      {
          this.$api = "http://localhost:4000/"
      }
      else {
        this.$api ="api/"
      }
      if (this.$store.state.session!=null) {

      }
    },
    color(modo) {
      if (modo = 0) {
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
    }
  },
  mounted() {
    this.inicio()

  }

}
</script>
