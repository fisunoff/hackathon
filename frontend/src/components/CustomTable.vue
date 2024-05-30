<template>
  <div class="pa-4">
    <div class="d-flex">
      <span>{{ tableTitle }}</span>
      <v-btn color="primary" class="ml-auto" @click="addItem">Добавить</v-btn>
    </div>
    <v-data-table
      dense
      :headers="headers"
      :items="items"
      :footer-props="{
        'items-per-page-options': [10, 25, 50, 100, -1]
      }"
      :items-per-page="50"
      class="elevation-1"
    >
      <template v-slot:item="{ item }">
        <tr>
          <td v-for="(col,index) in headers" :key="index">{{ item[col.value] }}</td>
          <td class="action-cell">
            <v-icon
              small
              class="mr-2"
              @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              small
              @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </td>
        </tr>
    </template>
    </v-data-table>
    <custom-modal
        ref="modal"
        :form="useForm"
        :api-path="apiPath"
        :modal-title="modalTitle"
    />
  </div>
</template>

<script>

import CustomModal from "@/components/CustomModal.vue";
import CreateForm from "@/forms/CreateForm.vue";

export default {
  name: "CustomTable",
  provide() {
    return {
      $table: this
    }
  },
  components: {CustomModal},
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    apiPath: {
      type: String,
      required: true,
    },
    tableTitle: {
      type: String,
      required: false,
    }
  },
  data() {
    return {
      openModal: false,
      useForm: null,
      modalTitle: null,
    }
  },
  mounted() {
    console.log(this.items)
  },
  methods: {
    addItem() {
      this.useForm = CreateForm
      this.modalTitle = 'Добавить запись'
      this.$refs.modal.dialog = true
    },
    editItem(item) {
      console.log('Editing:', item);
    },
    deleteItem(item) {
      console.log('Deleting:', item);
    },
  }
}
</script>

<style scoped>
  .action-cell {
    width: 100px;
  }
</style>