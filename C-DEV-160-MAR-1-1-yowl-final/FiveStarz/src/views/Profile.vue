<template>
  <div><div>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <headerFS />
    <div
      class="
        grid grid-rows-9 grid-cols-4 grid-flow-col
        gap-12
        justify-items-center
        lg:mb-28 mb-20
      "
    >
      </div>
      </div>
      <div class="row-start-">
        <div class="lg:p-28 p-2 ml-96 mb-40 mr-96 bg-blue-800 bg-opacity-20 lg:rounded-r-xl rounded-xl">
          <div class="pl-72">
          <p class="lg:font-bold text-blue-800 pl-24 lg:text-2xl text-xl font-semibold">Update</p>
          <br />
          <input
            class="lg:w-80 w-72 rounded-md p-1"
            title="Enter your login"
            placeholder="New login"
          />
          <div><br /></div>
          <input
            title="Enter a password"
            class="lg:w-80 w-72 rounded-md p-1"
            type="password"
            placeholder="New password"
          />
          <div><br /></div>
          <input
            title="Enter password again"
            type="password"
            class="lg:w-80 w-72 rounded-md p-1"
            placeholder="Password confirmation"
          />
          <div><br /></div>
          <input
            class="lg:w-80 w-72 rounded-md p-1"
            title="Enter your email address"
            type="email"
            placeholder="New email"
          />
          <div class="lg:visible invisible"><br /></div>
          <div class="lg:visible invisible"><br /><br /></div>
          <p class="text-blue-800">
            Don't have an account?
            <a href="/Register" title="Sign in" class="underline"> Register!</a>
          </p>
          <div><br /></div>
          <div class="lg:pl-64 pl-56">
            <button title="Update" class="bg-yellow-400 rounded-full px-4 py-2">
              <svg
                class="w-9 h-9 text-blue-800"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7"
                ></path>
              </svg>
            </button></div>
          </div>
        </div>
    <div><footerFS /></div>
  </div>
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import headerFS from '@/components/headerFS.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    footerFS,
    headerFS
  },
  methods: {
    updateuser (id, index) {
      axios({
        method: 'put',
        url: 'http://localhost:8181/api/users/' + id,
        data: {
          name: this.users[index].name,
          email: this.users[index].email,
          is_admin: this.users[index].is_admin
        },
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          axios({
            method: 'get',
            url: 'http://localhost:8181/api/users'
          })
            .then((response) => {
              this.users = response.data
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
}
</script>

<style>
</style>
