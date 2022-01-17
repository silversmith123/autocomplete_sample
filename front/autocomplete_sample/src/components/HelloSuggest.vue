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
          'Vue.js',
          'React.js',
          'Angular.js'
        ]
      }
    }
  }
</script>