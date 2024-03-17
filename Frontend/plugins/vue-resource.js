import Vue from "vue";
import VueResource from "vue-resource";
import VueFileAgent from 'vue-file-agent';
import VueFileAgentStyles from 'vue-file-agent/dist/vue-file-agent.css';

Vue.use(VueResource);
Vue.use(VueFileAgent);
Vue.use(VueFileAgentStyles);

// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
// Vue.http.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
// Vue.http.headers.common['Access-Control-Request-Method'] = 'GET, POST, PUT';
// Vue.http.options.emulateJSON = true