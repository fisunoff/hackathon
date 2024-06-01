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
        :table-title="'Сертификаты'"
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
      apiPath: 'protection_certificate/api/',
      data: [],
      headers: [],
    }
  },
  async mounted() {
    const {data} = await this.$ajax.get(this.apiPath)
    this.data = data
    this.splitData(this.data)
    this.headers = [
      { text: '№ сертификата', value: 'number' },
      { text: 'Дата внесения в реестр', value: 'date_added' },
      { text: 'Срок действия сертификата', value: 'validity_period' },
      { text: 'Наименование средства (шифр)', value: 'tool' },
      { text: 'Наименования документов, требованиям которых соответствует средство', value: 'documents' },
      { text: 'Схема сертификации', value: 'certification_schema' },
      { text: 'Испытательная лаборатория', value: 'laboratory' },
      { text: 'Орган по сертификации', value: 'agency' },
      { text: 'Заявитель', value: 'applicant' },
      { text: 'Реквизиты заявителя (индекс, адрес, телефон)', value: 'requisites' },
      { text: 'Информация об окончании срока технической поддержки, полученная от заявителя', value: 'support_period' },
      { text: 'Функции', value: 'functions' },

    ]
  },
  methods: {
    replaceSpace(el) {
      if (el === "")
        return "—"
      else return el
    },
    splitData(data) {
      data.forEach(el => {
        el.functions = el.functions.map(el2 => el2.title).join(', ');
      });
      data.forEach(el => {
        el.functions = this.replaceSpace(el.functions)
      })
      data.forEach(el => {
        el.tool = el.tool.title
      });
    }
  }
}
</script>

<style scoped>

</style>