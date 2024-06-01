<template>
  <div>

    <div class="d-flex">
      <v-btn
        color="black"
        style="color: #fff"
        @click="close"
      >
        Закрыть
      </v-btn>
    </div>

  </div>
</template>

<script>
export default {
  name: "InfoFunctionForm",
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
  mounted() {
    this.value = this.$table.formValue
  },
  methods: {
    close() {
      this.$modal.dialog = false
    },
  }
}
</script>

<style scoped>
.form-field {
  margin: 8px 0;
}

</style>