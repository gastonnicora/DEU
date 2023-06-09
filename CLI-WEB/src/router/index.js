import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import EditProfile from '../views/EditProfile.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/:pathMatch(.*)*',
    name:"Error",
    redirect:"/"
  },
  {
    path: '/edit-profile',
    name: 'Edit',
    component: EditProfile
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
