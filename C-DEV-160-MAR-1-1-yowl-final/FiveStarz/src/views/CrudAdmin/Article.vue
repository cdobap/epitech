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
          <select @change="setCategory($event)"
          type="text" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
            <option>Category</option>
            <option v-for="(categorie) in categories" :key="categorie.id"
            :value="categorie.id">
            {{categorie.name}}</option>
          </select>
          <input v-model="title" type="text" placeholder="title" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="description" type="text" placeholder="description" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="price" type="text" placeholder="price" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <input v-model="picture_1" type="text" placeholder="picture" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9">
          <button @click="createArticle" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">
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
  name: 'AdminArticle',
  components: {
    footerFS
  },
  data () {
    return {
      categories: [],
      category: null,
      file: null
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
  setup () {
    function uploadPics (event) {
      this.file = event.target.files[0]
      console.log(this.file)
    }
    return {
      uploadPics
    }
  },
  methods: {
    setCategory (event) {
      this.category = event.target.value
    },
    createArticle () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/articles',
        data: {
          title: this.title,
          description: this.description,
          price: this.price,
          category_id: this.category,
          user_id: '1',
          picture_1: 'pics'
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.$router.push('/admin/articles')
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
