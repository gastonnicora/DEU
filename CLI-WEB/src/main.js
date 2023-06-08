
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import './assets/main.css'

import router from './router'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap'



const app = createApp(App)
app.use(router)
app.use(VueAxios, axios) 
app.mount('#app')
