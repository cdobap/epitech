<template>
<div>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
    <BoardArticles />
    <headerFS/>
    </div>
    <div>
    <footerFS />
   </div>
</div>
  </template>

<script>
import footerFS from '@/components/footerFS.vue'
import headerFS from '@/components/headerFS.vue'
import BoardArticles from '@/components/BoardArticles.vue'

export default {
  name: 'App',
  components: {
    footerFS, headerFS, BoardArticles
  }
}
</script>

<style>

</style>
