<template>
  <div class="d-flex">
    <nav-panel />
     <v-data-table
      v-if="data.length === 0"
      class="elevation-1"
      loading
      loading-text="Загрузка..."
      style="width: 100%"
    ></v-data-table>
    <custom-table
        :key="data.length"
        v-if="data.length > 0"
        :items="data"
        :headers="headers"
        :api-path="apiPath"
        :table-title="'Изменения'"
        :have-filter="true"
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
      apiPath: 'protection_certificate/diff/',
      data: [],
      headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(this.apiPath)
    this.data = data
    this.headers = [
      { text: 'Тип изменения', value: 'reason' },
      { text: '№ сертификата', value: 'number' },
      { text: 'Дата внесения в реестр (старое)', value: 'date_added_old' },
      { text: 'Дата внесения в реестр (новое)', value: 'date_added_new' },
      { text: 'Срок действия сертификата (старое)', value: 'validity_period_old' },
      { text: 'Срок действия сертификата (новое)', value: 'validity_period_new' },
      { text: 'СЗИ (старое)', value: 'tool_old' },
      { text: 'СЗИ (новое)', value: 'tool_new' },
      { text: 'Наименования документов, требованиям которых соответствует средство (старое)', value: 'documents_old' },
      { text: 'Наименования документов, требованиям которых соответствует средство (новое)', value: 'documents_new' },
      { text: 'Схема сертификации (старое)', value: 'certification_schema_old' },
      { text: 'Схема сертификации (новое)', value: 'certification_schema_new' },
      { text: 'Испытательная лаборатория (старое)', value: 'laboratory_old' },
      { text: 'Испытательная лаборатория (новое)', value: 'laboratory_new' },
      { text: 'Орган по сертификации (старое)', value: 'agency_old' },
      { text: 'Орган по сертификации (новое)', value: 'agency_new' },
      { text: 'Заявитель (старое)', value: 'applicant_old' },
      { text: 'Заявитель (новое)', value: 'applicant_new' },
      { text: 'Реквизиты заявителя (индекс, адрес, телефон) (старое)', value: 'requisites_old' },
      { text: 'Реквизиты заявителя (индекс, адрес, телефон) (новое)', value: 'requisites_new' },
      { text: 'Информация об окончании срока технической поддержки, полученная от заявителя (старое)', value: 'support_period_old' },
      { text: 'Информация об окончании срока технической поддержки, полученная от заявителя (новое)', value: 'support_period_new' },
    ]
  },
}
</script>

<style scoped>

</style>