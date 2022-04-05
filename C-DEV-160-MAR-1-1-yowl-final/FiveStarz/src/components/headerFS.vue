<template>
  <header
    class="
      absolute
      top-0
      lg:flex xl:flex-row
      sm:flex sm:flex-col
      lg:justify-between
      lg:items-end
      px-16
      text-blue-800
      text-opacity-80
    "
  >
    <div class="lg:grid lg:grid-flow-row lg:auto-rows-max sm:flex sm:flex-col">
      <div class="lg:flex lg:flex-row sm:flex sm:flex-col">
        <div class="flex flex-col">
          <a href="/"
            ><img
              src="@/assets/LOGO_FIVE_STARZ.png"
              class="lg:h-28 h-20 pl-4 logo"
              title="Best of reviews"
          /></a>
          <div class="lg:pt-12 pt-6 font-medium slogan text-opacity-80"><p>The best of reviews</p></div>
        </div>
        <div class="flex flex-row justify-between mr-4">
        <router-link to="/Createarticle"><button
          title="New article"
          class="
            bg-yellow-400
            rounded-full
            lg:py-3
            lg:px-6
            lg:w-52
            lg:h-12
            h-7
            w-28
            lg:ml-16
            lg:mt-9
            lg:text-2xl
            text-sm
            lg:font-medium
            flex justify-center
            text-opacity-80
            pt-1
          "
          type="button"
        >
          <svg
            class="lg:w-7 lg:h-7 w-5 h-5 pt-1"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 6v6m0 0v6m0-6h6m-6 0H6"
            ></path></svg
          >New article
        </button></router-link>
        <div class="flex flex-row">
        <a title="Profile" href="/Profile"
          ><svg
            class="lg:w-8 lg:h-8 w-6 h-6 profile"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
            ></path></svg
        ></a>
        <a title="Register" href="/Register"
          ><svg
            class="lg:w-8 lg:h-8 w-6 h-6 register"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
            ></path></svg
        ></a>
        </div>
        </div>
      </div>
      <div>
      </div>
    </div>
        <button @click="logout()">Logout</button>
  </header>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Createarticle',
  components: {
  },
  data () {
    return {
      categories: [],
      category: null
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/categories'
    })
      .then((response) => {
        this.categories = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    setCategory (event) {
      this.category = event.target.value
    },
    search () {
      axios({
        method: 'get',
        url: 'http://localhost:8181/api/articles/search/' + this.searchbar
      })
        .then((response) => {
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    logout () {
      localStorage.removeItem('yowl-jwt')
    }
  }
}
</script>

<style>
header {
  font-family: "Raleway";
}
.logo {
  position: absolute;
}
.slogan {
  margin: 33px;
  padding-left: 50px;
}
.profile {
  margin-left: 3600%;
  margin-top: 170%;
}
.register {
 margin-left: 3600%;
  margin-top: 170%;
}

@media screen and (max-width: 1080px)
{
  .categories {
    width: 267px;
  }
.slogan {
  margin: 30px;
  padding-left: 30px;
}
.profile {
  margin-left: 100%;
  margin-top: 3%;
}
.register {
 margin-left: 100%;
  margin-top: 3%;
}
.search {
  width: 228px;
}
}
</style>
