<template>
  <div class="d-flex">
    <nav-panel />
    <custom-table
        :key="data.length"
        v-if="data.length > 0"
        :items="data"
        :headers="headers"
        :api-path="apiPath"
        :table-title="'Изменения'"
        style="width: 100%"
    >
      <date-filter />
    </custom-table>
  </div>
</template>

<script>

import CustomTable from "@/components/CustomTable.vue";
import NavPanel from "@/components/NavPanel.vue";
import DateFilter from "@/components/DateFilter.vue";
export default {
  name: "changeDataPage",
  components: {CustomTable, NavPanel, DateFilter},
  data() {
    return {
      apiPath: 'test_case/api/',
      data: [],
      headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(this.apiPath)
    this.data = data
    this.headers = [
      { text: '№ сертификата', value: '' },
      { text: 'Статус сертификата', value: '' },
      { text: '№ сертификата', value: '' },
      { text: 'Дата внесения в реестр', value: 'param1' },
      { text: 'Срок действия сертификата', value: 'param2' },
      { text: 'Наименование средства (шифр)', value: 'param3' },
      { text: 'Наименования документов, требованиям которых соответствует средство', value: 'param3' },
      { text: 'Схема сертификации', value: 'param3' },
      { text: 'Испытательная лаборатория', value: 'param3' },
      { text: 'Орган по сертификации', value: 'param3' },
      { text: 'Заявитель', value: 'param3' },
      { text: 'Реквизиты заявителя (индекс, адрес, телефон)', value: 'param3' },
      { text: 'Информация об окончании срока технической поддержки, полученная от заявителя', value: 'param3' },
    ]
  },
  methods: {

  }
}
</script>

<style scoped>

</style>