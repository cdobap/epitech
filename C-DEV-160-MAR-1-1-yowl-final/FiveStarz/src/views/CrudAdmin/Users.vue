<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <div class="flex flex-row m-7 gap-7" >
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-72">
            Name
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-72">
            Email
          </div>
          <div class="border-b-2 border-gray p-5 h-16 m-9 w-24">
            Admin
          </div>
      </div>
      <div class="">
      <div>
          <div v-for="(user, index) in users" :key="user.id"
          class="flex flex-row m-7 gap-7" >
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
                <input v-model="user.name" type="text">
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-72">
                <input v-model="user.email" type="text">
              </div>
              <div class="border-2 border-gray p-5 h-16 bg-gray-50 m-9 w-24">
                <input class="w-12" v-model="user.is_admin" type="text">
              </div>
              <button @click="updateuser(user.id, index)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Update</button>
              <button @click="deleteuser(user.id)" class="p-5 h-16 bg-gray-50 m-9 rounded-full border-2 border-gray">Delete</button>
          </div>
      </div>
    </div>
      <footerFS />
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import axios from 'axios'

export default {
  name: 'AdminUsers',
  components: {
    footerFS
  },
  data () {
    return {
      users: []
    }
  },
  mounted () {
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
  },
  methods: {
    deleteuser (id) {
      axios({
        method: 'delete',
        url: 'http://localhost:8181/api/users/' + id
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
    },
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
