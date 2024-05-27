import axios from "axios"
import store from "@/store"


const instance = axios.create({
    baseURL: "http://localhost:8000/"
})

instance.interceptors.request.use((config) => {
    const token = store.state.login.token

    if (token) {
        config.headers.Authorization = `Token ${token}`
    }
    return config
})

export default {
    install(Vue) {
        Vue.prototype.$ajax = instance
    }
}