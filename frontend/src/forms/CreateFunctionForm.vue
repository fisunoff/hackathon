<template>
  <div>
    <v-text-field
      v-model="value.title"
      label="Наименование"
      hide-details="auto"
    ></v-text-field>
    <v-text-field
      v-model="value.symbol"
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
        @click="create"
      >
        Добавить
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
        title: null,
        symbol: null,
      },
    }
  },
  methods: {
    close() {
      this.$modal.dialog = false
    },
    create() {
      if (this.item !== null) {
        this.$ajax.post(this.apiPath, {...this.value})
        this.close()
        this.$table.items.push(this.value)
      }
    },
  }
}
</script>

<style scoped>

</style>