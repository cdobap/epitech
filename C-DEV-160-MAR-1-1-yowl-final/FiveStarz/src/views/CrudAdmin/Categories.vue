<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <div class="flex flex-row m-7 gap-7" >
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-32">
            Category
          </div>
      </div>
      <div class="">
      <div>
          <div v-for="(categorie, index) in categories" :key="categorie.id"
          class="flex flex-row m-7 gap-7" >
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
                  <input type="text" v-model="categorie.name">
              </div>
              <button @click="updatecat(categorie.id, index)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Update</button>
              <button @click="deletecategorie(categorie.id)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Delete</button>
          </div>
      </div>
      <footerFS />
    </div>
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'AdminCategories',
  components: {
    footerFS
  },
  data () {
    return {
      categories: []
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/categories'
    })
      .then((response) => {
        this.categories = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    deletecategorie (id) {
      axios({
        method: 'delete',
        url: 'http://localhost:8181/api/categories/' + id
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/categories'
          })
            .then((response) => {
              this.categories = response.data
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    updatecat (id, index) {
      axios({
        method: 'put',
        url: 'http://localhost:8181/api/categories/' + id,
        data: {
          name: this.categories[index].name
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/categories'
          })
            .then((response) => {
              this.categories = response.data
            })
            .catch(function (error) {
              console.log(error)
            })
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
