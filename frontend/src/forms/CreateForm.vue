<template>
  <div>
    <v-text-field
      v-model="value.name"
      label="Name"
      hide-details="auto"
    ></v-text-field>
    <v-text-field
      v-model="value.param1"
      label="Param1"
      hide-details="auto"
    ></v-text-field>
    <v-text-field
      v-model="value.param2"
      label="Param2"
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
  name: "CreateForm",
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
        name: null,
        param1: null,
        param2: null,
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