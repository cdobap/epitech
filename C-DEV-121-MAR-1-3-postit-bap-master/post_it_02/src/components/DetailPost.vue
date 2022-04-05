<template>
  <div id="box" class="w-3/4 md:w-3/4 bg-purple-50 h-96 relative">
    <div class="bg-purple-50 p-5 ">
    <button  class="absolute top-0 right-0 pr-9 material-icons m-5" @click="showText = !showText">post_add</button>
      <div v-if="showText">
        <h1 class="text-5xl border-b-2 border-fuchsia-600 break-words my-9">{{note.title}}</h1>
        <p class="text-2xl pt-5 break-words">{{note.content.toString()}}</p>
        <router-link class="absolute left-0 top-0 text-4xl m-2 pl-9" to="/"> &lt;- </router-link>
      </div>
      <div v-else class="">
        <form @submit.prevent="updatePost(note._id)" action="" method="post" class="flex flex-col gap-5 m-5">
          <input class="text-5xl border-b-2 border-fuchsia-600 bg-purple-50 my-9" type="text" v-model="note.title" name="title" placeholder="Title" />
          <textarea class="text-2xl pt-5 bg-purple-50" v-model="note.content" name="content" placeholder="Content"></textarea>
          <button class="material-icons" type="submit">task_alt</button>
        </form>
         <router-link class="absolute left-0 top-0 text-4xl m-2 pl-9" to="/"> &lt;- </router-link>
      </div>
  </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'DetailPost',
  data () {
    return {
      showText: true,
      note: {
        title: '',
        content: []
      }
    }
  },
  mounted () {
    axios
      .get('http://5.135.119.239:3090/notes/' + this.$route.params._id)
      .then(response => {
        console.log(this.note = response.data.note)
      })
      .catch(err => {
        console.error(err)
        this.$router.push({ path: '/404' })
      })
  },
  methods: {
    updatePost (id) {
      axios
        .put('http://5.135.119.239:3090/notes/' + id, {
          title: this.note.title,
          content: this.note.content
        })
        .then(res => {
          console.log(res)
          axios
            .get('http://5.135.119.239:3090/notes/' + this.$route.params._id)
            .then(response => {
              console.log(this.note = response.data.note)
              this.$router.push({ path: '/' })
            })
        })
        .catch(err => {
          console.error(err)
          this.$router.push({ path: '/404' })
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
