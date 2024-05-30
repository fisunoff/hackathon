<template>
  <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h5">{{ modalTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <template>
              <component :is="form" v-bind="{ apiPath: apiPath}" />
            </template>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
</template>
<script>
export default {
  name: "CustomModal",
  provide() {
    return {
      $modal: this,
    }
  },
  props: {
    form: {
      type: Object,
      required: false,
    },
    apiPath: {
      type: String,
      required: true,
    },
    modalTitle: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      dialog: false,
    }
  },
}
</script>
<style scoped>

</style>