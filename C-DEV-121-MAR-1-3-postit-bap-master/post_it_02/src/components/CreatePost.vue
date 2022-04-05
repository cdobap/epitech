<template class="">
  <div id="box" class="w-3/4 md:w-3/4 bg-purple-50 h-96 relative">
    <form @submit.prevent="postData" action="" method="post" class="flex flex-col gap-5 p-12">
      <input class="text-5xl border-b-2 border-fuchsia-600 bg-purple-50" type="text" v-model="title" name="title" placeholder="Title" />
      <textarea class="text-2xl pt-5 bg-purple-50" v-model="content" name="content" placeholder="Content"></textarea>
      <button class="material-icons" type="submit">task_alt</button>
    </form>
     <router-link class="absolute left-0 top-0 text-4xl m-2 pl-9" to="/"> &lt;- </router-link>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreatePost',
  data () {
    return {
      title: null,
      content: null
    }
  },
  methods: {
    postData (e) {
      axios.post('http://5.135.119.239:3090/notes', {
        title: this.title,
        content: this.content
      })
        .then((result) => {
          console.log(result)
          this.$router.push({ path: '/' })
        })
    }
  }
}
</script>

<style scoped>
#box{
  height: 600px
}
</style>
