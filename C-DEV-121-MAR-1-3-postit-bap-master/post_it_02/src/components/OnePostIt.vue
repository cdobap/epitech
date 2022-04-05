<template>
<div v-for="note in notes" :key="note.content" class="bg-purple-50 h-96 w-96 p-8 m-1 md:m-8 relative">
    <h1 id="titlePost" class="text-5xl border-b-2 border-fuchsia-600 break-words">{{note.title}}</h1>
    <p id="contentPost" class="text-2xl pt-5 break-words">{{note.content.toString()}}</p>
    <router-link class="absolute inset-x-0 bottom-0 pb-5 text-4xl" :to="'/note/' + note._id">-></router-link>
    <button class="text-4xl pr-5 absolute top-0 right-0" @click="deletePost(note._id)">x</button>
</div>
</template>

<script>
export default {
  name: 'OnePostIt',
  props: {
    notes: {
      type: Array,
      default: () => []
    },
    method: {
      type: Function
    }
  },
  methods: {
    deletePost (id) {
      console.log(id)
      this.$emit('deletePost', id)
    }
  }
}
</script>

<style scoped>
#contentPost {
  display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 4; overflow: hidden;
}
#titlePost {
  display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; overflow: hidden;
}
</style>
