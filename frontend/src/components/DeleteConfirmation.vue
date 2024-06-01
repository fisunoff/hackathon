<template>
  <div>
    <span>Вы действительно хотите удалить запись?</span>
    <div class="d-flex" style="margin-top: 16px">
      <v-btn
        color="black"
        style="color: #fff"
        @click="close"
      >
        Отмена
      </v-btn>
      <v-btn
        color="error"
        style="margin-left: 303px;"
        @click="remove"
      >
        Удалить
      </v-btn>
    </div>

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