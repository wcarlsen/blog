import Vue from "vue";

const app = new Vue({
  el: '#app',
  delimiters: ["[[", "]]"],
  data: {
    message: 'Hello World!'
  },
})