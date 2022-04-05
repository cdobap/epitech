import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import Axios from 'axios'

/* createApp(App).use(store).use(router).mount('#app') */

const axios = Axios.create({
  baseURL: 'http://localhost:8181/api/'
})

const token = localStorage.getItem('yowl-jwt')
if (token) {
  axios.defaults.headers.common.Authorization = `Bearer ${token}`
}

/* created: function () {
  this.$axios.interceptors.response.use(undefined, function (err) {
    return new Promise(function () {
      if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
        localStorage.removeItem('yowl-jwt')
        this.$router.push('/Login')
      }
      throw err
    })
  })
} */

const app = createApp(App)

app.use(store)
app.use(router)
app.config.globalProperties.$axios = axios
app.mount('#app')
