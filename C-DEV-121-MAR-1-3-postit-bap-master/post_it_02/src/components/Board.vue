<template>
<div class="flex flex-wrap md:flex-wrap gap-6">
  <!-- <div><button class="bg-yellow-200 p-2 rounded" @click="deleteall">delete all</button></div> -->
  <OnePostIt :notes="notes" @deletePost="deletePost"/>
</div>
</template>

<script>
import OnePostIt from '@/components/OnePostIt.vue'
import axios from 'axios'
export default {
  name: 'Board',
  components: {
    OnePostIt
  },
  data () {
    return {
      notes: []
    }
  },
  mounted () {
    axios
      .get('http://5.135.119.239:3090/notes')
      .then(response => {
        console.log(response.data.notes)
        localStorage.notes = JSON.stringify(response.data.notes)
        this.notes = JSON.parse(localStorage.notes)
      })
      .catch(err => {
        console.error(err)
        this.$router.push({ path: '/404' })
      })
  },
  methods: {
    deletePost (id) {
      axios
        .delete('http://5.135.119.239:3090/notes/' + id)
        .then(res => {
          console.log(res)
          axios
            .get('http://5.135.119.239:3090/notes')
            .then(response => {
              localStorage.notes = JSON.stringify(response.data.notes)
              this.notes = JSON.parse(localStorage.notes)
            })
        })
        .catch(err => {
          console.error(err)
          this.$router.push({ path: '/404' })
        })
    },
    deleteall () {
      axios
        .get('http://5.135.119.239:3090/notes')
        .then(response => {
          for (const elt of response.data.notes) {
            console.log(elt._id)
            axios
              .delete('http://5.135.119.239:3090/notes/' + elt._id)
              .then(res => {
                console.log(res)
                axios
                  .get('http://5.135.119.239:3090/notes')
                  .then(response => {
                    localStorage.notes = JSON.stringify(response.data.notes)
                    this.notes = JSON.parse(localStorage.notes)
                  })
              })
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
