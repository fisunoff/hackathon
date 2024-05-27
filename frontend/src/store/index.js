import Vue from 'vue'
import Vuex from 'vuex'
import {store} from "@/store/store";



Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        login: store
    },

})