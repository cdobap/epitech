<template>
  <div>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <headerFS />
    <div class="pt-60 min-h-screen flex items-center justify-center lg:mb-28 mb-20">
      <div
        class="
          row-start-5
          bg-blue-800 bg-opacity-20
          lg:p-16
          p-6
          rounded-xl
          items-center
          shadow-2xl
          w-2/3
        "
      >
        <h2 class="lg:text-3xl items-center text-center font-bold mb-8 text-blue-800 text-opacity-80 text-2xl">
          Add new article
        </h2>
        <div class="lg:space-y-2 space-y-1">
          <div>
            <label class="block mb-1 font-semibold text-blue-800 text-opacity-80 text-lg">Title</label>
            <input
              v-model="title"
              type="text"
              class="w-full lg:p-3 p-1 rounded"
            />
          </div>
          <div class="mb-3">
            <label class="block mb-1 font-semibold justify-content text-blue-800 text-opacity-80 text-lg"
              >Description</label
            >
            <input
              v-model="description"
              type="text"
              class="w-full lg:p-3 p-1 rounded"
            />
          </div>
          <div class="mb-3">
            <label class="block mb-1 font-semibold text-blue-800 text-opacity-80 text-lg">Category</label>

            <select
              @change="setCategory($event)"
              type="text"
              class="w-full bg-white lg:p-3 p-1 rounded"
            >
              <option></option>
              <option
                v-for="categorie in categories"
                :key="categorie.id"
                :value="categorie.id"
              >
                {{ categorie.name }}
              </option>
            </select>
          </div>
          <div class="mb-3">
            <label class="block mb-1 font-semibold text-blue-800 text-opacity-80 text-lg">Price</label>
            <input
              v-model="price"
              type="text"
              class="w-full lg:p-3 p-1 rounded"
            />
          </div>
          <label
            class="
              w-full
              flex flex-col
              items-center
              lg:px-4
              lg:py-6
              px-2
              py-4
              bg-white
              text-blue-800
              text-opacity-80
              rounded-lg
              shadow-lg
              tracking-wide
              uppercase
              cursor-pointer
              hover:bg-blue-800
              hover:bg-opacity-80
              hover:text-gray-300
            "
          >
            <svg
              class="lg:w-8 lg:h-8 w-6 h-6"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
              />
            </svg>
            <span class="mt-2 lg:text-base text-sm leading-normal">Select an image</span>
            <input @change="uploadPics" type="file" class="hidden" />
          </label>
          <button
            @click="createArticle()"
            class="block lg:h-12 lg:px-6 h-8 px-4 bg-yellow-500 text-blue-800 text-opacity-80 font-semibold rounded-xl"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
    <div><footerFS /></div>
  </div>
</template>

<script>
import axios from 'axios'
import footerFS from '@/components/footerFS.vue'
import headerFS from '@/components/headerFS.vue'

export default {
  name: 'Createarticle',
  components: {
    footerFS,
    headerFS
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
