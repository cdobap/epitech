
<template>
<div> <StarIcon
        v-for="star in [1, 2, 3, 4, 5]"
        :key="star"
        class="w-full h-full text-gray-400 fill-current"
        :class="{
        'text-yellow-300': star <= articleNote,
        'cursor-pointer transform transition-all hover:scale-125': isEditable
        }"
        @click="isEditable ? $emit('update', star) : null"
        />
</div>
</template>

<script>
import StarIcon from '@/components/StarIcon.vue'
export default {
  components: {
    StarIcon
  },
  data () {
  },
  props: {
    note: {
      type: Number,
      default: 0
    },
    isEditable: {
      type: Boolean,
      default: false
    },
    articleNote: {
      type: Number
    }
  },
  mounted () {
    console.log(this.articleNote)
    console.log(this.note)
  }
}
</script>

<style>
</style>
