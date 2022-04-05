<template>
  <div id="home" class="home m-5">
    <Board />
    <AddLink />
  </div>
</template>

<script>
// @ is an alias to /src
import Board from '@/components/Board.vue'
import AddLink from '@/components/AddLink.vue'
export default {
  name: 'Home',
  components: {
    Board, AddLink
  }
}
</script>

<style scoped>
#home {
  margin: 60px;
}
</style>
