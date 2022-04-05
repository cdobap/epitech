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
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-24">
            Author
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-48">
            Article
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-72">
            Content
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-72">
            Stars
          </div>
      </div>
      <div class="">
      <div>
          <div v-for="(comment, index) in comments" :key="comment.id"
          class="flex flex-row m-7 gap-7" >
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-24">
                  {{comment.name}}
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-48">
                  {{comment.title}}
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
                  <input type="text" v-model="comment.content">
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
                 <input type="text" v-model="comment.notation">
              </div>
              <button @click="updatecomment(comment.id, index)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Update</button>
              <button @click="deletecomment(comment.id)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray"
              >Delete</button>
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
  name: 'AdminComments',
  components: {
    footerFS
  },
  data () {
    return {
      comments: []
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/comments'
    })
      .then((response) => {
        console.log(this.comments = response.data)
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    deletecomment (id) {
      axios({
        method: 'delete',
        url: 'http://localhost:8181/api/comments/' + id
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/comments'
          })
            .then((response) => {
              this.comments = response.data
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    updatecomment (id, index) {
      axios({
        method: 'put',
        url: 'http://localhost:8181/api/comments/' + id,
        data: {
          content: this.comments[index].content,
          notation: this.comments[index].notation
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/comments'
          })
            .then((response) => {
              this.comments = response.data
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
