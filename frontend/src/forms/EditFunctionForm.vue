<template>
  <div>
    <v-text-field
      :value="value.title"
      v-model="newValue.title"
      label="Наименование"
      outlined
      dense
      hide-details="auto"
      class="form-field"
    ></v-text-field>
    <v-text-field
      :value="value.symbol"
      v-model="newValue.symbol"
      label="Условное обозначение"
      outlined
      dense
      hide-details="auto"
      class="form-field"
    ></v-text-field>
    <div class="d-flex">
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
        @click="edit"
      >
        Изменить
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
.form-field {
  margin: 8px 0;
}

</style>