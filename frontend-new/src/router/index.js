import { createRouter, createWebHashHistory } from 'vue-router'
import RandomView from '../views/RandomView.vue'

const routes = [
  {
    path: '/',
    name: 'random',
    component: RandomView
  },
  {
    path: '/create',
    name: 'create',

    component: function () {
      return import('../views/CreateView.vue')
    }
  },
  {
    path: '/new',
    name: 'new',

    component: function () {
      return import('../views/NewView.vue')
    }
  },
  {
    path: '/top',
    name: 'top',

    component: function () {
      return import('../views/TopView.vue')
    }
  },
  {
    path: '/seen',
    name: 'seen',

    component: function () {
      return import('../views/SeenView.vue')
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
