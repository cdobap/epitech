<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <div>
        <div class="lg:grid lg:grid-flow-col lg:auto-cols-max flex flex-col pt-32 pl-16">
          <div class="
          pt-3
          lg:pl-6
          lg:pt-0">
            <select @change="setCategory($event)"
              class="
                lg:h-14
                lg:w-96
                lg:pl-28
                lg:rounded-l-md
                lg:rounded-r-none
                lg:font-medium
                lg:text-xl
                collection
                bg-blue-800
                bg-opacity-80
                text-white
                rounded
                categories
                h-8
                mb-1
              "
              name="Collection"
            >
              <option value="collection" selected disabled>Collection</option>
              <option v-for="(categorie) in categories" :key="categorie.id"
              :value="categorie.id">
              {{categorie.name}}</option>
            </select>
          </div>
          <div class="flex flex-row">
          <div>
            <input v-model="searchbar"
              title="search"
              placeholder="Search..."
              class="
                lg:h-14
                border-2 border-blue-800 border-opacity-80
                lg:rounded-r-md
                lg:rounded-l-none
                lg:font-medium
                lg:text-xl
                lg:pl-6
                rounded-md
                search
              "
            />
          </div>
          <div>
            <button @click="search()"
              title="Search"
              class="
                bg-yellow-400
                rounded-full
                lg:py-2
                lg:px-8
                lg:w-24
                lg:h-14
                lg:ml-3
                w-9
                h-6
                ml-1
                pl-2
                mt-0.5
              "
              type="button"
            >
              <svg
                class="lg:w-9 lg:h-9 w-5 h-5 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                ></path>
              </svg>
            </button>
            </div>
          </div>
        </div>
      </div>
      <div class="grid grid-cols-3 gap-4 pt-20">
          <div v-for="(article) in articles" :key="article.id"
          class="" >
            <div class="relative w-96 h-96 bg-none m-7 rounded-lg mx-28 space-x-10">
                <div class="w-80 bg-gray-200 rounded-xl">
                    <img
            src="@/assets/icoming-logo-final.jpg"
            title="Product image"
        />
                </div>
                <div class="text-blue-800 font-semibold text-lg ml-3">
                    {{article.title}}
                </div>
                <div>
                    <div class="absolute inset-y-0 right-0 w-8">
                      <StarReview :articleNote="article.notation_avg"/>
                    </div>
                </div>
            </div>
          </div>
      </div>
    </div>
</template>

<script>
import StarReview from '@/components/StarReview.vue'
import axios from 'axios'

export default {
  name: 'BoardArticles',
  components: {
    StarReview
  },
  data () {
    return {
      articles: [],
      categories: [],
      category: null
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/articles'
    })
      .then((response) => {
        this.articles = response.data
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
  methods: {
    setCategory (event) {
      console.log(this.category = event.target.value)
      axios({
        method: 'get',
        url: 'http://localhost:8181/api/articles/category/' + this.category
      })
        .then((response) => {
          this.articles = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    search () {
      axios({
        method: 'get',
        url: 'http://localhost:8181/api/articles/search/' + this.searchbar
      })
        .then((response) => {
          console.log(this.articles = response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style>
.search {
  width: 1220px;
}
</style>
