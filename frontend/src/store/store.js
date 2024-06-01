import axios from "axios";


export const store = {
    namespaced: true,
    state: () => ({
        token: localStorage.getItem('token')||""
    }),
    getters: {
        isLoggedIn: state => !!state.token
    },
    mutations: {
        setToken(state, token) {
            state.token = token
            localStorage.setItem('token', token)
        },
        removeToken(state) {
            state.token = ""
            localStorage.setItem('token', "")
        }
    },
    actions: {
        async login({commit}, {username, password, email, router}) {
            try {
                const response = await axios.post("http://localhost:8000/api-token-auth/", {
                  username: username,
                  password: password,
                  email: email,
                })
                const token = response.data.token
                await commit("setToken", token)
                router.push("/")
            } catch (error) {
                alert("Пароль или логин неверны!")
            }
        },
        async register({commit}, {username, password, email, router}) {
            try {
                const response = await axios.post("http://localhost:8000/account/register/", {
                  username: username,
                  password: password,
                  email: email
                })
                const token = response.data.token
                await commit("setToken", token)
                router.push("/login")
            } catch (error) {
                alert("Пользователь с таким логином уже существует!")
            }
        }
    },
}