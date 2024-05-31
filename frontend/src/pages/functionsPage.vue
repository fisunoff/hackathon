<template>
  <div class="d-flex">
    <nav-panel />
    <custom-table
        :key="data.length"
        v-if="data.length > 0"
        :items="data"
        :headers="headers"
        :api-path="apiPath"
        :table-title="'Функции'"
        style="width: 100%"
    />
  </div>
</template>

<script>

import CustomTable from "@/components/CustomTable.vue";
import NavPanel from "@/components/NavPanel.vue";
export default {
  name: "functionsPage",
  components: {CustomTable, NavPanel},
  data() {
    return {
      apiPath: 'protection_function/api/',
      data: [],
      headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(this.apiPath)
    this.data = data
    this.headers = [
      { text: '№', value: 'id' },
      { text: 'Наименование', value: 'title' },
      { text: 'Условное обозначение', value: 'symbol' },
    ]
  },
  methods: {

  }
}
</script>

<style scoped>

</style>