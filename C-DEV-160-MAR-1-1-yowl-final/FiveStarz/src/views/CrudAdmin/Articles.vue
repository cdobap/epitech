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
            Title
          </div>
           <!-- <div class="border-b-2 border-gray p-5 h-16 m-9 w-32">
            Description
          </div> -->
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-32">
            Price
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-32">
            Category
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-32">
            Stars
          </div>
      </div>
      <div class="">
          <div v-for="(article, index) in articles" :key="article.id"
          class="flex flex-row m-7 gap-7" >
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
                  <input class="w-20" type="text" v-model="article.title">
              </div>
              <!-- <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
                  <input type="text" v-model="article.description">
              </div> -->
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
                  <input class="w-20" type="text" v-model="article.price">
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
                  <input class="w-20" type="text" v-model="article.category_id">
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
                {{article.notation_avg}}
              </div>
              <button @click="updateArticle(article.id, index)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Update</button>
              <button @click="deleteArticle(article.id)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Delete</button>
          </div>
      </div>
      <footerFS />
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'AdminArticles',
  components: {
    footerFS
  },
  data () {
    return {
      articles: []
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/articles'
    })
      .then((response) => {
        this.articles = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    deleteArticle (id) {
      axios({
        method: 'delete',
        url: 'http://localhost:8181/api/articles/' + id
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/articles'
          })
            .then((response) => {
              this.articles = response.data
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    updateArticle (id, index) {
      axios({
        method: 'put',
        url: 'http://localhost:8181/api/articles/' + id,
        data: {
          title: this.articles[index].title,
          /* description: this.articles[index].description, */
          price: this.articles[index].price,
          category_id: this.articles[index].category_id
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/articles'
          })
            .then((response) => {
              this.articles = response.data
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
