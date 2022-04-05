import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Admin from '../views/Admin.vue'
import AdminArticle from '../views/CrudAdmin/Article.vue'
import AdminArticles from '../views/CrudAdmin/Articles.vue'
import AdminUser from '../views/CrudAdmin/User.vue'
import AdminUsers from '../views/CrudAdmin/Users.vue'
import AdminCategory from '../views/CrudAdmin/Category.vue'
import AdminCategories from '../views/CrudAdmin/Categories.vue'
import AdminComment from '../views/CrudAdmin/Comment.vue'
import AdminComments from '../views/CrudAdmin/Comments.vue'
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue'
import Login from '../views/Login.vue'

const isNotAuth = (to, from, next) => {
  if (!localStorage.getItem('yowl-jwt')) {
    next()
    return
  }
  next('/')
}

const isAuth = (to, from, next) => {
  if (localStorage.getItem('yowl-jwt')) {
    next()
    return
  }
  next('/Login')
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    beforeEnter: isAuth
  },
  {
    path: '/admin/article',
    name: 'AdminArticle',
    component: AdminArticle,
    beforeEnter: isAuth
  },
  {
    path: '/admin/articles',
    name: 'AdminArticles',
    component: AdminArticles,
    beforeEnter: isAuth
  },
  {
    path: '/admin/user',
    name: 'AdminUser',
    component: AdminUser,
    beforeEnter: isAuth
  },
  {
    path: '/admin/users',
    name: 'AdminUsers',
    component: AdminUsers,
    beforeEnter: isAuth
  },
  {
    path: '/admin/category',
    name: 'AdminCategory',
    component: AdminCategory,
    beforeEnter: isAuth
  },
  {
    path: '/admin/categories',
    name: 'AdminCategories',
    component: AdminCategories,
    beforeEnter: isAuth
  },
  {
    path: '/admin/comment',
    name: 'AdminComment',
    component: AdminComment,
    beforeEnter: isAuth
  },
  {
    path: '/admin/comments',
    name: 'AdminComments',
    component: AdminComments,
    beforeEnter: isAuth
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/Profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login,
    beforeEnter: isNotAuth
  },
  {
    path: '/createarticle',
    name: 'Createarticle',
    component: () => import(/* webpackChunkName: "createarticle" */ '../views/Createarticle.vue')
  },
  {
    path: '/produit',
    name: 'Produit',
    component: () => import(/* webpackChunkName: "produit" */ '../views/Produit.vue')
  }
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
