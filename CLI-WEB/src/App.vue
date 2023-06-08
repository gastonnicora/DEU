<template>
  <div id="nav" class="nav navbar">
    <router-link to="/">Inicio</router-link> |
    <router-link to="/mapa"> <i class="fas fa-map-marked"></i>Mapa</router-link> |
    <router-link to="/denuncias">Denuncias</router-link>
  </div>
  <router-view/>
  <footer id="" class="footer">
    <router-link to="/">Inicio</router-link> |
    <router-link to="/mapa"> <i class="fas fa-map-marked"></i>Mapa</router-link> |
    <router-link to="/denuncias">Denuncias</router-link>
  </footer>
</template>

<style>
@import'bootstrap/dist/css/bootstrap.css';
@import './assets/style.css';
</style>
