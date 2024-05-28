<template>
  <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h5">Добавить запись</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <template>
              <component :is="form" />
            </template>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Закрыть
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>
<script>
export default {
  name: "CustomModal",
  props: {
    form: {
      type: Object,
      required: false,
      default: null
    }
  },
  data() {
    return {
      dialog: false,
    }
  }
}
</script>
<style scoped>

</style>