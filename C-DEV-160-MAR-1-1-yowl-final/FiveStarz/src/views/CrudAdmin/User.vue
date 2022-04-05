<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <div class="flex flex-col pl-48 pr-48">
          <input v-model="name" type="text" placeholder="name" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="email" type="text" placeholder="email" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="password" type="password" placeholder="password" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="password_confirmation" type="password" placeholder="password_confirmation" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <!-- <input v-model="is_admin" type="text" placeholder="is_admin"> -->
          <input v-model="bdate" type="date" placeholder="birthdate" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <button @click="createUser()" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">
            Submit
          </button>
      </div>
      <footerFS />
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'AdminUser',
  components: {
    footerFS
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
          password_confirmation: this.password_confirmation,
          bdate: this.bdate
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.$router.push('/admin/users')
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
