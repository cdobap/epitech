<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <div class="pt-44 m-12">
          <input v-model="content" type="text" placeholder="content" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
          <input v-model="notation" type="text" placeholder="stars" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
          <input v-model="article_id" type="text" placeholder="article id" class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-32">
          <button @click="createComment" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">
            Submit
          </button>
      </div>
      <div><footerFS /></div>
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'AdminComment',
  components: {
    footerFS
  },
  methods: {
    setArticle (event) {
      this.article = event.target.value
    },
    createComment () {
      axios({
        method: 'post',
        url: 'http://localhost:8181/api/comments',
        data: {
          content: this.content,
          notation: this.notation,
          article_id: this.article,
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
    }
  }
}
</script>

<style>

</style>
