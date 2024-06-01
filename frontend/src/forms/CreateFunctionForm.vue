<template>
  <div>
    <v-text-field
      v-model="value.title"
      label="Наименование"
      outlined
      dense
      hide-details="auto"
      class="form-field"
    ></v-text-field>
    <v-text-field
      v-model="value.symbol"
      label="Условное обозначение"
      outlined
      dense
      class="form-field"
      hide-details="auto"
    ></v-text-field>
    <div>
      <v-btn
        color="black"
        style="color: #fff"
        @click="close"
      >
        Закрыть
      </v-btn>
      <v-btn
        color="rgba(254, 206, 9, 1)"
        style="margin-left: 303px;"
        @click="create"
      >
        Добавить
      </v-btn>
    </div>

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
.form-field {
  margin: 8px 0;
}

</style>