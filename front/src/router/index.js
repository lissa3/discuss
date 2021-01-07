import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Ideas from '@/views/Ideas'
import IdeaDetail from '@/components/IdeaDetail'
import IdeaSearch from '@/views/IdeaSearch'
import SignUp from '@/components/userUI/auth/SignUp'
import Login from '@/components/userUI/auth/Login'
import Logout from '@/components/userUI/auth/Logout'
import Activate from '@/components/userUI/auth/Activate'
import Confirm from '@/components/userUI/auth/signUpConfirm'
import ChangePassword from '@/components/userUI/pswActions/ChangePassword'
import ResetPassword from '@/components/userUI/pswActions/ResetPassword'
import ResetPasswordConfirm from '@/components/userUI/pswActions/PasswordResetConfirm'
import AuthFailed from '@/components/userUI/auth/authFailed'
import notFound from '../views/404.vue'


import ProfileDetail from '@/components/profileUI/profileDetail.vue'

// import ProfileDetail from '@/components/profileUI/profileDetail'

import ChangeDisplayName from '@/components/profileUI/ChangeDisplayName'
import ChangeProfile from '@/components/profileUI/ChangeProfile'

// add router to middelware of the proj
// name to use in other .vue, component = see above
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/ideas',
    name: 'Ideas',
    component: Ideas,
    meta:{
      requiresLogin:true
    }
  },
  {
    path: '/idea-detail/:id',
    name: 'IdeaDetail',
    component: IdeaDetail,
        
  },
  {
    path: '/ideas-search',
    // path: '/ideas-search/:search/',
    name: 'IdeaSearch',
    component: IdeaSearch
  },
  {
    path: '/profile-detail',
    name: 'ProfileDetail',
    component: ProfileDetail,
    meta:{
      requiresLogin:true
    }
  },
  {    
    path: '/profile-change-display-name/unid',
    name: 'ChangeDisplayName',
    component: ChangeDisplayName,
    meta:{
      requiresLogin:true
    }
  },
  {
    path: '/profile-change/:unid',
    name: 'ChangeProfile',
    component: ChangeProfile,
    meta:{
      requiresLogin:true
    }
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/signup-message',
    name: 'Confirm',
    component: Confirm
  },
  {
    path: '/activate/:uid/:token',
    name: 'Activate',
    component: Activate,
    props:true
  },
  {
    path: '/change-password',
    name: 'ChangePassword',
    component: ChangePassword
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: ResetPassword
  }, 
  {
    path: '/password/reset/confirm/:uid/:token',
    // path: '/reset-password-confirm/:uid/:token',
    name: 'ResetPasswordConfirm',
    component: ResetPasswordConfirm
  },
  
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/agreement',
    name: 'Agree',// see note net above    
    component: () => import(/* webpackChunkName: "about" */ '@/views/Agreement.vue')
  },
  {
    path:'/auth-failed',
    name: 'AuthFailed',
    component:AuthFailed
  },
  {
    path:'*',
    name: 'notFound',
    component:notFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
