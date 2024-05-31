<template>
  <div class="d-flex">
    <nav-panel />
    <custom-table
        :key="data.length"
        v-if="data.length > 0"
        :items="data"
        :headers="headers"
        :api-path="apiPath"
        :table-title="'СЗИ'"
        style="width: 100%"
    />
  </div>
</template>

<script>

import CustomTable from "@/components/CustomTable.vue";
import NavPanel from "@/components/NavPanel.vue";
export default {
  name: "currentDataPage",
  components: {CustomTable, NavPanel},
  data() {
    return {
      apiPath: 'protection_tool/api/',
      data: [],
      newData: [],
      headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(this.apiPath)
    this.data = data
    this.splitData(this.data)
    this.headers = [
      { text: 'СЗИ', value: 'title' },
      { text: '№ сертификата', value: 'number' },
      // { text: 'Дата внесения в реестр', value: 'date_added' },
      // { text: 'Срок действия сертификата', value: 'validity_period' },
      // { text: 'Наименование средства (шифр)', value: 'documents' },
      // { text: 'Наименования документов, требованиям которых соответствует средство', value: 'certification_schema' },
      // { text: 'Схема сертификации', value: 'laboratory' },
      // { text: 'Испытательная лаборатория', value: 'agency' },
      // { text: 'Орган по сертификации', value: 'applicant' },
      // { text: 'Заявитель', value: 'requisites' },
      // { text: 'Реквизиты заявителя (индекс, адрес, телефон)', value: 'support_period' },
      // { text: 'Информация об окончании срока технической поддержки, полученная от заявителя', value: 'functions' },
    ]
  },
  methods: {
    splitData(data) {
      data.forEach(el => {
          el.number = el.certificates.map(el2 => el2.number).join(', ');
      });
      // data.map(el => el.number = el.certificates.numbers).join('\n')
      // data.map(el => el.date_added = el.certificates.map(el2 => el2.date_added))
      // data.map(el => el.validity_period = el.certificates.map(el2 => el2.validity_period))
      // data.map(el => el.documents = el.certificates.map(el2 => el2.documents))
      // data.map(el => el.certification_schema = el.certificates.map(el2 => el2.certification_schema))
      // data.map(el => el.laboratory = el.certificates.map(el2 => el2.laboratory))
      // data.map(el => el.agency = el.certificates.map(el2 => el2.agency))
      // data.map(el => el.applicant = el.certificates.map(el2 => el2.applicant))
      // data.map(el => el.requisites = el.certificates.map(el2 => el2.requisites))
      // data.map(el => el.support_period = el.certificates.map(el2 => el2.support_period))
      // data.map(el => el.functions = el.certificates.map(el2 => this.mergeFunctions(el2.functions)))
    },
  }
}
</script>

<style scoped>

</style>