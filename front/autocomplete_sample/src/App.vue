<template>
  <div id="app">
    <img alt="Vue logo" src="/img/logo.png">
    <HelloAsyncSuggest/>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import HelloAsyncSuggest from './components/HelloAsyncSuggest.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld
    HelloAsyncSuggest
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
