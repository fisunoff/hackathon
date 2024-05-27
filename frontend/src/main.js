import Vue from 'vue'
import App from './App.vue'
import router from '@/router/router'
import store from '@/store'
import axios from "@/plugins/axios"
import {IconsPlugin} from "bootstrap-vue"

import vuetify from './plugins/vuetify'


Vue.config.productionTip = false
Vue.use(axios)
Vue.use(IconsPlugin)

//components.forEach(component => Vue.component(component.name, component))

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
