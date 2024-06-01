import axios from "axios";


export const store = {
    namespaced: true,
    state: () => ({
        token: localStorage.getItem('token')||"",
        username: localStorage.getItem('username')||"",
        password: localStorage.getItem('password')||"",
    }),
    getters: {
        isLoggedIn: state => !!state.token
    },
    mutations: {
        setToken(state, token, username, password) {
            state.token = token
            localStorage.setItem('token', token)
            localStorage.setItem('username', username)
            localStorage.setItem('password', password)
        },
        removeToken(state) {
            state.token = ""
            state.username = ""
            state.password = ""
            localStorage.setItem('token', "")
            localStorage.setItem('username', null)
            localStorage.setItem('password', null)
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
                console.log(response)
                const token = response.data.token
                await commit("setToken", token, username, password)
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