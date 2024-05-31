<template>
  <div>
    <span>Вы действительно хотите удалить запись?</span>
    <v-btn
        color="blue darken-1"
        text
        @click="close"
      >
        Отмена
      </v-btn>
      <v-btn
        color="blue darken-1"
        text
        @click="remove"
      >
        Удалить
      </v-btn>
  </div>
</template>
<script>
export default {
  name: "DeleteConfirmation",
  inject: ['$modal', '$table'],
  props: {
    apiPath: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      value: {},
    }
  },
  mounted() {
    this.value = this.$table.formValue
  },
  methods: {
    close() {
      this.$modal.dialog = false
    },
    remove() {
      if (this.value !== null) {
        this.$ajax.delete(`${this.apiPath}${this.value.id}/`)
        this.close()
      }
    },
  }
}
</script>

<style scoped>

</style>