const { createApp } = Vue

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            message: 'Hello Vue!',
            first_name : "meng"
        }
    }
}).mount('#app')
