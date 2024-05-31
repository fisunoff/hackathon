<template>
  <div>
    <v-text-field
      :value="value.title"
      v-model="newValue.title"
      label="Наименование"
      hide-details="auto"
    ></v-text-field>
    <v-text-field
      :value="value.symbol"
      v-model="newValue.symbol"
      label="Условное обозначение"
      hide-details="auto"
    ></v-text-field>
    <v-btn
        color="blue darken-1"
        text
        @click="close"
      >
        Закрыть
      </v-btn>
      <v-btn
        color="blue darken-1"
        text
        @click="edit"
      >
        Изменить
      </v-btn>
  </div>
</template>

<script>
export default {
  name: "CreateFunctionForm",
  inject: ['$modal', '$table'],
  props: {
    apiPath: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      value: {
        title: '',
        symbol: ''
      },
      newValue: {
        title: '',
        symbol: ''
      },
    }
  },
  created() {
    this.newValue = Object.assign(this.newValue, this.$table.formValue)
  },
  mounted() {
    this.value = this.$table.formValue
  },
  methods: {
    close() {
      this.$modal.dialog = false
    },
    edit() {
      if (this.newValue !== null) {
        this.$ajax.put(`${this.apiPath}${this.value.id}/`, {...this.newValue})
        this.close()
      }
      this.$table.formValue = Object.assign(this.value, this.newValue)
    },
  }
}
</script>

<style scoped>

</style>