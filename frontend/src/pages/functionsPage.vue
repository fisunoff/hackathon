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
        :add-action="true"
        :can-edit="true"
        :create-form="CreateFunctionForm"
        :edit-form="EditFunctionForm"
        :show-form="InfoFunctionForm"
        :show-more-info="true"
        style="width: 100%"
    />
  </div>
</template>

<script>

import CustomTable from "@/components/CustomTable.vue";
import NavPanel from "@/components/NavPanel.vue";
import CreateFunctionForm from "@/forms/CreateFunctionForm.vue";
import EditFunctionForm from "@/forms/EditFunctionForm.vue";
import InfoFunctionForm from "@/forms/InfoFunctionForm.vue";
export default {
  name: "functionsPage",
  computed: {
    CreateFunctionForm() {
      return CreateFunctionForm
    },
    EditFunctionForm() {
      return EditFunctionForm
    },
    InfoFunctionForm() {
      return InfoFunctionForm
    }
  },
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
      { text: 'ID', value: 'id' },
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