<template>
  <div><div>
  <headerFS />
  <footerFS />
    <h1 class="text-4xl p-2 m-20 flex items-left justify-left">
      Product Title
    </h1>
    <div
      class="
        grid grid-cols-2
        m-20
        items-center
        gap-x-4
        justify-center
        md:grid-cols-2
      "
    >
      <div
        class="
          grid
          overflow-y-scroll
          mx-xl
          shadow-lg
          flex
          items-right
          justify-right
          rounded-lg
          max-w-xl
          hover:shadow-2xl
          transition
          duration-300
        "
      >
        <img
          src="https://images.unsplash.com/photo-1627751476653-e954179b174a"
          alt=""
          class="rounded-t-lg w-full"
        />
        <h1
          class="
            md:text-1xl
            text-l
            flex
            items-right
            justify-right
            hover:text-indigo-600
            transition
            duration-200
            font-bold
            text-gray-900
          "
        >
          This is Amazing for people to visit.
        </h1>
        <p class="text-gray-700 my-2 hover-text-900">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellat
          itaque praesentium ab. Officia sapiente sint ipsam, velit explicabo
          cum quia nesciunt perspiciatis libero aut tempora laboriosam labore
          quae necessitatibus omnis qui! Quis nostrum consequatur, facilis eius
          eveniet, vero repellat veritatis quia, ducimus necessitatibus optio
          expedita mollitia.
        </p>
        <button
          class="
            float-right
            h-12
            px-6
            left-0
            top-0
            m-2
            bg-yellow-500
            rounded-xl
          "
        >
          BUY
        </button>
        <div><starReview class="px-32 flex flex-row" /></div>
      </div>
    </div>
  </div>
  <button
    class="float-right h-12 px-6 left-0 top-0 m-2 bg-yellow-500 rounded-xl"
  >
   <commentModal />
  </button>
  <div class="grid grid-cols-1 md:grid-cols-1 bg-blue-300"></div>
  <div><footerFS /></div>
  </div>
</template>

<script>
import headerFS from '../components/headerFS.vue'
import footerFS from '../components/footerFS.vue'
import StarReview from '../components/StarReview.vue'
import commentModal from '../components/commentModal.vue'
import axios from 'axios'

export default {
  name: 'Produit',
  components: {
    headerFS,
    footerFS,
    StarReview,
    commentModal
  },
  data () {
    return {
      articles: [],
      comments: []
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/articles/1'
    })
      .then((response) => {
        console.log(this.articles = response.data)
        axios({
          method: 'get',
          url: 'http://localhost:8181/api/comments/article/1'
        })
          .then((response) => {
            console.log(this.comments = response.data)
            /* const a = this.comments */
            /*  const rng = a.length */
            /*  console.log(a.length)
            console.log(a[0])
            console.log(Object.values(a[0])) */
            /*   for (let i = 0; i++; i = rng) {
              if (Object.values(a[i]) == 1) {

              }
            } */
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
</script>

<style scoped>
</style>
