<!-- Some component.vue -->
<template>
  <VueSimpleSuggest
    v-model="chosen"
    :list="simpleSuggestionList"
    :filter-by-query="true">
<!-- Filter by input text to only show the matching results -->
    <div slot="misc-item-above" slot-scope="{ suggestions, query }">
      <div class="misc-item">
        <span>You're searching for {{ query }}.</span>
      </div>
      <div class="misc-item">
        <span>{{ suggestions.length }} suggestions are shown...</span>
      </div>
      <hr>
    </div>
    <div slot="suggestion-item" slot-scope="{ suggestion }">
      <img :src="suggestion.img" width="30px"/>
      <span>{{ suggestion.title }}</span>
    </div>
  </VueSimpleSuggest>
</template>

<script>
  import VueSimpleSuggest from 'vue-simple-suggest'
  import 'vue-simple-suggest/dist/styles.css' // Optional CSS

  export default {
    components: {
      VueSimpleSuggest
    },
    data() {
      return {
        chosen: ''
      }
    },
    methods: {
      simpleSuggestionList() {
        return [
          {'id':1, 'title':'Vue.js', 'img':'/img/logo.png'},
          {'id':2, 'title':'React.js', 'img':'/img/logo.png'},
          {'id':3, 'title':'Angular.js', 'img':'/img/logo.png'}
        ]
      }
    }
  }
</script>