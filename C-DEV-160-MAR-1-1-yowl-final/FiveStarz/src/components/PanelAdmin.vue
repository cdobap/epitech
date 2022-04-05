<template>
<div class="flex flex-row">
    <div class="grid grid-cols-2 gap-4 m-9 w-2/4">
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/user">Create user</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/users">Display users</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/category">Create category</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/categories">Display categories</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/article">Create article</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/articles">Display articles</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/comment">Create comment</a>
        </div>
        <div class="border-2 border-gray-200 w-72 p-7 bg-gray-50">
            <a href="/admin/comments">Display comments</a>
        </div>
    </div>
    <div class="grid grid-cols-2 gap-4 m-9 w-2/4">
        <div class="border-2 border-gray-200 h-48 w-72 p-7 bg-gray-100">
            <h1>Number of users</h1>
            <div class="text-6xl ml-24 mt-7">
                {{numberOfUsers}}
            </div>
        </div>
        <div class="border-2 border-gray-200 h-48 w-72 p-7 bg-gray-100">
            <h1>Number of articles</h1>
            <div class="text-6xl ml-24 mt-7">
                {{numberOfArticles}}
            </div>
        </div>
        <div class="border-2 border-gray-200 h-48 w-72 p-7 bg-gray-100">
            <h1>Number of comments</h1>
            <div class="text-6xl ml-24 mt-7">
                {{numberOfComments}}
            </div>
        </div>
        <div class="border-2 border-gray-200 h-48 w-72 p-7 bg-gray-100">
            <h1>Number of categories</h1>
            <div class="text-6xl ml-24 mt-7">
                {{numberOfCategories}}
            </div>
        </div>
        <div class="border-2 border-gray-200 h-48 w-72 p-7 bg-gray-100">
            Average comments per article <div class="text-6xl ml-24 mt-7">{{avgCom}}</div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PanelAdmin',
  components: {
  },
  data () {
    return {
      numberOfUsers: 0,
      numberOfArticles: 0,
      numberOfComments: 0,
      numberOfCategories: 0,
      avgCom: 0
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8181/api/kpi'
    })
      .then((response) => {
        this.numberOfUsers = response.data[0]
        this.numberOfArticles = response.data[1]
        this.numberOfComments = response.data[2]
        this.numberOfCategories = response.data[3]
        this.avgCom = Math.round(this.numberOfComments / this.numberOfArticles)
        console.log(response)
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
  }
}
</script>

<style>
</style>
