import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import routes from "./routes"
import vuetify from './plugins/vuetify';
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false;
Vue.use(VueRouter);


const router = new VueRouter({
  routes
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
