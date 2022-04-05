<template>
  <div>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <div
      class="
        grid grid-rows-9 grid-cols-3 grid-flow-col
        lg:gap-12
        gap-8
        justify-items-center
        lg:mb-28 mb-20
      "
    >
      <div class="row-start-1 col-start-2 pr-80">
        <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="lg:h-28 h-24 ml-6 logo"
            title="Best of reviews"
        /></a>
      </div>
<div><br /></div>
      <div class="row-start-5 col-start-2 bg-blue-800 bg-opacity-20 rounded-xl">
        <div class="lg:p-28 p-8">
          <p class="font-bold text-blue-800 pl-24 text-2xl">JOIN US!</p>
          <br />
          <input v-model='name' class="w-80 rounded-md p-1" title = "Enter your login" placeholder="Login" />
          <div><br /></div>
          <input
            v-model='password'
            title = "Enter a password"
            class="w-80 rounded-md p-1"
            type="password"
            placeholder="Password"
          />
          <div><br /></div>
          <input
            v-model='password_confirmation'
            title = "Enter password again"
            type="password"
            class="w-80 rounded-md p-1 border"
            placeholder="Password confirmation"
          />
          <div><br /></div>
          <input v-model="email" class="w-80 rounded-md p-1" title = "Enter your email address" type="email" placeholder="Mail" />
          <div><br /></div>
          <input v-model="bdate" class="w-80 rounded-md p-1" type="date" title = "Enter your birthdate" placeholder="Birthdate" />
          <div><br /><br /></div>
          <p class="text-blue-800 text-opacity-80">
            Already have an account? <a href="/Login" title = "Sign in" class="underline"> Sign in!</a>
          </p>
          <div><br /></div>
          <div class="pl-64">
            <button @click="registerUser()"
            title="Join" class="bg-yellow-400 rounded-full px-4 py-2">
              <svg
                class="w-9 h-9 text-blue-800"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7"
                ></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div><footerFS /></div>
  </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    footerFS
  },
  data () {
    return {
      name: '',
      email: '',
      password: '',
      password_confirmation: '',
      bdate: ''
    }
  },
  methods: {
    createUser () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/register',
        data: {
          name: this.name,
          email: this.email,
          password: this.password,
          password_confirmation: this.password_confirmation/* ,
          bdate: this.bdate */
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          this.$router.push('/')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    async registerUser () {
      try {
        if (!this.name && !this.password && !this.email && !this.password_confirmation) {
          return
        }
        const { data } = await this.$axios.post('/register', {
          name: this.name,
          email: this.email,
          password: this.password,
          password_confirmation: this.password_confirmation,
          bdate: this.bdate
        })
        localStorage.setItem('yowl-jwt', data.token)
        this.$axios.defaults.headers.common.Authorization = `Bearer ${data.token}`
        this.$router.push('/')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style>
</style>
