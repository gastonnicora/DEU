<template>
  <nav class="nav navbar fixed-top ">

    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <div style="padding:0rem .5rem" @click="$router.go(-1)"><font-awesome-icon :icon="['fas', 'arrow-left']" /></div>
      </li>
    </ul>

    <router-link class="navbar-brand" to="/">Inicio</router-link>
    <ul class="navbar-nav  ml-auto" style="right: 0;">
      <li class="nav-item dropdown" v-if="this.$store.state.session != null">
        <a class="nav-link dropdown-toggle " style="padding:0rem .5rem" href="#" id="navbarDropdown" role="button"
          data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <font-awesome-icon :icon="['far', 'user']" />
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <router-link to="/edit-profile" class="dropdown-item"> <font-awesome-icon :icon="['fas', 'user-pen']" /> Editar
            Perfil</router-link>
          <div class="dropdown-divider"></div>
          <router-link to="#" class="dropdown-item"> <font-awesome-icon :icon="['fas', 'key']" /> Cambiar
            Contraseña</router-link>
          <div class="dropdown-divider"></div>
          <a to="#" class="dropdown-item" data-toggle="modal" data-target="#config" @click="()=>{modal()}"> <font-awesome-icon
              :icon="['fas', 'gear']" /> Configuración</a>
          <div class="dropdown-divider"></div>
          <router-link to="#" class="dropdown-item" @click="cerrarSesion()"><font-awesome-icon
              :icon="['fas', 'door-closed']" /> Cerrar Sesión</router-link>
        </div>
      </li>
    </ul>

  </nav>
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
  <div class="modal  " id="config" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title"> <font-awesome-icon :icon="['fas', 'gear']" /> Configuración </h5>
          <button type="button" class="close boton" @click="cerrar()" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="container">
            <div class=" justify-content-center ">
              <label for="tema">Tema</label>
              <br>
              <div class=" justify-content-center d-flex d-flex  align-items-md-center">
              <font-awesome-icon style="margin:0 1rem " :icon="['fas', 'sun']" /> 
              <label class="switch ">
                <input type="checkbox" id="tema" name="tema" @change="aplicar()">
                <span class="slider round"></span>
              </label><font-awesome-icon style="margin:0 1rem " :icon="['fas', 'moon']" />
            </div>
            </div>
            <br>
            <div class=" justify-content-center ">
              <label for="tam">Tamaño de fuente</label>
              <br>
              <div class="range" style="--step:.25; --min:0.5; --max:2">
                <input type="range" id="tam"  name="tam" value="1" min=".5" max="2" step="0.25"  list="value"  @change="aplicar()">
                
              </div>

<datalist id="value" style="margin:auto">
  <div v-for="i in ((2-.25)/.25)" :key="i">
  <option v-bind:value=" Math.floor( i*100/((2-.25)/.25)) " v-bind:label=".25* i +.25 "></option></div>
</datalist>
            </div>
          </div>
          <br>
          
        </div>
        <div class="modal-footer justify-content-center">
          <button class="btn btn-danger" data-dismiss="modal"  @click="cerrar()" >Cancelar</button>
          <button class="boton btn" data-dismiss="modal" @click="guardar()">Guardar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import './assets/style.css';
</style>
<script>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
export default {
  async created() {
    this.$store.commit('SET_CONNECTION');
  },
  data() {
    return {
      isLoading: false,
      modo:1,
      fuente:2,
      id_config:1
    }
  },
  components: {
    Loading
  },

  methods: {
    guardar(){
      if(tema.checked) this.modo=1 
      this.color(this.modo)
      localStorage.setItem("modo", this.modo)
      this.fuente = tam.value
      body.style.fontSize = this.fuente+"em"
      localStorage.setItem("fuente", this.fuente)
      this.isLoading = true
            fetch(this.$store.state.connection + 'config_editar', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id:this.id_config, us: this.$store.state.session.id, tema:this.modo })
            })
                .then(response => {
                    return response.json();
                })
                .then(json => {
                    if (json.error) {
                        this.error = json.error
                    } 
                    console.log("guardar")
                })
                .catch(error => {
                    console.log(error)
                })
                this.isLoading = false
    },
    aplicar(){
      let modo=0
      if(tema.checked) modo=1 
      this.color(modo)
      let fuente = tam.value
      body.style.fontSize = fuente+"em"
    },
    modal(){
      if(this.modo==1) tema.checked=true
      tam.value= this.fuente
    },
    cerrar(){
      this.color(this.modo)
      body.style.fontSize = this.fuente+"em"
    },
    cerrarSesion() {
      localStorage.removeItem('sesion')
      this.$store.state.session = null
    },
    inicio() {
      this.isLoading = true
      this.$store.state.session = JSON.parse(localStorage.getItem('sesion'))
      let modo = localStorage.getItem("modo")
      this.modo=modo
      let fuente = localStorage.getItem("fuente")
      if(fuente) this.fuente=fuente
      body.style.fontSize = this.fuente+"rem"
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
      this.isLoading = false
    },
    color(modo) {
      if (modo == 1 || modo == null || modo == undefined) {
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
            this.modo=json.tema
            this.id_config=json.id
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
