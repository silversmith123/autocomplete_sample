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
      <div>{{ suggestion.title }} img {{ suggestion.img }}</div>
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
          {'id':1, 'title':'Vue.js', 'img':'https://jp.vuejs.org/images/logo.svg'},
          {'id':2, 'title':'React.js', 'img':'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K'},
          {'id':3, 'title':'Angular.js', 'img':'https://angularjs.org/img/angularjs-for-header-only.svg'}
        ]
      }
    }
  }
</script>