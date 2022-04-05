<template>
  <div>
    <button class="bg-yellow-300 text-blue-800 active:bg-yellow-600 font-semibold text-sm px-6 py-3 rounded-full shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
      Add review
    </button>
    <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
      <div class="relative w-auto my-6 mx-auto max-w-6xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-gray-300 outline-none focus:outline-none">
          <!--header-->
            <h3 class="text-3xl mx-52 my-6 font-semibold text-blue-800">
              What did you think ?
            </h3>
          <!--body-->
          <div class="relative p-6 flex flex-row gap-5 justify-center">
              <label
            class="
              flex
              flex-col
              flex-wrap
              justify-center
              content-center
              bg-gray-200
              text-blue-800
              rounded-lg
              tracking-wide
              cursor-pointer
              hover:bg-blue-800
              uppercase
              hover:bg-opacity-80
              hover:text-gray-400
              rounded-md
              w-1/3
              my-4">
                <svg
              class="lg:w-8 lg:h-8 w-6 h-6 mx-14"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
              />
            </svg>
            <span class="lg:text-base text-sm leading-relaxed">Select an image</span>
                <input type="file" class="hidden">
                </label>
                <div>
                <StarReview v-model="notation" @update="updateNote" :note="note" :isEditable="true" class="flex flex-row w-48 mt-3"/>
                <input v-model="content" type="text" placeholder="Type your review here" class="my-4 bg-white rounded-md h-56 w-72 leading-relaxed"></div>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6">
          <button class="text-blue-800 bg-transparent border border-solid border-blue-800 hover:bg-yellow-300 active:bg-yellow-300 font-bold uppercase text-sm px-6 py-3 rounded-full outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
              Close
            </button>
            <button class="text-blue-800 background-transparent font-bold uppercase px-6 py-2 text-sm rounded-lg outline-none focus:outline-none hover:bg-yellow-300 mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="createReview()" @click="toggleModal()">
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-60 fixed inset-0 z-40 bg-blue-800"></div>
  </div>
</template>

<script>
import axios from 'axios'
import StarReview from '@/components/StarReview.vue'

export default {
  name: 'commentModal',
  props: {
    articles: {
      type: Array,
      default: () => []
    }
  },
  components: {
    StarReview
  },
  data () {
    return {
      showModal: false,
      note: 0
    }
  },
  methods: {
    createReview () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/comments' + this.article_id,
        data: {
          content: this.content,
          notation: this.notation,
          article_id: this.article_id,
          user_id: '1'
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.$router.push('/admin/comments')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    toggleModal: function () {
      this.showModal = !this.showModal
    },
    updateNote (star) {
      this.note = star
    }
  }
}
</script>

<style>

</style>
