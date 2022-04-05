<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <div>
          <input v-model="name" type="text" placeholder="name" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <button @click="createCategory" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">
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
  name: 'AdminCategory',
  components: {
    footerFS
  },
  methods: {
    createCategory () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/categories',
        data: {
          name: this.name/* ,
          picture: this.picture */
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.$router.push('/admin/categories')
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
