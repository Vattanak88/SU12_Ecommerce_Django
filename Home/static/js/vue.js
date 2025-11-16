import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'



const { createApp } = Vue;

createApp({
    delimiters: ['[[', ']]'],
       data() {
    return {
      products: [],         // all products from JSON
      visibleProducts: [],  // products currently visible
      perPage: 10,
      currentPage: 1
    };
  },
  computed: {
    hasNext() {
      return this.visibleProducts.length < this.products.length;
    }
  },
  methods: {
    loadMore() {
      const start = (this.currentPage - 1) * this.perPage;
      const end = start + this.perPage;
      this.visibleProducts = this.visibleProducts.concat(this.products.slice(start, end));
      this.currentPage++;
    }
  },
  mounted() {
    fetch("{% static 'data/product.json' %}")
      .then(res => res.json())
      .then(data => {
        this.products = data;
        this.loadMore(); // load first 10 products
      });
  }
}).mount('#app');





















