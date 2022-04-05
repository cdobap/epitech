<template>
<div>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
<headerFS />
<div
      class="
        grid grid-rows-9 grid-cols-4 grid-flow-col
        gap-12
        justify-items-center
      "
    >
      <div class="row-start-1 col-start-2 col-span-2 pr-80">
        <a href="#"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo"
            title="Best of reviews"
        /></a>
      </div>
      <div class="row-start-6 col-start-2 col-span-2 bg-blue-800 bg-opacity-20 rounded-xl">
        <div class="p-32">
          <div></div>
          <p class="font-bold text-blue-800 pl-24 text-2xl">Connect</p>
          <br />
          <input v-model="email"
          class="w-80 rounded-md p-1" title = "Enter your email" placeholder="Email" />
          <div><br /></div>
          <input
            v-model="password"
            title = "Enter a password"
            class="w-80 rounded-md p-1"
            type="password"
            placeholder="Password"
          />
          <div><br /><br /></div>
          <p class="text-blue-800">
            Don't have an account?
            <a href="/Register" title="Sign in" class="underline"> Register!</a>
          </p>
          <div><br /></div>
          <div class="pl-64">
            <button @click="login"
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
import headerFS from '@/components/headerFS.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    footerFS,
    headerFS
  },
  methods: {
    login () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/login',
        data: {
          email: this.email,
          password: this.password
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
    }
  }
}
</script>

<style>

</style>
