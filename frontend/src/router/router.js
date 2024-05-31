import Vue from "vue"
import VueRouter from "vue-router"
import store from "@/store"
import loginPage from "@/pages/loginPage.vue"
import mainPage from "@/pages/mainPage.vue"
import currentDataPage from "@/pages/currentDataPage.vue";
import changeDataPage from "@/pages/changeDataPage.vue";
import accountPage from "@/pages/accountPage.vue";
import registerPage from "@/pages/registerPage.vue";

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
    {
        path: '/register',
        component: registerPage,
        meta: {requiresAuth: false}
    },
    {
        path: '/current-data',
        component: currentDataPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/change-data',
        component: changeDataPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/user',
        component: accountPage,
        meta: {requiresAuth: true}
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
