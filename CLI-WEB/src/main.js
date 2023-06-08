
import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

import router from './router'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap'



createApp(App).use(router).mount('#app')
