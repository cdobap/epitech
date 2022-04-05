<template>
  <div>
<link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet">
      <transition name="modal">
        <div class="modal-mask" v-if="show">
          <div class="modal-wrapper">
            <div class="modal-container bg-gray-300 rounded-md w-5/6 h-96 grid rows-3 place-items-center ">

              <div class="modal-header text-blue-800 text-xl">
                <slot name="header">
              What did you think ?
                </slot>
              </div>
              <div class="modal-body flex flex-row gap-5 justify-center">
                <slot name="body">
                  <div class="w-8 h-8">
                <StarReview v-model="notation" @update="updateNote" :note="note" :isEditable="true"/>
                </div>
                <input type="file" class="bg-gray-400 rounded-md w-1/3">
                <input v-model="content" type="text" placeholder="Type your review here" class="bg-white rounded-md h-56 w-72">
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">

                  <button v-on:click="createReview()" @click="closeModal()" type="submit" class="bouton shadow-sm rounded-full bg-yellow-300 text-blue-800 px-6 py-1 pt-1 ml-96 mb-5">Submit</button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>
         <div id="app">
    <button v-on:click="toggleModal()"><addReview/></button>
      <!-- use the modal component, pass in the prop -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarReview from '@/components/StarReview.vue'

export default {
  name: 'commentForm',
  props: {
    articles: {
      type: Array,
      default: () => []
    }
  },
  components: {
    addReview,
    StarReview
  },
  data () {
    return {
      show: false,
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
    closeModal () {
      this.show = false
      document.querySelector('body').classList.remove('overflow-hidden')
      document.querySelector('body').classList.remove('bg-blue-800')
    },
    openModal () {
      this.show = true
      document.querySelector('body').classList.add('overflow-hidden')
      document.querySelector('body').classList.add('bg-blue-800')
      document.querySelector('body').classList.add('bg-opacity-50')
      document.querySelector('body').classList.add('filter')
    },
    updateNote (star) {
      this.note = star
    }
  }
}
</script>

<style>
.modal-header {
    font-family: "Raleway";
}
</style>
