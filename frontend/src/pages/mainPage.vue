<template>
  <custom-table
      :key="test_data.length"
      v-if="test_data.length > 0"
      :items="test_data"
      :headers="test_headers"
      :api-path="'test_case/api/'"
      :table-title="'Тестовая таблица'"
  />
</template>

<script>

import CustomTable from "@/components/CustomTable.vue";

export default {
  name: "mainPage",
  components: {CustomTable},
  data() {
    return {
      test_data: [],
      test_headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(`test_case/api/`)
    this.test_data = data
    this.test_headers = [
      { text: 'Name', value: 'name' },
      { text: 'Param1', value: 'param1' },
      { text: 'Param2', value: 'param2' },
      { text: 'Param3', value: 'param3' }]
  },
  methods: {

  }
}
</script>

<style scoped>

</style>