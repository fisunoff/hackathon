import Vue from "vue"
import VueRouter from "vue-router"
import store from "@/store"
import loginPage from "@/pages/loginPage.vue"
import mainPage from "@/pages/mainPage.vue"


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: mainPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/login',
        component: loginPage,
        meta: {requiresAuth: false}
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    const token = store.state.login.token
    if (to.meta.requiresAuth && !token) {
        next("/login")
    } else {
        console.log(token)
        next()
    }
})
export default router;
